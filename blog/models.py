from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name


class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name


class Post(models.Model):
    title = models.CharField(verbose_name='标题', max_length=80)
    author = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)
    body = models.TextField(verbose_name='正文')
    category = models.ForeignKey(Category, verbose_name='分类', on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, verbose_name='标签', blank=True)
    img = models.ImageField(verbose_name='图片', default=None)
    excerpt = models.CharField(verbose_name='摘要', max_length=200, blank=True)
    created_time = models.DateTimeField(verbose_name='创建时间', default=timezone.now)
    modified_time = models.DateTimeField(verbose_name='修改时间')
    visits=models.PositiveIntegerField(verbose_name='访问量', default=0, editable=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.modified_time = timezone.now()
        super().save(*args, **kwargs)

    def increase_views(self):
        self.visits += 1
        super().save(update_fields=['visits'])

    class Meta:
        verbose_name = '博文'
        verbose_name_plural = verbose_name
        ordering = ['-created_time']
