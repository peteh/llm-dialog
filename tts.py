import logging
import os
import wave
from abc import ABC, abstractmethod
from typing import List
from piper.voice import PiperVoice
from piper.download import ensure_voice_exists, find_voice, get_voices

# XTTS
import torch
from TTS.tts.configs.xtts_config import XttsConfig
from TTS.tts.models.xtts import Xtts
import torchaudio

class TextToSpeechEngine(ABC):

    @abstractmethod
    def tts(self, text: str, wav_file_path: str) -> None:
        """
        Convert text to speech and save the audio to a WAV file.

        Args:
        - text (str): The text to convert to speech.
        - wav_file_path (str): Path to save the generated WAV file.
        """

class PiperTTS(TextToSpeechEngine):

    VOICE_DATA_DIR = "./piper_voice_data/"
    VOICE_CUSTOM_DIR = "./piper_voice_custom/"

    def __init__(self, voice_name: str, speaker_id = None, voice_cache_dir: str = VOICE_DATA_DIR, voice_custom_dir: str = VOICE_CUSTOM_DIR) -> None:
        self._voice_cache_dir = voice_cache_dir
        self._voice_custom_dir = voice_custom_dir

        # generate dirs for piper to store voices
        if not os.path.exists(self._voice_cache_dir):
            os.makedirs(self._voice_cache_dir)
        if not os.path.exists(self._voice_custom_dir):
            os.makedirs(self._voice_custom_dir)
        self._voices = get_voices(self._voice_cache_dir, update_voices=True)

        self._voice_name = voice_name
        self._speaker_id = speaker_id

        try:
            onnx_path, _ = find_voice(voice_name, [self._voice_cache_dir, self._voice_custom_dir])
        except ValueError:
            ensure_voice_exists(voice_name, [self._voice_cache_dir], self._voice_cache_dir, self._voices)
            onnx_path, _ = find_voice(voice_name, [self._voice_cache_dir, self._voice_custom_dir])

        self._voice = PiperVoice.load(onnx_path, config_path=None, use_cuda=False)

    def _get_voices(self) -> List[str]:
        return self._voices

    def tts(self, text: str, wav_file_path: str):
        synthesize_args = {
            "speaker_id": self._speaker_id,
            "length_scale": None,
            "noise_scale": None,
            "noise_w": None,
            "sentence_silence": 0.0,
        }
        with open(wav_file_path, "wb") as wav_io:
            with wave.open(wav_io, "wb") as wav_file:
                self._voice.synthesize(text, wav_file, **synthesize_args)


class XTTS(TextToSpeechEngine):
    def __init__(self, model_path: str, reference_wav: str = "reference.wav", default_lang : str = "en") -> None:
        xtts_config = "config.json"
        self._reference_wav = reference_wav
        self._model_path = model_path
        self._config = XttsConfig()
        self._config.load_json(f"{self._model_path}/{xtts_config}")
        self._model = Xtts.init_from_config(self._config)
        self._language = default_lang
        logging.info(f"Loading XTTS model: {self._model_path}")
        self._model.load_checkpoint(self._config, checkpoint_dir=self._model_path, use_deepspeed=False)
        if torch.cuda.is_available():
            self._model.cuda()
        logging.info("Model Loaded!")

    def tts(self, text: str, wav_file_path : str, language : str = None) -> bool:
        gpt_cond_latent, speaker_embedding = self._model.get_conditioning_latents(audio_path=f"{self._model_path}/{self._reference_wav}", 
                                                                                  gpt_cond_len=self._model.config.gpt_cond_len, 
                                                                                  max_ref_length=self._model.config.max_ref_len, 
                                                                                  sound_norm_refs=self._model.config.sound_norm_refs)
        target_lang = language if language is not None else self._language

        out = self._model.inference(
            text=text,
            language=target_lang,
            gpt_cond_latent=gpt_cond_latent,
            speaker_embedding=speaker_embedding,
            temperature=self._model.config.temperature, # Add custom parameters here
            length_penalty=self._model.config.length_penalty,
            repetition_penalty=self._model.config.repetition_penalty,
            top_k=self._model.config.top_k,
            top_p=self._model.config.top_p,
            enable_text_splitting = True
        )
        out["wav"] = torch.tensor(out["wav"]).unsqueeze(0)
        torchaudio.save(wav_file_path, out["wav"], 24000)
