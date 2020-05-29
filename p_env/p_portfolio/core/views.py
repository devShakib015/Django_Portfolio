from django.shortcuts import render
from .models import *
from .forms import ContactForm


# Create your views here.
def videos(request):
    videos = Video.objects.order_by('-id')

    context = {
        'videos': videos
    }
    return render(request, 'videos.html', context)

def about(request):
    profiles = AboutMe.objects.all()
    hobbies = Hobby.objects.all()

    context = {
        'profiles': profiles,
        'hobbies': hobbies
    }

    return render(request, 'about.html', context)

def career(request):
    careers = Career.objects.all()

    context = {
        'careers': careers
    }

    return render(request, 'career.html', context)

def service(request):
    services = Service.objects.all()

    context = {
        'services': services
    }

    return render(request, 'service.html', context)

def recent_work(request):
    r_w = RecentWorks.objects.all()

    context = {
        'r_w': r_w
    }

    return render(request, 'recent_works.html', context)

def contact(request):
    new_message = None
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            new_message = form.save(commit=False)
            new_message.save()
    else:
        form = ContactForm()
    
    context = {
        'form': form, 
        'new_message': new_message
    }

    return render(request, 'contact.html', context)

def other_business(request):
    businesses = OtherBusiness.objects.all()

    context = {
        'businesses': businesses
    }

    return render(request, 'other_business.html', context)

def index(request):
    return render(request, 'index.html')