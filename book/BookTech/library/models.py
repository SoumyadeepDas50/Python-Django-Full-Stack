from django.db import models
from datetime import date

class Author(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    birth_date=models.DateField()
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    def full_name(self):
        """This function will return the full name of the author"""
        return f"{self.first_name} {self.last_name}"
    
class Publisher(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=225)
    city=models.CharField(max_length=200)
    state_province=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    website=models.URLField(null=True)

    def __str__(self):
        return self.name
    
    def formatte_address(self):
        """Return the full address of the publisher"""
        return f"{self.address},{self.city},{self.state_province},{self.country}"

class Book(models.Model):
    title=models.CharField(max_length=200)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    publication_date=models.DateField()
    isbn=models.CharField(max_length=30)
    genre=models.CharField(max_length=50, default="Unknown") #new field
    publisher=models.ManyToManyField(Publisher)
    description=models.TextField(max_length=500)

    def __str__(self):  
        return self.title
    
    def book_age(self):
        """This function return the book age...!!"""
        today=date.today()
        return today.year- self.publication_date.year
    
    