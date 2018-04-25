from django.db import models

class Publisher(models.Model):
    # Publisher's name
    name = models.CharField(
        verbose_name="Publisher",
        max_length=50,
        null=True,
        editable=True
        )
    # Publisher's date of establishment
    established = models.DateField(
        verbose_name="Established Date",
        editable=True,
        null=True
        )
    
    def __str__(self):
        return "{0} - {1}".format(
            self.name,
            self.established.year
            )

    
class Author(models.Model):
    # Author's name
    name = models.CharField(
        verbose_name="Name",
        max_length=50,
        editable=True,
        null=True
        )
    # Author's date of birth
    birth_date = models.DateField(
        verbose_name="Birth Date",
        editable=True,
        null=True
        )
    
    def __str__(self):
        return self.name
    
    
class Book(models.Model):
    # Book's name
    name = models.CharField(
        verbose_name="Name",
        max_length=50,
        editable=True,
        null=True
        )
    # Book's publishing date
    publish_date = models.DateField(
        verbose_name="Publish Date",
        editable=True,
        null=True
        )
    # Related fields:
    # Book's authors (M2M)
    authors = models.ManyToManyField(
        verbose_name="Authors",
        to=Author,
        related_name="books"
        )
    # Book's publisher (FK)
    publisher = models.ForeignKey(
        verbose_name="Publisher",
        to=Publisher,
        null=True,
        on_delete=models.SET_NULL
        )

    def __str__(self):
        return self.name