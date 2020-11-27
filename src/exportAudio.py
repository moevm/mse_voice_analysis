from pydub import AudioSegment


class ExportAudio:
    @staticmethod
    def export(splits, path):
        paths = []
        for start, end in splits:
            audio = AudioSegment.from_file(path)[start * 1000:end * 1000]
            new_file = 'cut' + str(start) + '-' + str(end) + '.wav'
            new_path = '../result/' + new_file
            audio.export(new_path, format="wav")
            paths.append(new_path)
        return paths