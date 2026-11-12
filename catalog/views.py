from django.shortcuts import get_object_or_404, redirect, render

from .forms import AuthorForm, BookForm
from .models import Author, Book


def book_list(request):
    books = Book.objects.select_related("author").all()
    return render(request, "catalog/book_list.html", {"books": books})


def book_form(request, pk=None):
    book = get_object_or_404(Book, pk=pk) if pk is not None else None

    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            book = form.save()
            return redirect("author_detail", pk=book.author.pk)
    else:
        form = BookForm(instance=book)

    is_edit = book is not None
    return render(
        request,
        "catalog/book_form.html",
        {
            "form": form,
            "page_title": "Editar livro" if is_edit else "Novo livro",
            "heading": "Atualize os dados<br>do livro." if is_edit else "Uma nova história<br>precisa de um <em>livro.</em>",
            "description": "Ajuste o título, o ano, a disponibilidade e as categorias da obra." if is_edit else "Cadastre o título, escolha o autor, informe o ano e as categorias da obra.",
            "submit_label": "Salvar alterações" if is_edit else "Salvar livro",
            "is_edit": is_edit,
        },
    )


def book_create(request):
    return book_form(request)


def book_edit(request, pk):
    return book_form(request, pk=pk)


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