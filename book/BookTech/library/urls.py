from django.urls import path
from .import views
#from .views import BookListView,BookDetailView

urlpatterns=[
    #This path is for the function view urls
    path('books/',views.book_list,name='book_list'),
    path('book/<int:book_id>/',views.book_detail,name='book_detail'),
    path('author/<str:author_id>/books',views.books_by_author,name='books_by_author'),
    path('books/add',views.add_book,name='add_book'),
    path('books/add_with_author/',views.add_book_and_author,name='add_book_and_author'),

    #This path is for the class view urls
    #path("book/",BookListView.as_view(),name="book_list"),
    #path("book//",BookDetailView.as_view(),name="book_detail"),
]
