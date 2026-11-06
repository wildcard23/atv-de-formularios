from django.shortcuts import get_object_or_404, redirect, render

from .forms import AuthorForm, BookForm
from .models import Author, Book


def book_list(request):
    books = Book.objects.select_related("author").all()
    return render(request, "catalog/book_list.html", {"books": books})


def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return redirect("book_detail", pk=book.pk)
    else:
        form = BookForm()

    return render(
        request,
        "catalog/book_form.html",
        {
            "form": form,
            "page_title": "Novo livro",
            "heading": "Uma nova história<br>precisa de um <em>livro.</em>",
            "description": "Cadastre o título e escolha o autor que vai dar vida à obra.",
            "submit_label": "Salvar livro",
            "is_edit": False,
        },
    )


def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book_detail", pk=book.pk)
    else:
        form = BookForm(instance=book)

    return render(
        request,
        "catalog/book_form.html",
        {
            "form": form,
            "page_title": "Editar livro",
            "heading": "Atualize os dados<br>do livro.",
            "description": "Ajuste o título ou troque o autor da obra.",
            "submit_label": "Salvar alterações",
            "is_edit": True,
        },
    )


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        book.delete()
        return redirect("book_list")

    return redirect("book_detail", pk=book.pk)


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, "catalog/book_detail.html", {"book": book})


def author_create(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save()
            return redirect("author_detail", pk=author.pk)
    else:
        form = AuthorForm()

    return render(
        request,
        "catalog/author_form.html",
        {
            "form": form,
            "page_title": "Novo autor",
            "submit_label": "Salvar autor",
            "heading": "Todo livro<br>começa com <em>alguém.</em>",
            "description": "Registre uma nova voz no nosso acervo. Você pode completar a nacionalidade depois.",
            "is_edit": False,
        },
    )


def author_edit(request, pk):
    author = get_object_or_404(Author, pk=pk)

    if request.method == "POST":
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect("author_detail", pk=author.pk)
    else:
        form = AuthorForm(instance=author)

    return render(
        request,
        "catalog/author_form.html",
        {
            "form": form,
            "page_title": "Editar autor",
            "submit_label": "Salvar alterações",
            "heading": "Atualize os dados<br>do autor.",
            "description": "Ajuste o nome ou a nacionalidade do autor no acervo.",
            "is_edit": True,
            "author": author,
        },
    )


def author_delete(request, pk):
    author = get_object_or_404(Author, pk=pk)

    if request.method == "POST":
        author.delete()
        return redirect("book_list")

    return redirect("author_detail", pk=author.pk)


def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, "catalog/author_detail.html", {"author": author})