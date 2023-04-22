from django.contrib import admin
from posts.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'created', 'modified')
    list_display_links = ('pk','title')

    search_fields = ('title',)
    list_filter = ('created', 'modified')