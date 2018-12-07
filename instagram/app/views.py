from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.views.decorators.debug import sensitive_post_parameters
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic import View

from .forms import UserForm


def index(request):
    context = dict(username=request.user.username)
    return render(request, "app/index.html", context)


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
