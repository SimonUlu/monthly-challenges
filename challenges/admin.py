from django.contrib import admin

from .models import Book, Author, Address, Country

class BookAdmin(admin.ModelAdmin):
    readonly_fields = ('author', 'slug')
    list_filter = ("rating", )

# Register your models here.    

admin.site.register(Book, BookAdmin)

admin.site.register(Author)

admin.site.register(Address)

admin.site.register(Country)


