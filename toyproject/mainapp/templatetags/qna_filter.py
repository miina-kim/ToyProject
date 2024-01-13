import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter # 템플릿에서 아래 함수를 필터로 사용 가능
def sub(value, arg):
    return value - arg

@register.filter
def mark(value):
    extensions = ["nl2br", "fenced_code"]
    return mark_safe(markdown.markdown(value, extensions=extensions))