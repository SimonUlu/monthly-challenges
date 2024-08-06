## Initial setup 


### 1. Create superuser

```sh
python manage.py createsuperuser
```

### 2. Select some columns as readonly or whatever

```sh
class BookAdmin(admin.ModelAdmin):
    readonly_fields = ('author', 'slug')
```


### 3. Register new models to our admin dashboard

```sh
admin.site.register(Book, BookAdmin)
```

### 4. More Config Options

```sh
class BookAdmin(admin.ModelAdmin):
    readonly_fields = ('author', 'slug')
    list_filter = ("rating", )
```