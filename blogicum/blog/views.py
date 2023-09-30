from django.conf import settings
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from blog.models import Category, Post


def all_posts():
    """Функция для получения всех постов"""
    posts = Post.objects.select_related(
        'category',
        'author',
        'location').filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now())
    return posts


def index(request):
    template = 'blog/index.html'
    context = {
        'post_list': all_posts()[:settings.NUMBER_OF_POSTS],
    }
    return render(request, template, context)


def post_detail(request, post_id: int):
    template = 'blog/detail.html'
    context = {'post': get_object_or_404(
        all_posts(),
        pk=post_id)}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True)
    context = {
        'category': category,
        'post_list': all_posts().filter(category=category)}
    return render(request, template, context)
