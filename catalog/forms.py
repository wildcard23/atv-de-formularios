from django import forms

from .models import Author, Book


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["name", "nationality"]
        labels = {
            "name": "Nome",
            "nationality": "Nacionalidade",
        }


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author"]
        labels = {
            "title": "Título",
            "author": "Autor",
        }