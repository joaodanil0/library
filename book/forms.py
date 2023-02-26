from django import forms
from book.models import Book

class RegisterBook(forms.ModelForm):
    class Meta:
        model = Book
        fields =  ("name","author", "co_author", "register_date", "borrowed", "category", "user")
    
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        self.fields["user"].widget = forms.HiddenInput()
