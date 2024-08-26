import speech_recognition as sr

speech = sr.Recognizer()

with sr.AudioFile(r'Archivos\audio.wav') as source:
    audio_data = speech.record(source)

    texto = speech.recognize_google(audio_data, language='es-AR', show_all=True)
    print(texto)