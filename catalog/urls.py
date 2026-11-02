from django.urls import path

from . import views


urlpatterns = [
    path("livros/", views.book_list, name="book_list"),
    path("autores/novo/", views.author_create, name="author_create"),
    path("autores/<int:pk>/", views.author_detail, name="author_detail"),
]