# Generated by Django 4.2.3 on 2023-07-14 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200, verbose_name='комментарий')),
                ('data_create', models.DateField(auto_now_add=True, verbose_name='дата создания')),
                ('data_update', models.DateField(auto_now=True, verbose_name='дата редактирования')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='заголовок')),
                ('content', models.CharField(max_length=500, verbose_name='содержание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog_image/', verbose_name='изображение')),
                ('data_create', models.DateField(auto_now_add=True, verbose_name='дата создания')),
                ('data_update', models.DateField(auto_now=True, verbose_name='дата редактирования')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
            },
        ),
    ]
