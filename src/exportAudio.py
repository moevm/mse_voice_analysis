from pydub import AudioSegment


class ExportAudio:
    @staticmethod
    def export(splits, path):
        paths = []
        for start, end in splits:
            audio = AudioSegment.from_file(path)[start * 1000:end * 1000]
            new_file = 'cut' + str(start) + '-' + str(end) + '.mp3'
            new_path = './audio_data_test/' + new_file
            audio.export(new_path, format="mp3")
            paths.append(new_path)
        return paths
