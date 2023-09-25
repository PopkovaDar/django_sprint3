from django.contrib import admin

from .models import Category, Location, Post


def get_model_fields(model):
    return model._meta.fields


class Blog(admin.ModelAdmin):
    """Панель администратора"""
    list_editable = ('is_published',)


@admin.register(Category)
class CategoryPost(Blog):
    """Управление катерогиями со страницы админа"""
    list_display = (
        'title',
        'is_published',
        'created_at',
        'slug',
    )


@admin.register(Post)
class PostsPost(Blog):
    """Управление постами со страницы админа"""
    list_display = (
        'title',
        'is_published',
        'created_at',
        'text',
        'pub_date',
        'author',
        'location',
        'category',
    )


@admin.register(Location)
class LocationPost(Blog):
    """Управление местоположением со страницы админа"""
    list_display = (
        'created_at',
        'is_published',
        'name',
    )
