from pytube import YouTube, Stream


def load_audio(url: str) -> str:
    video = YouTube(url)
    stream: Stream = video.streams.filter(only_audio=True).order_by("abr").desc()[0]
    return stream.download()
