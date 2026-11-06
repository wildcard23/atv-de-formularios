from django.urls import path

from . import views


urlpatterns = [
    path("", views.book_list, name="home"),
    path("livros/", views.book_list, name="book_list"),
    path("livros/novo/", views.book_create, name="book_create"),
    path("livros/<int:pk>/", views.book_detail, name="book_detail"),
    path("livros/<int:pk>/editar/", views.book_edit, name="book_edit"),
    path("livros/<int:pk>/excluir/", views.book_delete, name="book_delete"),
    path("autores/novo/", views.author_create, name="author_create"),
    path("autores/<int:pk>/editar/", views.author_edit, name="author_edit"),
    path("autores/<int:pk>/excluir/", views.author_delete, name="author_delete"),
    path("autores/<int:pk>/", views.author_detail, name="author_detail"),
]