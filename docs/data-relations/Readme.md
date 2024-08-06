## Foreign Key Relation

#### 1. One to many relation

```sh
class Author(models.Model):
    fn = models.CharField(max_length=100)
    ln = models.CharField(max_length=100)

class Book(models.Model):
    ...
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name="books") 
    ## Cascade = if author is deleted all related books are also deleted
    ...
```

- cascade: if author is deleted all related books are also deleted
- protect:
- set null:

#### 2. One to one relation

```sh
class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=60)

class Author(modelsModel):
   address = models.OneToOneField(Address, on_delete=models.CASCADE) 
```


## Query by relations

- inverse relations

```sh
jkr = Author.objects.get(first_name="J.K.")

## if object with connected foreign key is of object type Book
jkr.book_set.all()
```

- with related_names

```sh
jkr.books.all()
```