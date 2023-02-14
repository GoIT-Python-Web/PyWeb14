"""
У цьому прикладі класи VideoFile, AudioFile і SubtitleFile представляють складні підсистеми відеоплеєра.
Клас VideoPlayerFacade надає спрощений інтерфейс для відтворення відео за допомогою виклику play(), який, у свою чергу,
викликає методи окремих підсистем для декодування відео, аудіо та файлів субтитрів. Клієнтський код, який використовує
фасад, повинен знати лише про клас VideoPlayerFacade і не повинен турбуватися про складність окремих підсистем.
"""


class VideoFile:
    def __init__(self, filename):
        self.filename = filename

    def decode(self):
        print("Decoding video file:", self.filename)


class AudioFile:
    def __init__(self, filename):
        self.filename = filename

    def decode(self):
        print("Decoding audio file:", self.filename)


class SubtitleFile:
    def __init__(self, filename):
        self.filename = filename

    def decode(self):
        print("Decoding subtitle file:", self.filename)


class VideoPlayerFacade:
    def __init__(self, video_file, audio_file, subtitle_file):
        self.video_file = video_file
        self.audio_file = audio_file
        self.subtitle_file = subtitle_file

    def play(self):
        self.video_file.decode()
        self.audio_file.decode()
        self.subtitle_file.decode()


if __name__ == '__main__':
    video_file = VideoFile("action_movie.mp4")
    audio_file = AudioFile("action_movie.mp3")
    subtitle_file = SubtitleFile("action_movie.srt")

    player = VideoPlayerFacade(video_file, audio_file, subtitle_file)
    player.play()
