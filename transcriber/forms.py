from django import forms


class FileTranscriberForm(forms.Form):
    file = forms.FileField()


class UrlTranscriberForm(forms.Form):
    url = forms.URLField()

