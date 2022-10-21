from django.contrib import admin

from .models import News, Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'created_at', 'updated_at', 'is_bublished']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'content']
    list_editable = ['is_bublished']
    list_filter = ['is_bublished', 'category']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    search_fields = ['title']

admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
