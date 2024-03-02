from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']  # shows a list of objects on the page
    list_filter = ['status', 'created', 'publish', 'author']  # filters results for fields included in the attribute
    search_fields = ['title', 'body']  # Search options
    prepopulated_fields = {'slug': ('title',)}  # title written in slug
    raw_id_fields = ['author']  # to select the list automatically.
    date_hierarchy = 'publish'  # navigation by publication dates
    ordering = ['status', 'publish']  # default sorting
