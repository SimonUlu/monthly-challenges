## Foreign Key Relation

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


## Query by relations

- inverse relations

```sh
jkr = Author.objects.get(first_name="J.K.")

## if object with connected foreign key is of object type Book
jkr.book_set.all()
```

- with related_names

```sh

```