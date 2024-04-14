import whisper


def transcribe_audio(audio_path: str, model_name: str = "small", **model_parameters) -> str:
    model = whisper.load_model(model_name)
    result = model.transcribe(audio_path, **model_parameters)
    return result["text"]
