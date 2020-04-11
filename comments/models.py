from django.db import models
from blog.models import Post
from django.utils import timezone


# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=30, verbose_name='发布者')
    email = models.EmailField(verbose_name='邮箱')
    url = models.URLField(verbose_name='网址')
    post = models.ForeignKey(Post, verbose_name='对应文章', on_delete=models.CASCADE)
    text = models.TextField(verbose_name='内容')
    created_time = models.DateTimeField(verbose_name='发布时间', default=timezone.now)

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name
        ordering = ['created_time']

    def __str__(self):
        return '{}: {}'.format(self.name, self.text[:20])


class Reply(models.Model):
    name = models.CharField(max_length=30, verbose_name='发布者')
    email = models.EmailField(verbose_name='邮箱')
    url = models.URLField(verbose_name='网址')
    comment = models.ForeignKey(Post, verbose_name='原评论', on_delete=models.CASCADE)
    text = models.TextField(verbose_name='内容')
    created_time = models.DateTimeField(verbose_name='发布时间', default=timezone.now)

    class Meta:
        verbose_name = '回复'
        verbose_name_plural = verbose_name
        ordering = ['created_time']

    def __str__(self):
        return '{}: {}'.format(self.name, self.text[:20])
