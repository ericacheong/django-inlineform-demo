from django.db import models

TITLE_CHOICES = (
        ('MR', 'Mr'),
        ('MRS', 'Mrs'),
        ('MS', 'Ms'),
)

class Author(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=3, choices=TITLE_CHOICES)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    authors = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
