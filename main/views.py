from django.shortcuts import render

from main.models import Experience


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


def show_experience(request):
    context = {
        "name": "Muhammad Raihan Al Qadri Kusumaputra",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)