## Foreign Key Relation

```sh
class Author(models.Model):
    fn = models.CharField(max_length=100)
    ln = models.CharField(max_length=100)

class Book(models.Model):
    ...
    author = models.ForeignKey(Author, on_delete=models.CASCADE) ## Cascade = if author is deleted all related books are also deleted
    ...
```

- cascade: if author is deleted all related books are also deleted
- protect:
- set null: