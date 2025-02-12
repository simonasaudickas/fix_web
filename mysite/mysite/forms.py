from django import forms
from django.core.validators import EmailValidator


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100,label='Vardas, Pavardė')
    email = forms.EmailField(validators=[EmailValidator()],label='El.paštas')
    phone = forms.CharField(max_length=15, label='Telefonas')
    subject = forms.CharField(max_length=100, label='Žinutės pavadinimas')
    message = forms.CharField(widget=forms.Textarea, label='Užklausos tekstas')