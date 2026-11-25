from django.urls import path
from rest_framework.authtoken import views as authtoken_views
from main import api_views

app_name = "api"

urlpatterns = [
    # Auth Token untuk Flutter
    path("auth/token/", authtoken_views.obtain_auth_token, name="api_token_auth"),
    path("auth/logout/", api_views.api_logout, name="api_logout"),

    # Endpoint Projects
    path("projects/", api_views.project_list, name="project-list"),
    path("projects/<uuid:project_id>/", api_views.project_detail, name="project-detail"),
    path("projects/<uuid:project_id>/star/", api_views.project_star, name="project-star"),

    # Endpoint Artfolio
    path("arts/", api_views.art_list, name="art-list"),
    path("arts/<uuid:art_id>/", api_views.art_detail, name="art-detail"),
    path("arts/<uuid:art_id>/love/", api_views.art_love, name="art-love"),
]