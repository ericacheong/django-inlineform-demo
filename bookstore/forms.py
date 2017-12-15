from django.forms import ModelForm
from bookstore.models import Author, Book

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
