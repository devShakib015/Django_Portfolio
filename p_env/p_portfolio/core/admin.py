from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Video)
class VideoItemAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ['name', 'birth']

@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(RecentWorks)
class RecentWorkAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'service', 'time']
    list_filter = ['service']

@admin.register(Hobby)
class HobbyAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(OtherBusiness)
class OtherBusinessAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Map)
class MapAdmin(admin.ModelAdmin):
    list_display = ['link']