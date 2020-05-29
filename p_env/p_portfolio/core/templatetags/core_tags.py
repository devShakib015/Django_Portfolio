from django import template
from ..models import *

register = template.Library()

@register.inclusion_tag('testimonial.html')
def testimonial():
    testimonials = Testimonial.objects.all()

    return{'testimonials': testimonials}