from core.models import BaseModel
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Category(BaseModel):
    """В этой модели описаны категории"""
    title = models.CharField(
        max_length=256,
        verbose_name='Заголовок')
    description = models.TextField(
        verbose_name='Описание')
    slug = models.SlugField(
        unique=True,
        verbose_name='Идентификатор',
        help_text=('Идентификатор страницы для URL; '
                   'разрешены символы латиницы, цифры, '
                   'дефис и подчёркивание.'))

    class Meta:
        verbose_name = 'категория',
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Location(BaseModel):
    """В этой модели описано местоположение"""
    name = models.CharField(
        max_length=256,
        verbose_name='Название места')

    class Meta:
        verbose_name = 'местоположение',
        verbose_name_plural = 'Местоположения',
        ordering = ['name']

    def __str__(self):
        return self.name


class Post(BaseModel):
    """В этой модели описаны посты"""
    title = models.CharField(
        max_length=256,
        verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    pub_date = models.DateTimeField(
        verbose_name='Дата и время публикации',
        help_text='Если установить дату и время в будущем '
                  '— можно делать отложенные публикации.')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор публикации',
        related_name='author_post'
        )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Местоположение',
        related_name='location_post')
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Категория',
        related_name='category_post')

    class Meta:
        verbose_name = 'публикация',
        verbose_name_plural = 'Публикации',
        ordering = ['text']

    def __str__(self):
        return self.title
