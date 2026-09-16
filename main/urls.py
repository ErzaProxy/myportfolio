from django.urls import path

from main.views import show_main, show_experience, show_menu, show_about, show_artfolio, show_project, show_contact, create_project, get_projects_json, delete_project
from .views import index

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("menu/", show_menu, name="show_menu"),
    path("about/", show_about, name="show_about"),
    path("artfolio/", show_artfolio, name="show_artfolio"),
    path("project/", show_project, name="show_project"),
    path("contact/", show_contact, name="show_contact"), 
    path("project/add/", create_project, name="create_project"),
    path("api/project/", get_projects_json, name="get_projects_json"),
    path("project/<uuid:project_id>/delete/",delete_project,name="delete_project"),
]
