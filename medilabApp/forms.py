from django import forms

from medilabApp.models import ImageModel


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields  = '__all__'