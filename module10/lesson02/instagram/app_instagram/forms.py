from django.forms import ModelForm, ImageField, FileInput, CharField, TextInput

from .models import Picture


class PictureForm(ModelForm):
    description = CharField(max_length=350, widget=TextInput(attrs={"class": "form-control"}))
    path = ImageField(widget=FileInput(attrs={"class": "form-control"}))

    class Meta:
        model = Picture
        fields = ['description', 'path']
