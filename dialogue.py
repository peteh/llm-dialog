from abc import ABC, abstractmethod
import wave
import tempfile
from ollama import Client
from tts import TextToSpeechEngine



class Participant(ABC):
    @abstractmethod
    def add_assistant_message(self, assistant_message) -> None:
        pass
    
    @abstractmethod
    def respond_to(self, user_message) -> str:
        pass
    
    @abstractmethod
    def clear(self) -> None:
        pass

class SystemMessageGenerator():
    def __init__(self, name: str, other_name: str, topic:str, stand_point: str):
        self._name = name
        self._other_name = other_name
        self._topic = topic
        self._stand_point = stand_point
    
    def system_message(self):
        return f"You are 'f{self._name}'. The user's name is '{self._other_name}'. Please answer with short answers as you would in a spoken dialog between 2 pleople. The topic is '{self._topic}'. You have to defend your stand point. This is your standpoint: '{self._stand_point}'"

class SystemMessageGeneratorGerman():
    def __init__(self, name: str, other_name: str, topic:str, stand_point: str):
        self._name = name
        self._other_name = other_name
        self._topic = topic
        self._stand_point = stand_point
    
    def system_message(self):
        return f"Du bist 'f{self._name}'. Dein User ist '{self._other_name}'. Bitte anworte immer kurz wie in einem direkten Gespräch zwischen 2 Menschen. Das Thema ist '{self._topic}'. Du musst deinen Standpunkt verteidigen. Dies ist dein Standpunkt: '{self._stand_point}'"



class ParticipantOllama(Participant):
    def __init__(self, system_message: str, model = "llama3", host = "http://localhost:11434") -> None:
        self._system_message = system_message
        self._model = model
        self._client = Client(host=host)
        self._messages = []
        self._init_messages()

    def _init_messages(self) -> None:
        self._messages = []
        sysmsg = {
            "role": "system",
            "content": self._system_message
        }
        self._messages.append(sysmsg)

    def add_assistant_message(self, assistant_message) -> None:
        msg = { 
            "role": "user",
            "content": assistant_message,
        }
        self._messages.append(msg)

    def respond_to(self, user_message) -> str:
        msg = { 
            "role": "user",
            "content": user_message,
        }
        self._messages.append(msg)

        response = self._client.chat(model=self._model, messages=self._messages)
        self._messages.append(response["message"])
        return response["message"]["content"]

    def clear(self) -> None:
        self._init_messages()

class DialogueManager():
    DEFAULT_OUTPUT_DIR = "output"
    
    def __init__(self, participant_a: Participant, tts_a: TextToSpeechEngine, participant_b: Participant, tts_b: TextToSpeechEngine, first_message_b_to_a, output_dir = DEFAULT_OUTPUT_DIR) -> None:
        self._participant_a = participant_a
        self._participant_b = participant_b
        self._tts_a = tts_a
        self._tts_b = tts_b
        self._first_message_b_to_a = first_message_b_to_a
    
        self._output_dir = output_dir
    
    def _join_wav_files(self, input_files, output_file):
        # Open the first input file to get parameters
        with wave.open(input_files[0], 'rb') as first_file:
            params = first_file.getparams()

            # Open the output file for writing
            with wave.open(output_file, 'wb') as output_wav:
                output_wav.setparams(params)

                # Write data from each input file to the output file
                for input_file in input_files:
                    with wave.open(input_file, 'rb') as input_wav:
                        output_wav.writeframes(input_wav.readframes(input_wav.getnframes()))
  
    def process(self, num_responses):
        wav_files = []
        msg_counter = 0
        transcript = open(f"{self._output_dir}/dialogue.txt", "w", encoding="UTF-8")
        response_b_to_a = self._first_message_b_to_a
        self._participant_b.add_assistant_message(response_b_to_a)
        print(f"B: {response_b_to_a}")
        transcript.write(f"B: {response_b_to_a}\n")
        wav_name_start_b = f"{self._output_dir}/{msg_counter}_b.wav"
        self._tts_a.tts(response_b_to_a, wav_name_start_b)
        wav_files.append(wav_name_start_b)
        splitter = "======================\n"

        for i in range(1, num_responses+1):
            transcript.write(splitter)
            print(f"Dialogue {i}/{num_responses}")
            print(splitter)
            response_a_to_b = self._participant_a.respond_to(response_b_to_a)
            print(f"A: {response_a_to_b}")
            transcript.write(f"A: {response_a_to_b}\n")
            wav_name_a = f"{self._output_dir}/{msg_counter}_a.wav"
            msg_counter += 1
            self._tts_a.tts(response_a_to_b, wav_name_a)
            wav_files.append(wav_name_a)
            transcript.write(splitter)
            print(splitter)
            response_b_to_a = self._participant_b.respond_to(response_a_to_b)
            print(f"B: {response_b_to_a}")
            transcript.write(f"B: {response_b_to_a}\n")
            wav_name_b = f"{self._output_dir}/{msg_counter}_b.wav"
            msg_counter += 1
            self._tts_b.tts(response_b_to_a, wav_name_b)
            wav_files.append(wav_name_b)
        self._join_wav_files(wav_files, f"{self._output_dir}/dialogue.wav")
        transcript.close()
        
