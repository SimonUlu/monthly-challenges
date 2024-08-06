# Define blueprints / models in models.py of apps



### See docs for different field types

- https://docs.djangoproject.com/en/5.0/topics/db/models/#field-types

f.e.

```sh
class Book(models.Model):
    # it will automatically create an id field with autoincrementing number
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.CharField(null=True, max_length=255)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False)
```

- from scratch django creates the table with a field id that is auto incrementing
- if you add new fields after already creating the model than you can just add stuff like null or default values and you can run migrations again

## Create helper methods for business logic


- presentation if you print out an object

```sh
def __str__(self):
        return f"{self.title} ({self.rating})"
```

- create url

```sh
def get_absolute_url(self):
    return reverse("book-detail", args=[self.slug]) 
```

- overwrite save (but make sure the built in will also get called)

```sh
from django.utils.text import slugify

def save(self, *args, **kwargs):
    self.slug = slugify(self.title)
    super().save(*args, **kwargs)


```

## After creating the models run migrations which will create new migrations under migrations folder

```sh
python manage.py makemigrations
```

## Run all migrations that have not been executed yet

- this will also run migrations that are part of the base application

```sh
python manage.py migrate
```

- if you just add a method than you dont have to run this again

## Save new entry to database

- this will create a new entry, and if the one already exists than it will update (this equals to update/create in sql)

```sh
book = Book(title=, rating=)
book.save()
```

- use create() instead of save() if you don't instantiate an item (skip one step)

```sh
Book.objects.create(title="Harry Potter 2", rating=5, author="J.K. Rowling", is_bestselling=True)
```

## Fetching data

-use django built in methods

- get all data
```sh
Book.objects.all()
```

## Deleting data

```sh
book.delete()
```

## Get instance that fulfils certain condition

- filter objects very easily 
- only works when filter is unique (otherwise it will throw an error)
```sh
Book.objects.get(id=2)
```

- this method will also work when filtering if there are multiple (when retrieving a list)

```sh
Book.objects.filter(is_bestselling=False)
```

-> look up different filter under: https://docs.djangoproject.com/en/5.0/topics/db/queries/

## Or - Conditions

```sh
from django.db.models import Q

Book.objects.filter(Q(rating_lt=3) | Q(is_bestselling=True))
```

## Query Performance

When you filter than the code will only touch the database when you print or finally get out 

- when f.e. printing django caches the results

- best practice = structure your code that it can reuse cached results

Bad practice:

```sh
print(Book.objects.filter(rating__gt=3))
```

Good Practice (store queries in variables):

```sh
good_books = Book.objects.filter(rating__gt=3)
print(good_books)
```

## Blank vs null

Zusammengefasst: blank bezieht sich auf die Validierung in Formularen und null auf die Speicherung in der Datenbank.

## Bulk operations

You can delete multiple model instances (i.e. database records) at once: https://docs.djangoproject.com/en/3.1/topics/db/queries/#deleting-objects

You can update multiple model instances (i.e. database records) at once: https://docs.djangoproject.com/en/3.0/ref/models/querysets/#bulk-update

You can create multiple model instances (i.e. database records) at once: https://docs.djangoproject.com/en/3.0/ref/models/querysets/#bulk-create


## Preparing data for displaying in templates or returning in views functions


## Aggregation function

These are one of the most important aggregate function for more visit docs

```sh
from django.db.models import Avg, Max, Min

avg_rating = books.aggregate(Avg("rating")) ## -> this will be new col rating__avg
```

## Order and sort functions

-- does ordering on the database level and not with python

```sh
## asc
books = Book.objects.all().order_by("title")

## desc
books = Book.objects.all().order_by("title")
```