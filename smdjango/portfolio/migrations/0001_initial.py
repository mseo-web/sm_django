# Generated by Django 4.2 on 2023-04-29 06:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Категория')),
                ('description', models.TextField(verbose_name='Описание')),
                ('сreated', models.DateTimeField(null=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('client', models.CharField(max_length=250, verbose_name='Заказчик')),
                ('spec', models.CharField(max_length=250, verbose_name='Должность')),
                ('period', models.TextField(verbose_name='Период')),
                ('siteurl', models.TextField(verbose_name='siteurl')),
                ('сreated', models.DateTimeField(null=True, verbose_name='Дата создания')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='portfolio.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
            },
        ),
        migrations.CreateModel(
            name='ProjectImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='project_images/', verbose_name='Изображение')),
                ('сreated', models.DateTimeField(null=True, verbose_name='Дата создания')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.projects', verbose_name='Проект')),
            ],
            options={
                'verbose_name': 'Изображение проекта',
                'verbose_name_plural': 'Изображения проекта',
            },
        ),
    ]
