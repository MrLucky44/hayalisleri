from django.contrib import admin
from .models import Blog, Category
from django.utils.safestring import mark_safe

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "slug")
    list_editable = ("is_active", )
    search_fields = ("title", "description")
    readonly_fields = ("slug",)
    list_filter = ("is_active", "categories")

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ("slug",)

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)