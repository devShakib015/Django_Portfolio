from django import template
from ..models import *

register = template.Library()

@register.inclusion_tag('testimonial.html')
def testimonial():
    testimonials = Testimonial.objects.all()

    return{'testimonials': testimonials}

@register.inclusion_tag('video_tag.html')
def video_tag(count=3):
    videos = Video.objects.order_by('-id')[0:3]

    return{'videos': videos}

@register.inclusion_tag('service_tag.html')
def service_tag(count=3):
    services = Service.objects.order_by('-id')[0:3]

    return{'services': services}

@register.inclusion_tag('work_tag.html')
def work_tag(count=3):
    works = RecentWorks.objects.order_by('-id')[0:3]

    return{'works': works}