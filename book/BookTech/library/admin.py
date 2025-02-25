from django.contrib import admin

from .models import Book,Publisher,Author

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publisher)
