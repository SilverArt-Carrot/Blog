from django.contrib import admin
from .models import Comment, Reply


# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_filter = ['name', ]
    list_display = ['name', 'email', 'url', 'created_time', ]
    fields = ['name', 'email', 'url', 'text', 'post', 'created_time', ]


class ReplyAdmin(admin.ModelAdmin):
    list_filter = ['name', ]
    list_display = ['name', 'email', 'url', 'created_time', ]
    fields = ['name', 'email', 'url', 'text', 'comment', 'created_time', ]


admin.site.register(Reply, ReplyAdmin)
admin.site.register(Comment, CommentAdmin)
