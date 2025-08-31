from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns shown in admin list
    list_filter = ('publication_year', 'author')            # Filters on the right sidebar
    search_fields = ('title', 'author')                     # Search box for these fields
