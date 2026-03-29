from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "publication_status", "views_counter")
    list_filter = ("publication_status",)
    search_fields = ("title", "content")
