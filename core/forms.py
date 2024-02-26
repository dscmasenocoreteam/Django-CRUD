from django import forms
from .models import Contact

class ContactCreationForm(forms.ModelForm):
    class Meta:
        model = Contact
        #fields = ['f_name', 'l_name', 'email', 'phone_number', 'address']
        exclude = ['user']