from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.views.decorators.debug import sensitive_post_parameters
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic import View

from .forms import UserForm
from .graph_models import *


def index(request):
    context = dict(username=request.user.username)
    return render(request, "app/index.html", context)


def graphdb_test(request):
    """Just playground"""
    # db.set_connection('bolt://neo4j:neo4j@localhost:7687')
    # config.DATABASE_URL = 'bolt://neo4j:password@localhost:7687'
    bucky = User.nodes.get(name='Bucky')
    jim = User.nodes.get(name="Jim")
    timmy = User(name="Timothy").save()
    fol = jim.following.connect(bucky).save()

    photo = Photo.nodes.get(name="sea")
    # photo.liked_by.connect(bucky).save()
    print(photo.likes_number)
    # rel = jim.friends.connect(User(name="Tim").save(), {'met': 'Warsaw'})
    # rel = jim.friends.connect(User(name="Bucky").save(), {'met': 'Warsaw'})
    # rel = jim.friends.connect(User(name="drWilk").save(), {'met': 'Warsaw'})
    # # print(rel.start_node().name)  # jim
    # # print(rel.end_node().name)  # bob
    # rel.met = "Amsterdam"
    # rel.save()
    return render(request, "app/index.html", {})


class PostCreateForm(View):
    form_class = UserForm
    template_name = "app/post_create.html"

    def get(self, request):
        """Displaying blank form"""
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            username = self.request.user.username
            user = User.nodes.get(name=username)
            photo = Photo.nodes.get(name="sea")  # temporarily
            Post(
                name=name,
                description=description,
                photo=photo,
                author=user
            ).save()
            messages.success(self.request, "Post has been added!")
            return redirect('index')
        else:
            messages.error(self.request, "Invalid form")

        return render(request, self.template_name, {'form': form})


def create_and_authenticate_user(form):
    """
    Creates user object with cleaned data from django form.
    Then user is authenticated with credentials provided in form
    :param form: filled Django form instance
    :return: user object if everything is correct, None otherwise
    """
    user_object = form.save(commit=False)
    username = form.cleaned_data['username']
    password = form.cleaned_data['password']
    user_object.email = username
    user_object.set_password(password)
    user_object.save()
    user = authenticate(username=username, password=password)
    return user


def are_passwords_matching(form) -> bool:
    """
    Checks whether password field and password confirm field have same value
    :param form: filled Django form instance
    :return: true if fields have same value, false otherwise
    """
    return form.cleaned_data['password'] == form.cleaned_data['password_confirm']


class RegisterView(View):
    form_class = UserForm
    template_name = "registration/registration.html"

    def get(self, request):
        """Displaying blank form"""
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    @method_decorator(sensitive_post_parameters())
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            if are_passwords_matching(form):
                user = create_and_authenticate_user(form)
                if user is not None:
                    User(name=user.username).save()
                    messages.success(self.request, "User has been created!")
                    login(self.request, user)
                    return redirect('index')
                else:
                    messages.error(self.request, "Invalid email or password")
            else:
                form.add_error('password_confirm', 'Passwords do not match')

        return render(request, self.template_name, {'form': form})


def logout_view(request):
    logout(request)
    return render(request, 'registration/logged_out.html', {})
