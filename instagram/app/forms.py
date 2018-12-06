from django.contrib.auth.forms import User
from django.forms import ModelForm, PasswordInput, CharField


class UserForm(ModelForm):
    password = CharField(widget=PasswordInput)
    password_confirm = CharField(widget=PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
