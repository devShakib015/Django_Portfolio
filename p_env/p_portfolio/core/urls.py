from . import views
from django.urls import path

urlpatterns = [
    path('videos/', views.videos, name='videos'),
    path('about_me/', views.about, name='about'),
    path('my_career/', views.career, name='career'),
    path('my_service/', views.service, name='service'),
    path('recent_work/', views.recent_work, name='recent_work'),
    path('contact/', views.contact, name='contact'),
    path('other_business/', views.other_business, name='other_business'),
    path('', views.index, name='index')
]
