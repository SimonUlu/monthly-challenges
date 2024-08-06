# Define blueprints / models in models.py of apps



### See docs for different field types

- https://docs.djangoproject.com/en/5.0/topics/db/models/#field-types

f.e.

```sh
class Book(models.Model):
    # it will automatically create an id field with autoincrementing number
    title = models.CharField(max_length=50)
    rating = models.IntegerField()
```

- from scratch django creates the table with a field id that is autoincrementing

## After creating the models run migrations which will create new migrations under migrations folder

```sh
python manage.py makemigrations
```

## Run all migrations that have not been executed yet

- this will also run migrations that are part of the base application

```sh
python manage.py migrate
```