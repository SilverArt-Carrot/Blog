from django.contrib import admin
from .models import Category, Tag, Post


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'created_time', 'modified_time')
    list_filter = ['author', 'category']
    search_fields = ['title']
    fieldsets = [
        ('基本信息', {'fields': ['title', 'tag', 'category', 'author']}),
        ('摘要', {'fields': ['excerpt']}),
        ('图片', {'fields': ['img']}),
        ('内容', {'fields': ['body']}),
    ]


admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
