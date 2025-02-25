from django import forms
from .models import Book,Author
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit,Layout,Field

class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields=['title','author','publication_date','isbn','publisher']

    def clean_isbn(self):
        isbn=self.cleaned_data.get('isbn')
        if len(isbn)!=13:
            raise forms.ValidationError("ISBN must be 13")
        return isbn

class AuthorForm(forms.ModelForm):
    class Meta:
        model=Author
        fields=['first_name','last_name','birth_date']


    #def __init__(self,*args,**kwargs):
       # super().__init__(*args,**kwargs)
        #self.helper=FormHelper()
        #self.helper.form_method="post"
        #self.helper.layout=Layout(
        #    Field("title",css_class="form-control"),
         #   Field("author",css_class="form-control"),
          #  Field("publication_date",css_class="form-control"),
           # Field("isbn",css_class="form-control"),
            #Field("publisher",css_class="form-control"),
            #Submit("submit","send message",css_class="btn btn-primary"),
        #)