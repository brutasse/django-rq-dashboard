from django.template import Library

try:  # Django < 1.9
    from django.templates.future import url as url_compat
except ImportError:
    from django.template.defaulttags import url as url_compat


register = Library()


@register.tag
def url(parser, token):
    return url_compat(parser, token)
