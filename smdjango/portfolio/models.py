from tabnanny import verbose
from django.db import models
from datetime import date
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    """Категории"""
    name = models.CharField("Категория", max_length=150)
    description = models.TextField("Описание")
    # url = models.SlugField(max_length=160, unique=True, null=True)
    сreated = models.DateTimeField('Дата создания', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Projects(models.Model):
    """Проект"""
    name = models.CharField('Название', max_length=250)
    description = models.TextField('Описание')
    client = models.CharField('Заказчик', max_length=250)
    spec = models.CharField('Должность', max_length=250)
    period = models.TextField('Период')
    siteurl = models.TextField('siteurl')
    category = models.ManyToManyField(
        Category, verbose_name="Категория", null=True
    )
    сreated = models.DateTimeField('Дата создания', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

class ProjectImages(models.Model):
    """Изображения проекта"""
    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="project_images/")
    project = models.ForeignKey(Projects, verbose_name="Проект", on_delete=models.CASCADE, related_name="project_images")
    сreated = models.DateTimeField('Дата создания', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Изображение проекта"
        verbose_name_plural = "Изображения проекта"