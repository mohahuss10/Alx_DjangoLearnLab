from .models import Author, Book, Library, Librarian

def run_queries():
    # Query all books by a specific author
    try:
        author_name = "J.K. Rowling"
        author = Author.objects.get(name=author_name)
        books_by_author = Book.objects.filter(author=author)
        print(f"Books by {author_name}:", [book.title for book in books_by_author])
    except Author.DoesNotExist:
        print("No author named J.K. Rowling found.")

    # List all books in a library
    try:
        library_name = "Central Library"
        library = Library.objects.get(name=library_name)
        books_in_library = library.books.all()
        print(f"Books in {library_name}:", [book.title for book in books_in_library])
    except Library.DoesNotExist:
        print("No library named Central Library found.")

    # Retrieve the librarian for a library
    try:
        library_name = "Central Library"
        library = Library.objects.get(name=library_name)
        librarian = library.librarian
        print(f"Librarian of {library_name}:", librarian.name)
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        print("No librarian found for Central Library.")
