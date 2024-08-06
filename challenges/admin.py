from django.contrib import admin

from .models import Book

class BookAdmin(admin.ModelAdmin):
    readonly_fields = ('author', 'slug')
    list_filter = ("rating", )
    

admin.site.register(Book, BookAdmin)

# Register your models here.
