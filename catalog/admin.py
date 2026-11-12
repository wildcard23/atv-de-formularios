from django.contrib import admin

from .models import Author, Book, Category


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "nationality")
    search_fields = ("name", "nationality")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "year", "available")
    list_filter = ("available", "author", "categories")
    search_fields = ("title", "author__name")
    filter_horizontal = ("categories",)
