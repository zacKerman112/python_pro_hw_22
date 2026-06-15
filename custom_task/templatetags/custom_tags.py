from django import template

register = template.Library()


@register.filter(name='uppercase_fields')
def uppercase_fields(value):
    return str(value).upper()


@register.simple_tag
def project_greeting(username):
    return f"Welcome to the project, {username}!"