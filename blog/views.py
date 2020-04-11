from django.shortcuts import render, get_object_or_404
from pure_pagination import PaginationMixin
from .models import Tag, Category, Post
from django.views.generic import ListView, DetailView
import markdown


# Create your views here.
def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', {'post_list': post_list})


class IndexView(PaginationMixin, ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    paginate_by = 5

    # def get_queryset(self):
    #     return Post.objects.all().order_by('-created_time')


def detail(request, pk):
    post = Post.objects.get(pk=pk)
    post.increase_views()
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                  ])
    return render(request, 'blog/detail.html', {'post': post})


def detail_for_js_md(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.increase_views()
    return render(request, 'blog/detail.html', {'post':post})


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        response = super(PostDetailView, self).get(self, *args, **kwargs)
        self.object.increase_views()
        return response

    def get_object(self, queryset=None):
        post = super().get_object(self)
        post.body = markdown.markdown(post.body,
                                      extensions=[
                                          'markdown.extensions.extra',
                                      ])
        return post


def category(request, pk):
    c = Category.objects.get(pk=pk)
    post_list = Post.objects.filter(category=c)
    return render(request, 'blog/index.html', {'post_list': post_list})


class CategoryView(PaginationMixin, ListView):
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    paginate_by = 5

    def get_queryset(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return Post.objects.filter(category=cate)


def archives(request, year, month):
    post_list = Post.objects.filter(created_time__year=year, created_time__month=month).order_by('-created_time')
    return render(request, 'blog/index.html', {'post_list': post_list})


class ArchivesView(PaginationMixin, ListView):
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.filter(created_time__year=self.kwargs.setdefault('year'),
                                   created_time__month=self.kwargs.setdefault('month'),
                                   ).order_by('created_time')


def tag(request, pk):
    t = Tag.objects.get(pk=pk)
    post_list = Post.objects.filter(tag=t)
    return render(request, 'blog/index.html', {'post_list': post_list})


class TagView(PaginationMixin, ListView):
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    paginate_by = 5

    def get_queryset(self):
        t = get_object_or_404(Tag, pk=self.kwargs.get('pk'))
        return Post.objects.filter(tag=t)
