from django.utils.html import strip_tags
from rest_framework import serializers
from main.models import Project

class ProjectSerializer(serializers.ModelSerializer):
    tipe_display = serializers.CharField(source="get_tipe_display", read_only=True)
    star_count = serializers.SerializerMethodField()
    is_starred = serializers.SerializerMethodField()
    starred_by_names = serializers.SerializerMethodField()
    
    class Meta:
        model = Project
        fields = [
            "id",
            "nama",
            "tipe",
            "tipe_display",
            "deskripsi",
            "thumbnail",
            "link",
            "skillset",
            "star_count",
            "is_starred",
            "starred_by_names",
        ]
        read_only_fields = ["id", "tipe_display"]
    
    def validate_nama(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Nama project tidak boleh kosong.")
        return value
    
    def validate_deskripsi(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Deskripsi tidak boleh kosong.")
        return value

    def validate_skillset(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Skillset tidak boleh kosong.")
        return value

    def validate_thumbnail(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Path thumbnail tidak boleh kosong.")
        return value

    def get_star_count(self, obj):
        return obj.starred_by.count()
    
    def get_is_starred(self, obj):
        request = self.context.get("request")
        if request is None or not request.user.is_authenticated:
            return False
        return request.user in obj.starred_by.all()
    
    def get_starred_by_names(self, obj):
        return ", ".join(user.username for user in obj.starred_by.all())
    
    