from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from blog.models import Post, Category


def index(request):
    template = 'blog/index.html'
    post_list = Post.objects.filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now()
    ).order_by()[:5]
    context = {
        'post_list': post_list,
    }
    return render(request, template, context)


def post_detail(request, id):
    template = 'blog/detail.html'
    post_list = get_object_or_404(Post.objects.filter(
            pub_date__lte=timezone.now(),
            is_published=True,
            category__is_published=True
    ),
        pk=id
    )
    context = {'post': post_list}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(Category,
                                 slug=category_slug,
                                 is_published=True
                                 )
    post_list = Post.objects.filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category=category
    )
    context = {
        'category': category,
        'post_list': post_list}
    return render(request, template, context)
