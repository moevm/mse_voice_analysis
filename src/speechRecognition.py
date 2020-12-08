import speech_recognition as sr


class SpeechRecognition:
    def __init__(self, language='en-EN'):
        self.language = language
        self.recognizer = sr.Recognizer()

    def recognize_speech(self, path):
        result = ''
        file = sr.AudioFile(path)
        with file as source:
            for i in range(0, int(source.DURATION), 2):
                audio = self.recognizer.record(source, offset=i, duration=2)
                try:
                    result += self.recognizer.recognize_google(audio, language=self.language) + ' '
                except sr.UnknownValueError:
                    result += ' *** '
                except sr.RequestError:
                    return 'Recognizer Api is unavailable'
        return result





