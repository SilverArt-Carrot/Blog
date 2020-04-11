from django import template
from ..models import Tag, Post, Category
from django.db.models import Count, F

register = template.Library()


@register.inclusion_tag('blog/inclusions/_recent_posts.html', takes_context=True)
def show_recent_posts(context, num=5):
    posts = Post.objects.order_by('-created_time')[:num]
    return {
        'recent_posts': posts,
    }


@register.inclusion_tag('blog/inclusions/_archives.html', takes_context=True)
def show_archives(context):
    return {
        # 'date_list': Post.objects.dates('created_time', 'month', order='DESC'),
        # 'date_list': Post.objects.dates('created_time', 'month', order='DESC')
        'date_list': Post.objects.annotate(posts_num=Count('created_time__month')).dates('created_time', 'month', order='DESC')
        # 'date_list': Post.objects.annotate(posts_num=F('created_time__month')).dates('created_time', 'month', order='DESC'),
    }


@register.inclusion_tag('blog/inclusions/_tags.html', takes_context=True)
def show_tags(context):
    return {
        'tags': Tag.objects.all()
    }


@register.inclusion_tag('blog/inclusions/_categories.html', takes_context=True)
def show_categories(context):
    return {
        'categories': Category.objects.all()
    }


@register.inclusion_tag('blog/inclusions/_info.html', takes_context=True)
def show_info(context):
    return {
        'posts_num': Post.objects.count(),
        'tags_num': Tag.objects.count(),
        'cate_num': Category.objects.count(),
    }
