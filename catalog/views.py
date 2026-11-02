from django.shortcuts import get_object_or_404, redirect, render

from .forms import AuthorForm
from .models import Author, Book


def book_list(request):
    books = Book.objects.select_related("author").all()
    return render(request, "catalog/book_list.html", {"books": books})


def author_create(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save()
            return redirect("author_detail", pk=author.pk)
    else:
        form = AuthorForm()

    return render(request, "catalog/author_form.html", {"form": form})


def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, "catalog/author_detail.html", {"author": author})