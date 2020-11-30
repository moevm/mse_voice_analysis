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
            new_file = '/cut' + str(start) + '-' + str(end) + '.wav'
            new_path = '../res/' + str(path).replace('\\', '_')
            try:
                os.mkdir(new_path)
            except FileExistsError:
                pass
            finally:
                audio.export(new_path + new_file, format="wav")
                paths.append(new_path + new_file)
        return paths
