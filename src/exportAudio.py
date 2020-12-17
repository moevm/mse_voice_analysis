import os
from pydub import AudioSegment


class ExportAudio:
    @staticmethod
    def export(splits, path, rate=1):
        paths = []
        tmp = 0
        for start, end in splits:
            start = tmp
            end = int(end * rate) + 1
            tmp = end + 1
            audio = AudioSegment.from_file(path)[start * 1000:end * 1000]
            new_file = 'cut' + str(start) + '-' + str(end) + '.wav'
            new_path = './result/' + new_file
            audio.export(new_path, format="wav")
            paths.append(new_path)
        return paths
