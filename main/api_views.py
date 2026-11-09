from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from main.models import Project, Art
from main.permissions import (
    IsPortfolioOwnerOrReadOnly,
    IsPortfolioOwnerOrEditorOrReadOnly,
)
from main.serializers import ProjectSerializer, ArtSerializer

# =x=x=x=x=x==xx==x=x=x=x=x==x=x=x=x
# API VIEWS UNTUK PROJEK
# =x=x=x=x==x=x=x=x=x=x=x=x==x=x=x=x
@api_view(["GET", "HEAD", "POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrReadOnly])
def project_list(request):
    if request.method in ("GET", "HEAD"):
        projects = Project.objects.prefetch_related("starred_by").order_by("nama", "id")
        # Mendukung query parameter ?nama= (dan fallback ?title=)
        nama = (
            request.query_params.get("nama", "").strip()
            or request.query_params.get("title", "").strip()
        )
        if nama:
            projects = projects.filter(nama__icontains=nama)
        serializer = ProjectSerializer(
            projects, many=True, context={"request": request}
        )
        return Response(serializer.data)
    
    serializer = ProjectSerializer(data=request.data, context={"request": request})
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(["GET", "HEAD", "PUT", "PATCH", "DELETE"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrReadOnly])
def project_detail(request, project_id):
    project = get_object_or_404(
        Project.objects.prefetch_related("starred_by"), pk=project_id
    )
    if request.method in ("GET", "HEAD"):
        serializer = ProjectSerializer(project, context={"request": request})
        return Response(serializer.data)
    if request.method == "DELETE":
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    serializer = ProjectSerializer(
        project,
        data=request.data,
        partial=(request.method == "PATCH"),
        context={"request": request},
    )
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

@api_view(["POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def project_star(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if project.starred_by.filter(pk=request.user.pk).exists():
        project.starred_by.remove(request.user)
    else:
        project.starred_by.add(request.user)
    serializer = ProjectSerializer(project, context={"request": request})
    return Response(serializer.data)

# =x=x=x=x=x==xx==x=x=x=x=x==x=x=x=x
# API VIEWS UNTUK ARTFOLIO
# =x=x=x=x==x=x=x=x=x=x=x=x==x=x=x=x
@api_view(["GET", "HEAD", "POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])
def art_list(request):
    if request.method in ("GET", "HEAD"):
        arts = Art.objects.prefetch_related("loved_by").order_by("nama", "id")
        nama = request.query_params.get("nama", "").strip()
        if nama:
            arts = arts.filter(nama__icontains=nama)
        serializer = ArtSerializer(arts, many=True, context={"request": request})
        return Response(serializer.data)

    serializer = ArtSerializer(data=request.data, context={"request": request})
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "HEAD", "PUT", "PATCH", "DELETE"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])
def art_detail(request, art_id):
    art = get_object_or_404(Art.objects.prefetch_related("loved_by"), pk=art_id)
    if request.method in ("GET", "HEAD"):
        serializer = ArtSerializer(art, context={"request": request})
        return Response(serializer.data)

    if request.method == "DELETE":
        art.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    serializer = ArtSerializer(
        art,
        data=request.data,
        partial=(request.method == "PATCH"),
        context={"request": request},
    )
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(["POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def art_love(request, art_id):
    art = get_object_or_404(Art, pk=art_id)
    if art.loved_by.filter(pk=request.user.pk).exists():
        art.loved_by.remove(request.user)
    else:
        art.loved_by.add(request.user)
    serializer = ArtSerializer(art, context={"request": request})
    return Response(serializer.data)