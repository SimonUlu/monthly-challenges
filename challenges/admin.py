from django.contrib import admin

from .models import Book, Author, Address

class BookAdmin(admin.ModelAdmin):
    readonly_fields = ('author', 'slug')
    list_filter = ("rating", )
    

admin.site.register(Book, BookAdmin)

admin.site.register(Author)

admin.site.register(Address)

# Register your models here.
