from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='transcriber'),
    path('youtube_transcriber', views.youtube_transcriber, name='youtube_transcriber'),
    path('file_transcriber', views.file_transcriber, name='file_transcriber'),
    path('voice_transcriber', views.voice_transcriber, name='voice_transcriber'),
]
