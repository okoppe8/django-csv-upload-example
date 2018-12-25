from django import forms
from django.core.validators import FileExtensionValidator


class UploadForm(forms.Form):
    file = forms.FileField(
        validators=[FileExtensionValidator(['csv', ])])
