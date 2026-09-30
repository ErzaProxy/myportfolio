from django.forms import ModelForm, TextInput, Textarea, URLInput, Select
from main.models import Project, Art
from django.utils.html import strip_tags
from django.core.exceptions import ValidationError

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "nama",
            "tipe",
            "deskripsi",
            "thumbnail",
            "link",
            "skillset",
        ]
        labels = {
            "nama": "Nama Project",
            "tipe": "Tipe Project",
            "deskripsi": "Deskripsi Project",
            "thumbnail": "Path Thumbnail",
            "link": "URL Project",
            "skillset": "Skillset",
        }
        widgets = {
            "nama": TextInput(
                attrs={
                    "placeholder": "Nama project",
                    "maxlength": 255,
                }
            ),
            "tipe": Select(
                attrs={
                    "class": "form-select",
                }
            ),
            "deskripsi": Textarea(
                attrs={
                    "placeholder": "Ceritakan tentang project ini...",
                    "rows": 4,
                }
            ),
            "thumbnail": TextInput(
                attrs={
                    "placeholder": "/static/img/project/iMaba.png",
                    "maxlength": 255,
                }
            ),
            "link": URLInput(
                attrs={
                    "placeholder": "https://bem.cs.ui.ac.id/imaba",
                }
            ),
            "skillset": TextInput(
                attrs={
                    "placeholder": "Next.js, TypeScript",
                    "maxlength": 255,
                }
            ),
        }
    def clean_nama(self):
        nama = strip_tags(self.cleaned_data["nama"]).strip()
        if not nama:
            raise ValidationError("Nama project tidak boleh hanya berisi tag HTML.")
        return nama

    def clean_deskripsi(self):
        return strip_tags(self.cleaned_data["deskripsi"]).strip()

    def clean_skillset(self):
        return strip_tags(self.cleaned_data["skillset"]).strip()
class ArtForm(ModelForm):
    class Meta:
        model = Art
        fields = [
            "nama",
            "deskripsi",
            "url",
        ]
        labels = {
            "nama": "Judul Karya",
            "deskripsi": "Deskripsi",
            "url": "URL Gambar",
        }
        widgets = {
            "nama": TextInput(
                attrs={
                    "placeholder": "Masukkan judul art",
                    "maxlength": 255,
                }
            ),
            "deskripsi": Textarea(
                attrs={
                    "placeholder": "Deskripsikan art ini",
                    "rows": 4,
                }
            ),
            "url": URLInput(
                attrs={
                    "placeholder": "https://...",
                }
            ),
        }
        
