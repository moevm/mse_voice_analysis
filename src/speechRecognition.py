import speech_recognition as sr


class SpeechRecognition:
    def __init__(self, language='en-EN'):
        self.language = language
        self.recognizer = sr.Recognizer()

    def recognize_speech(self, path):
        file = sr.AudioFile(path)
        with file as source:
            audio = self.recognizer.record(source)
        result = self.recognizer.recognize_google(audio, language=self.language)
        return result


