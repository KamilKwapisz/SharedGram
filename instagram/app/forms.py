from django.contrib.auth.forms import User
from django.forms import Form, ModelForm, PasswordInput, CharField, TextInput


class UserForm(ModelForm):
    password = CharField(widget=PasswordInput)
    password_confirm = CharField(widget=PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class PostForm(Form):
    name = CharField()
    description = CharField()
    # photo =