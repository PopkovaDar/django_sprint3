from django.conf import settings
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from blog.models import Category, Post


def index(request):
    template = 'blog/index.html'
    post_list = Post.objects.select_related('category').filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now()
    )[:settings.NUMBER_OF_POSTS]
    context = {
        'post_list': post_list,
    }
    return render(request, template, context)


def post_detail(request, post_id: int):
    template = 'blog/detail.html'
    post_list = get_object_or_404(
        Post,
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True,
        pk=post_id)
    context = {'post': post_list}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True)
    post_list = Post.objects.filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category=category
    )
    context = {
        'category': category,
        'post_list': post_list}
    return render(request, template, context)


def all_posts(request):
    '''Функция для получения всех постов'''
    template = 'blog/all_posts.html'
    post_list = Post.objects.all()
    context = {
        'post_list': post_list,
    }
    return render(request, template, context)
