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

@register.inclusion_tag('career_tag.html')
def career_tag(count=3):
    careers = Career.objects.order_by('-id')[0:3]

    return{'careers': careers}

@register.inclusion_tag('map_tag.html')
def map_tag():
    maps = Map.objects.all()

    return{'maps': maps}

@register.inclusion_tag('about_tag.html')
def about_tag():
    profiles = AboutMe.objects.all()

    return{'profiles': profiles}

@register.inclusion_tag('about_description_tag.html')
def about_description_tag():
    profiles = AboutMe.objects.all()

    return{'profiles': profiles}