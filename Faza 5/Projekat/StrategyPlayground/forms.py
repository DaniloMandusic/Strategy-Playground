from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password

from .models import Korisnik

class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = Korisnik
        fields = ['ime', 'prezime', 'email', 'password1', 'password2']
        placeholder_fields = {
            'ime': 'Ime',
            'prezime':'Prezime',
            'email': 'Email',
            'password1': 'Sifra',
            'password2':'Potvrda sifre',
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Sifre se ne podudaraju!")
        return password2
    def save(self, commit=True):
        korisnik= super(UserRegistrationForm, self).save(commit=False)
        korisnik.email = self.cleaned_data['email']
        password = self.cleaned_data['password1']
        korisnik.password= make_password(password)
        if commit:
            korisnik.save()

        return korisnik



class LoginForm(forms.Form):
    email = forms.EmailField(label='email')
    password = forms.CharField(label='password', widget=forms.PasswordInput)


class UpdateForm(forms.Form):
    ime = forms.CharField(label='ime')
    prezime = forms.CharField(label='prezime')



