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
from django.http import JsonResponse
from django.views.decorators.http import require_POST

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
    nama_query = request.GET.get("nama", "").strip()
    context = {
        "name": "Muhammad Raihan Al Qadri Kusumaputra",
        "form": ArtForm(),
        "nama_query": nama_query,
    }
    return render(request, "artfolio.html", context)

@login_required(login_url="/login/") 
def create_art(request):
    if not request.user.is_superuser: 
        raise PermissionDenied
    form = ArtForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("main:show_artfolio")
        
    context = {
        "name": "Muhammad Raihan Al Qadri Kusumaputra",
        "form": form,
    }
    return render(request, "artfolio_form.html", context)

@require_POST
def create_art_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse({"message": "Hanya Admin portofolio yang dapat menambahkan karya."}, status=403)
    
    form = ArtForm(request.POST)
    if form.is_valid():
        art = form.save()
        return JsonResponse({"message": "Karya berhasil ditambahkan.", "pk": str(art.id)}, status=201)
    
    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)

def get_arts_json(request):
    nama_query = request.GET.get("nama", "").strip()
    arts = Art.objects.prefetch_related('loved_by').all()
    if nama_query:
        arts = arts.filter(nama__icontains=nama_query)
    
    data = []
    for art in arts:
        loved_users = art.loved_by.all()
        is_loved = request.user in loved_users if request.user.is_authenticated else False
        loved_by_names = ", ".join([u.username for u in loved_users])
        
        data.append({
            "pk": str(art.id),
            "fields": {
                "nama": art.nama,
                "deskripsi": art.deskripsi,
                "url": art.url,
                "love_count": loved_users.count(),
                "is_loved": is_loved,
                "loved_by_names": loved_by_names,
            }
        })
    return JsonResponse(data, safe=False)

@login_required(login_url="/login/") 
def delete_art(request, art_id):
    if not request.user.is_superuser: 
        raise PermissionDenied
    art = get_object_or_404(Art, pk=art_id)
    if request.method == "POST":
        art.delete()
    return redirect("main:show_artfolio")

@login_required(login_url="/login/") 
def edit_art(request, art_id):
    if not request.user.has_perm('main.change_art'):
        raise PermissionDenied
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
    nama_query = request.GET.get("nama", "").strip()
    
    context = {
        "name": "Muhammad Raihan Al Qadri Kusumaputra",
        "nama_query": nama_query,
        "form": ProjectForm(), # Ditambahkan untuk modal tambah proyek nanti
    }
    return render(request, "project.html", context)

def get_projects_json(request):
    nama_query = request.GET.get("nama", "").strip()
    # Mengambil data dengan prefetch_related untuk optimasi query
    projects = Project.objects.prefetch_related('starred_by').all()
    if nama_query:
        projects = projects.filter(nama__icontains=nama_query)
    
    # Konstruksi data JSON secara manual
    data = []
    for project in projects:
        starred_users = project.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])
        
        # Mengambil label/display dari choices Tipe
        tipe_display = dict(Project.PROJECT_TYPES).get(project.tipe, project.tipe)
        
        data.append({
            "pk": str(project.id),
            "fields": {
                "nama": project.nama,
                "tipe_display": tipe_display,
                "deskripsi": project.deskripsi,
                "thumbnail": project.thumbnail,
                "link": project.link,
                "skillset": project.skillset,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })
    return JsonResponse(data, safe=False)

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

@login_required(login_url="/login/") 
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

@login_required(login_url="/login/") 
def edit_project(request, project_id):
    if not request.user.has_perm('main.change_project'):
        raise PermissionDenied
    project = get_object_or_404(Project, pk=project_id)
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

@login_required(login_url="/login/")
def toggle_love(request, art_id):
    art = get_object_or_404(Art, pk=art_id)
    if request.method == "POST":
        if request.user in art.loved_by.all():
            art.loved_by.remove(request.user)
        else:
            art.loved_by.add(request.user)
    return redirect("main:show_artfolio")

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

@require_POST
def create_project_ajax(request):
    # Cek hak akses: hanya superuser yang boleh menambah data
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Hanya pemilik portofolio yang dapat menambahkan proyek."},
            status=403,
        )
    
    # Gunakan ProjectForm yang sudah ada untuk memvalidasi input
    form = ProjectForm(request.POST)
    if form.is_valid():
        project = form.save()
        return JsonResponse(
            {"message": "Project berhasil ditambahkan.", "pk": str(project.id)},
            status=201,
        )
    
    # Jika tidak valid, kembalikan daftar error dari form
    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)