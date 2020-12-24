import speech_recognition as sr
import webbrowser


class SpeechRecognition:
    def __init__(self, language='en-EN'):
        self.language = language
        self.recognizer = sr.Recognizer()

    def recognize_speech(self, path):
        result = ''
        file = sr.AudioFile(path)
        with file as source:
            audio = self.recognizer.record(source)
            try:
                result = self.recognizer.recognize_google(audio, language=self.language)
                return result
            except sr.UnknownValueError:
                file = sr.AudioFile(path)
                with file as _source:
                    for i in range(0, int(_source.DURATION), 10):
                        audio = self.recognizer.record(_source, duration=10)
                        try:
                            text = self.recognizer.recognize_google(audio, language=self.language) + ' '
                            result += text
                        except sr.UnknownValueError:
                            result += ' *** '
                        except sr.RequestError:
                            return 'Recognizer Api is unavailable'
        return result





