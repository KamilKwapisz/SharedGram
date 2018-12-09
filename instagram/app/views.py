from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.views.decorators.debug import sensitive_post_parameters
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic import View

from neomodel import db
from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
                          UniqueIdProperty, RelationshipTo, RelationshipFrom, StructuredRel)

from .forms import UserForm


def index(request):
    context = dict(username=request.user.username)
    return render(request, "app/index.html", context)


class FriendRel(StructuredRel):
    met = StringProperty()


class User(StructuredNode):
    name = StringProperty()
    friends = RelationshipTo('User', 'FRIEND', model=FriendRel)


def graphdb_test(request):
    from . import graph_models

    # db.set_connection('bolt://neo4j:neo4j@localhost:7687')
    # config.DATABASE_URL = 'bolt://neo4j:password@localhost:7687'
    bucky = graph_models.User.nodes.get(name='Bucky')
    jim = graph_models.User.nodes.get(name="Jim")
    timmy = graph_models.User(name="Timothy").save()
    fol = jim.following.connect(bucky).save()

    photo = graph_models.Photo.nodes.get(name="sea")
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


class RegisterView(View):
    form_class = UserForm
    template_name = "registration/registration.html"
    success_url = reverse_lazy('index')

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    @method_decorator(sensitive_post_parameters())
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid() and form.cleaned_data['password'] == form.cleaned_data['password_confirm']:
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.email = username
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)
            if user:
                messages.success(self.request, "User {} has been created!".format(username))
                login(self.request, user)
                return redirect('index')
            else:
                messages.error(self.request, "Invalid email or password")

        elif form.data['password'] != form.data['password_confirm']:
            form.add_error('password_confirm', 'Passwords do not match')

        return render(request, self.template_name, {'form': form})


def logout_view(request):
    logout(request)
    return render(request, 'registration/logged_out.html', {})
