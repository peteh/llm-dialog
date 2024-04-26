from tts import PiperTTS
from dialogue import DialogueManager, ParticipantOllama, SystemMessageGeneratorGerman

system_a = SystemMessageGeneratorGerman("Angela Merkel", "Marco", "Der Sozialstaat und Wirtschaftswachstum", "Du glaubst, dass der Sozialstaat und Steuern nötig sind um eine lebenswerte Welt mit gutem Wirtschaftswachstum zu schaffen. ")
system_b = SystemMessageGeneratorGerman("Marco", "Angela Merkel", "Der Sozialstaat und Wirtschaftswachstum", "Du glaubst, dass der Staat so klein wie möglich zu halten ist, Steuern so niedrig wie möglich zu halten sind und das soziale Netz nicht nötig ist um möglichst gute wirtschaftliche Leistungen zu erreichen. Du vertrittst deinen Stand sehr aggressiv. ")

a = ParticipantOllama(system_a.system_message(), "llama3")
b = ParticipantOllama(system_b.system_message(), "llama3")

tts_a = PiperTTS("de_DE-karlsson-low")
tts_b = PiperTTS("de_DE-thorsten_emotional-medium", 1)

dialog_manager = DialogueManager(a, tts_a, b, tts_b, "Hallo")

# process n dialogues between A and B
dialog_manager.process(5)