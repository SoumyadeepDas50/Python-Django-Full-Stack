from django.db import models
import barcode
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File
#from asyncore import write
from barcode import Code39

class Genre(models.Model):
    name=models.CharField(max_length=200,
                help_text="Enter a book genre (e.g. Science, Fiction, Language)")
    def __str__(self):
        return self.name
    
class Language(models.Model):
    name=models.CharField(max_length=200,
                help_text="Enter the books natural language (e.g. English, Hindi, Bengali)")
    def __str__(self):
        return self.name
    
class Book(models.Model):
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=100)
    summary=models.TextField(max_length=1000)
    isbn=models.CharField('ISBN',max_length=13)
    genre=models.ManyToManyField(Genre)
    language=models.ForeignKey('Language',on_delete=models.SET_NULL,null=True)
    pic=models.ImageField(blank=True,null=True,upload_to='book_image')
    barcode=models.ImageField(blank=True,null=True,upload_to='book_image')

    def __str__(self):
        return self.title
    
    def save(self,*args,**kwargs):
        CODE_39=barcode.get_barcode_class('Code39')
        code=CODE_39('isbn',writer=ImageWriter())
        buffer=BytesIO()
        code.write(buffer)
        self.barcode.save('isbn.png',File(buffer),save=False)
        return super().save(*args,**kwargs)

