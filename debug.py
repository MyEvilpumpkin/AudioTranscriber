from modules.transcriber import transcribe_youtube_video

transcribed_audio = transcribe_youtube_video("https://www.youtube.com/watch?v=ZvWH0D2_y_I", model_name="large")

print(transcribed_audio)
