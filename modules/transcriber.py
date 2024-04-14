import io
import os

from libs.youtube_loader import load_audio
from libs.whisper_transcriber import transcribe_audio
from libs.buffer_saver import save_buffer


def transcriber(transcription_function):
    def transcribe(*args, **kwargs):
        try:
            return transcription_function(*args, **kwargs)
        except Exception as e:
            msg = f"Error while trying to transcribe: {e}"
            print(msg)
            return msg

    return transcribe


@transcriber
def transcribe_youtube_video(url: str, **transcription_parameters) -> str:
    audio_file_path = load_audio(url)
    transcription = transcribe_audio_file(audio_file_path, **transcription_parameters)
    os.remove(audio_file_path)
    return transcription


@transcriber
def transcribe_buffer(buffer: io.BytesIO, name: str, **transcription_parameters) -> str:
    audio_file_path = save_buffer(buffer, name)
    transcription = transcribe_audio_file(audio_file_path, **transcription_parameters)
    os.remove(audio_file_path)

    return transcription


@transcriber
def transcribe_audio_file(audio_file_path: str, **transcription_parameters) -> str:
    return transcribe_audio(audio_file_path, **transcription_parameters)
