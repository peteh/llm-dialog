from tts import PiperTTS, XTTS
from dialogue import DialogueManager, ParticipantOllama, SystemMessageGenerator

system_a = SystemMessageGenerator("Arnold", "Angy", "Banning flights for the environment", "You believe flights should never be banned as they are useful for economic growth. ")
system_b = SystemMessageGenerator("Angy", "Arnold", "Banning flights for the environment", "You want to ban flights because it's important to save the environment. ")

a = ParticipantOllama(system_a.system_message(), "llama3")
b = ParticipantOllama(system_b.system_message(), "llama3")

tts_a = PiperTTS("en_US-joe-medium")
tts_b = PiperTTS("en_US-amy-medium")

#tts_a = XTTS("xtts/xtts_arny1", default_lang="en")
#tts_b = XTTS("xtts/xtts_merkel1", default_lang="en")

dialog_manager = DialogueManager(a, tts_a, b, tts_b, "Hello")

# process n dialogues between A and B
dialog_manager.process(3)