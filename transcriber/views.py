from django.shortcuts import render
from modules import transcriber
from . import forms


def home(request):
    return render(request, "base_text.html", {
        "title": "Transcriber",
        "text": "",
    })


def youtube_transcriber(request):
    if request.method == "GET":
        return render(request, "base_form.html", {
            "title": "YouTube Transcriber",
            "form": forms.UrlTranscriberForm(),
        })

    if request.method == "POST":
        return process_url_form(request)


def file_transcriber(request):
    if request.method == "GET":
        return render(request, "base_form.html", {
            "title": "File Transcriber",
            "form": forms.FileTranscriberForm(),
        })

    if request.method == "POST":
        return process_file_form(request)


def voice_transcriber(request):
    if request.method == "GET":
        return render(request, "voice_form.html", {
            "title": "Voice Transcriber",
            "form": forms.FileTranscriberForm(),
        })

    if request.method == "POST":
        return process_file_form(request)


def process_url_form(request):
    url = request.POST.get("url")
    transcription = transcriber.transcribe_youtube_video(url)
    return transcription_result(request, transcription)


def process_file_form(request):
    file = request.FILES.get("file")
    transcription = transcriber.transcribe_buffer(file.file, file.name)
    return transcription_result(request, transcription)


def transcription_result(request, text: str):
    return render(request, "base_text.html", {
        "title": "Transcription Result",
        "text": text,
    })
