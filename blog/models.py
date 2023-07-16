from django.db import models
from django.conf import settings

from django.template.defaultfilters import escape
from django.urls import reverse
from users.models import User

NULLABLE = {'blank': True, 'null': True}

class Post(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок')
    content = models.CharField(max_length=500, verbose_name='содержание')
    image = models.ImageField(upload_to='blog_image/', **NULLABLE, verbose_name='изображение')
    data_create = models.DateField(auto_now_add=True, verbose_name='дата создания')
    data_update = models.DateField(auto_now=True, verbose_name='дата редактирования')

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title



class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='автор')
    content = models.CharField(max_length=200, verbose_name='комментарий')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='пост')
    data_create = models.DateField(auto_now_add=True, verbose_name='дата создания')
    data_update = models.DateField(auto_now=True, verbose_name='дата редактирования')

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.author

