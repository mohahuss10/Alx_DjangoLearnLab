from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book
from .models import Library  


# Function-based view: plain text list of books
def list_books(request):
    books = Book.objects.all()
    output = "\n".join([f"{book.title} by {book.author.name}" for book in books])
    return HttpResponse(output, content_type="text/plain")


# Class-based view: show details for a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"
