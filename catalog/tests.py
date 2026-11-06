from django.test import Client, TestCase
from django.urls import reverse

from .forms import AuthorForm, BookForm
from .models import Author, Book


class AuthorFormTests(TestCase):
    def test_author_form_requires_name(self):
        form = AuthorForm(data={"name": "", "nationality": "Brasileira"})

        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors)

    def test_valid_author_form_creates_author(self):
        response = self.client.post(
            reverse("author_create"),
            {"name": "Machado de Assis", "nationality": "Brasileira"},
        )

        self.assertEqual(response.status_code, 302)
        author = Author.objects.get(name="Machado de Assis")
        self.assertEqual(author.nationality, "Brasileira")
        self.assertRedirects(response, reverse("author_detail", kwargs={"pk": author.pk}))

    def test_missing_csrf_token_is_rejected(self):
        client = Client(enforce_csrf_checks=True)

        response = client.post(
            reverse("author_create"),
            {"name": "Clarice Lispector", "nationality": "Brasileira"},
        )

        self.assertEqual(response.status_code, 403)

    def test_author_can_be_edited(self):
        author = Author.objects.create(name="Autor Antigo", nationality="Brasileira")

        response = self.client.post(
            reverse("author_edit", kwargs={"pk": author.pk}),
            {"name": "Autor Atualizado", "nationality": "Japonesa"},
        )

        self.assertEqual(response.status_code, 302)
        author.refresh_from_db()
        self.assertEqual(author.name, "Autor Atualizado")
        self.assertEqual(author.nationality, "Japonesa")

    def test_author_can_be_deleted(self):
        author = Author.objects.create(name="Autor para excluir", nationality="Brasileira")

        response = self.client.post(reverse("author_delete", kwargs={"pk": author.pk}))

        self.assertEqual(response.status_code, 302)
        self.assertFalse(Author.objects.filter(pk=author.pk).exists())


class BookFormTests(TestCase):
    def test_valid_book_form_creates_book(self):
        author = Author.objects.create(name="José Sarria", nationality="Brasileira")

        response = self.client.post(
            reverse("book_create"),
            {"title": "Dom Casmurro", "author": author.pk},
        )

        self.assertEqual(response.status_code, 302)
        book = Book.objects.get(title="Dom Casmurro")
        self.assertEqual(book.author, author)
        self.assertRedirects(response, reverse("book_detail", kwargs={"pk": book.pk}))

    def test_book_form_requires_title(self):
        author = Author.objects.create(name="Autor Teste", nationality="Brasileira")
        form = BookForm(data={"title": "", "author": author.pk})

        self.assertFalse(form.is_valid())
        self.assertIn("title", form.errors)

    def test_book_can_be_edited(self):
        author = Author.objects.create(name="Autor Original", nationality="Brasileira")
        book = Book.objects.create(title="Livro Antigo", author=author)

        response = self.client.post(
            reverse("book_edit", kwargs={"pk": book.pk}),
            {"title": "Livro Atualizado", "author": author.pk},
        )

        self.assertEqual(response.status_code, 302)
        book.refresh_from_db()
        self.assertEqual(book.title, "Livro Atualizado")

    def test_book_can_be_deleted(self):
        author = Author.objects.create(name="Autor de Livro", nationality="Brasileira")
        book = Book.objects.create(title="Livro para excluir", author=author)

        response = self.client.post(reverse("book_delete", kwargs={"pk": book.pk}))

        self.assertEqual(response.status_code, 302)
        self.assertFalse(Book.objects.filter(pk=book.pk).exists())
