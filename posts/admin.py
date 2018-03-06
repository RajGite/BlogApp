from django.contrib import admin

# Register your models here.
from .models import Post,UsersCategories

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "category"]
    list_display_links = ["title"]
    list_filter = ["updated", "timestamp"]
    search_fields = ["title", "content", "category"]
    class Meta:
        model = Post
admin.site.register(Post, PostModelAdmin)
admin.site.register(UsersCategories)