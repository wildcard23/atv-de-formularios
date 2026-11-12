from datetime import date

from django import forms

from .models import Author, Book, Category


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["name", "nationality"]
        labels = {
            "name": "Nome",
            "nationality": "Nacionalidade",
        }


class BookForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple,
        label="Categorias",
    )

    class Meta:
        model = Book
        fields = ["title", "author", "year", "available", "categories"]
        labels = {
            "title": "Título",
            "author": "Autor",
            "year": "Ano",
            "available": "Disponível",
            "categories": "Categorias",
        }
        widgets = {
            "available": forms.CheckboxInput,
        }

    def clean_title(self):
        title = self.cleaned_data.get("title", "")
        cleaned_title = " ".join(title.split())
        if len(cleaned_title) < 3:
            raise forms.ValidationError(
                "O título ficou com menos de 3 caracteres após remover espaços extras. Corrija o texto e tente novamente."
            )
        return cleaned_title

    def clean_year(self):
        year = self.cleaned_data.get("year")
        if year is not None and year > date.today().year:
            raise forms.ValidationError(
                f"O ano do livro não pode ser posterior ao ano atual ({date.today().year}). Corrija o ano informado."
            )
        return year