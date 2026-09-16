from django.forms import ModelForm, TextInput, Textarea, URLInput, Select
from main.models import Project

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