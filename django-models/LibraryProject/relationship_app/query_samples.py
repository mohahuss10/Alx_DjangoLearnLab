from .models import Author, Book, Library, Librarian

def run_queries():
    # Query all books by a specific author
    try:
        author = Author.objects.get(name="J.K. Rowling")
        books_by_author = Book.objects.filter(author=author)
        print("Books by J.K. Rowling:", [book.title for book in books_by_author])
    except Author.DoesNotExist:
        print("No author named J.K. Rowling found.")

    # List all books in a library
    try:
        library = Library.objects.get(name="Central Library")
        books_in_library = library.books.all()
        print("Books in Central Library:", [book.title for book in books_in_library])
    except Library.DoesNotExist:
        print("No library named Central Library found.")

    # Retrieve the librarian for a library
    try:
        library = Library.objects.get(name="Central Library")
        librarian = library.librarian
        print("Librarian of Central Library:", librarian.name)
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        print("No librarian found for Central Library.")
