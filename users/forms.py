from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


# from .models import *
#
# class AddPostForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['cat'].empty_label = "Категория не выбрана"
#
#     class Meta:
#         model = Women
#         fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat']
#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-input'}),
#             'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
#         }
#
#     def clean_title(self):
#         title = self.cleaned_data['title']
#         if len(title) > 200:
#             raise ValidationError('Длина превышает 200 символов')
#
#         return title


class RegisterUserForm(UserCreationForm):
    phone = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='password', widget=forms.EmailInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('phone', 'password',)


class LoginUserForm(AuthenticationForm):
    phone = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))