from django.shortcuts import render

from main.models import Experience
from main.models import Mahasiswa


def show_main(request):
    context = {
        "name": "Muhammad Raihan Al Qadri Kusumaputra",
        "npm": "2506602334",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "I'm Qodri/Bodrex. An Otaku CS Student that's interested on Game Dev and Data Science, though still has zero understanding about them."
        ),
    }
    return render(request, "index.html", context)

def show_menu(request):
    context = {
            "name": "Muhammad Raihan Al Qadri Kusumaputra",
        }
    return render(request, "menu.html", context)

def show_about(request):
    context = {
        "name": "Muhammad Raihan Al Qadri Kusumaputra",
        "npm": "2506602334",
        "study_program": "Ilmu Komputer",
        "birth_date": "5 Juni 2007",
        "hobbies": "Reading, watching, writing fictions.",
        "fav_food": "Sate Padang, Kari Jepang",
        "bio": "I'm Qodri/Bodrex. An Otaku CS Student that's interested on Game Dev and Data Science, though still has zero understanding about them."
    }
    return render(request, "about.html", context)

def show_artfolio(request):
    context = {}
    return render(request, "artfolio.html", context)

def show_experience(request):
    context = {
        "name": "Muhammad Raihan Al Qadri Kusumaputra",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_project(request):
    context = {}
    return render(request, "project.html", context)

def show_contact(request):
    context = {
            "name": "Muhammad Raihan Al Qadri Kusumaputra",
            "npm": "2506602334",
            "study_program": "S1 Ilmu Komputer",
            "bio": (
                "I'm Qodri/Bodrex. An Otaku CS Student that's interested on Game Dev and Data Science, though still has zero understanding about them."
            ),
        }
    return render(request, "contact.html", context)
# Untuk Hands-on
def index(request):
    mahasiswa_list = Mahasiswa.objects.all()
    context = {
        'name': 'Mahasiswa PBP',
        'mahasiswa_list': mahasiswa_list,
    }
    return render(request, 'index.html', context)
