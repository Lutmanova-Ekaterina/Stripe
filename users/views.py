from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from users.models import User

from users.forms import RegisterUserForm, LoginUserForm




def contact(request):
    return HttpResponse("Обратная связь")


def pageNotFound(request):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


class RegisterUserView(CreateView):
    template_name = 'users/register.html'
    model = User
    form_class = RegisterUserForm

    def index(request):
        return render(request, 'users/register.html')

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save()
        return super().form_valid(form)


class LoginUserView(LoginView):
    template_name = 'users/login.html'
    form_class = LoginUserForm

    def index(request):
        return render(request, 'users/login.html')


def logout_user(request):
    logout(request)
    return redirect('login')
