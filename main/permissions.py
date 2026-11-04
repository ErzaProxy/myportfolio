from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsPortfolioOwnerOrReadOnly(BasePermission):
    message = "Hanya pemilik portofolio yang dapat mengelola project."
    
    def has_permission(self, request, view):
        return(
            request.method in SAFE_METHODS
            or bool(request.user and request.user.is_superuser)
        )
        
class IsPortfolioOwnerOrEditorOrReadOnly(BasePermission):
    message = "Hanya pemilik portofolio atau Editor yang dapat mengubah data ini"
    
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if not request.user or not request.user.is_authenticated:
            return False
        if request.user.is_superuser:
            return True
        return (
            request.method in ("PUT", "PATCH")
            and (
                request.user.groups.filter(name="Editor").exists()
                or request.user.has_perm("main.change_art")
                or request.user.has_perm("main.change_project")
            )
        )