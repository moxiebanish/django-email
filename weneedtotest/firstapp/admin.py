from django.contrib import admin
from .models import TemporaryPassword, Media
from django.utils.safestring import mark_safe

@admin.register(TemporaryPassword)
class TemporaryPasswordAdmin(admin.ModelAdmin):
    list_display = ('owner', 'temporary_password')

    def owner(self, obj):
        return obj.user.username


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('view', 'name')

    def view(self, obj):

        return mark_safe(f"<img src='{obj.image.url}' height=50px width=50px>")
