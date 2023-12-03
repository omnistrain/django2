from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from authentication.forms import LoginForm, SignupForm
from django.views.generic import View
from django.conf import settings
from django.contrib.auth.decorators import login_required
from . import forms, models


# Create your views here.
@login_required()
def photo_upload(request):
    form = forms.upload_profil_photo_form(instance=request.user)
    if request.method == 'POST':
        form = forms.upload_profil_photo_form(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('welcome')
    else:
        return render(request, 'authentication/photo_upload.html', context={'form': form})


class signup_page(View):
    form_class = SignupForm

    def get(self, request):
        form = self.form_class()
        return render(request, 'authentication/signup.html', context={'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)


class login_page(View):
    template_name = 'authentication/login.html'
    form_class = LoginForm

    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, self.template_name, context={'form': form, 'message': message})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('welcome')
        message = 'Identifiants invalides.'
        return render(request, self.template_name, context={'form': form, 'message': message})


def logout_view(request):
    logout(request)
    return redirect('login')


"""
def login_view(request):
    message_retour = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('welcome')
                #message_retour = f'{user.username} est connecté'
            else:
                message_retour = 'Refus de connection'
    else:
        form = LoginForm()
    return render(request, 'authentication/login.html', context={'form': form, 'message': message_retour})
"""
