from django import template

register = template.Library()


@register.filter  # 过滤器格式{{data|fliter_tag:X}}  只能传两个参数  能够在逻辑判断中使用
def multi_fliter(x, y):
    return x*y


@register.simple_tag  # 自定义标签{%     %}     能传多个参数   不能再逻辑判断中使用
def multi_tag(x, y):
    return x*y