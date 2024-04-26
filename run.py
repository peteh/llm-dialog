from tts import PiperTTS, XTTS
from dialogue import DialogueManager, ParticipantOllama, SystemMessageGenerator, SystemMessageGeneratorGerman

#system_a = SystemMessageGenerator("Horst", "Amy", "Banning flights for the environment", "You believe flights should never be banned as they are useful for economic growth. ")
#system_b = SystemMessageGenerator("Amy", "Horst", "Banning flights for the environment", "You want to ban flights because it's important to save the environment. ")

system_a = SystemMessageGeneratorGerman("Angela Merkel", "Marco", "Der Sozialstaat und Wirtschaftswachstum", "Du glaubst, dass der Sozialstaat und Steuern nötig sind um eine lebenswerte Welt mit gutem Wirtschaftswachstum zu schaffen. ")
system_b = SystemMessageGeneratorGerman("Marco", "Angela Merkel", "Der Sozialstaat und Wirtschaftswachstum", "Du glaubst, dass der Staat so klein wie möglich zu halten ist, Steuern so niedrig wie möglich zu halten sind und das soziale Netz nicht nötig ist um möglichst gute wirtschaftliche Leistungen zu erreichen. Du vertrittst deinen Stand sehr aggressiv. ")

a = ParticipantOllama(system_a.system_message(), "llama3:8b-instruct-q6_K", "http://homeassistant.home:11434")
b = ParticipantOllama(system_b.system_message(), "llama3:8b-instruct-q6_K", "http://homeassistant.home:11434")

tts_a = PiperTTS("de_DE-karlsson-low")
tts_b = PiperTTS("de_DE-thorsten_emotional-medium", 1)
#tts_a = XTTS("xtts/xtts_merkel1", default_lang="de")
#tts_b = XTTS("xtts/xtts_marco1", default_lang="de")


dialog_manager = DialogueManager(a, tts_a, b, tts_b, "Hallo")
dialog_manager.process(2)
