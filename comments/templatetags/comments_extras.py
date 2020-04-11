from django import template
from ..models import Reply, Comment

register = template.Library()


@register.inclusion_tag('comments/inclusions/_comment.html', takes_context=True)
def show_comment(context):
    pass


@register.inclusion_tag('comments/inclusions/_comments_list.html', takes_context=True)
def show_comments_list(context):
    pass
