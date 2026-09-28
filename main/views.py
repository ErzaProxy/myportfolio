from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .forms import ProjectForm, ArtForm
import datetime
from main.models import Experience, Project, Art
from main.models import Mahasiswa
from django.contrib.auth.decorators import login_required  
from django.core.exceptions import PermissionDenied        

def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
    context = {
        "name": "Muhammad Raihan Al Qadri Kusumaputra",
        "npm": "2506602334",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "I'm Qodri/Bodrex. An Otaku CS Student that's interested on Game Dev and Data Science, though still has zero understanding about them."
        ),
        "last_login": last_login,
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
    json_response = get_arts_json(request)
    arts = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    arts = [art.object for art in arts]
    nama_query = request.GET.get("nama", "").strip()
    
    context = {
        "name": "Muhammad Raihan Al Qadri Kusumaputra",
        "art_list": arts,
        "nama_query": nama_query,
    }
    return render(request, "artfolio.html", context)

@login_required(login_url="/login/") 
def create_art(request):
    form = ArtForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("main:show_artfolio")
        
    context = {
        "name": "Muhammad Raihan Al Qadri Kusumaputra",
        "form": form,
    }
    return render(request, "artfolio_form.html", context)

def get_arts_json(request):
    nama_query = request.GET.get("nama", "").strip()
    arts = Art.objects.all()
    if nama_query:
        arts = arts.filter(nama__icontains=nama_query)
    
    arts_json = serializers.serialize("json", arts)
    return HttpResponse(arts_json, content_type="application/json")

def delete_art(request, art_id):
    art = get_object_or_404(Art, pk=art_id)
    if request.method == "POST":
        art.delete()
    return redirect("main:show_artfolio")

def edit_art(request, art_id):
    art = get_object_or_404(Art, pk=art_id)
    form = ArtForm(request.POST or None, instance=art)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("main:show_artfolio")

    context = {
        "name": "Muhammad Raihan Al Qadri Kusumaputra",
        "form": form,
    }
    return render(request, "artfolio_form.html", context)

def show_experience(request):
    context = {
        "name": "Muhammad Raihan Al Qadri Kusumaputra",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_project(request):
    json_response = get_projects_json(request)

    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    projects = [project.object for project in projects]
    nama_query = request.GET.get("nama", "").strip()
    
    context = {
        "name": "Muhammad Raihan Al Qadri Kusumaputra",
        "project_list": projects,
        "nama_query": nama_query,   
    }
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

def create_project(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_project")

    context = {
        "name": "Muhammad Raihan Al Qadri Kusumaputra",
        "form": form,
    }
    return render(request, "project_form.html", context)

def get_projects_json(request):
    nama_query = request.GET.get("nama", "").strip()
    projects = Project.objects.all()
    if nama_query:
        projects = projects.filter(nama__icontains=nama_query)
    
    projects_json = serializers.serialize(
    "json", projects, use_natural_foreign_keys=True  # Tambahkan argumen ini
    )
    return HttpResponse(projects_json, content_type="application/json")

@login_required(login_url="/login/") 
def delete_project(request, project_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_project")

    return redirect("main:show_project")

def edit_project(request, project_id):
    project = get_object_or_404(Art, pk=project_id)
    form = ProjectForm(request.POST or None, instance=project)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("main:show_project")

    context = {
        "name": "Muhammad Raihan Al Qadri Kusumaputra",
        "form": form,
    }
    return render(request, "project_form.html", context)

# Tanpa cek is_superuser: semua akun yang sudah login boleh memberi star
@login_required(login_url="/login/")
def toggle_star(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        # Kalau akun ini sudah pernah memberi star, batalkan star-nya.
        # Kalau belum, tambahkan star.
        if request.user in project.starred_by.all():
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)

    return redirect("main:show_project")

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": "Muhammad Raihan Al Qadri Kusumaputra",
        "form": form,
    }
    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Muhammad Raihan Al Qadri Kusumaputra",
        "form": form,
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response

