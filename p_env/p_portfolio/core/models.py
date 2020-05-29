from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.


class Video(models.Model):
    title = models.CharField(max_length=400, default='Add the title of your video...')
    video = models.URLField()

    def __str__(self):
        return self.title
    

class AboutMe(models.Model):
    name = models.CharField(max_length=200)
    birth = models.DateField(auto_now=False, auto_now_add=False)
    short_description = models.CharField(max_length=1000)
    long_description = models.TextField()
    image = models.ImageField(upload_to='about')

    class Meta:
        verbose_name = "About me"
        verbose_name_plural = 'About Me'

    def __str__(self):
        return self.name
    
class Career(models.Model):
    title = models.CharField(max_length=400)
    description = models.TextField()
    image = models.ImageField(upload_to='career')

    class Meta:
        verbose_name = "My career"
        verbose_name_plural = 'My careers'
    
    def __str__(self):
        return self.title

class Service(models.Model):
    title = models.CharField(max_length=400)
    description = models.TextField()
    image = models.ImageField(upload_to='service')

    class Meta:
        verbose_name = "My Service"
        verbose_name_plural = 'My Services'
    
    def __str__(self):
        return self.title
    
class RecentWorks(models.Model):
    title = models.CharField(max_length=400)
    description = models.TextField()
    image = models.ImageField(upload_to='recent_works')

    class Meta:
        verbose_name = "Recent Work"
        verbose_name_plural = 'Recent Works'
    
    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    comment = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = 'Messages'
    
    def __str__(self):
        return self.name

class Hobby(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Hobby"
        verbose_name_plural = 'Hobbies'

    def __str__(self):
        return self.title
    
    
class OtherBusiness(models.Model):
    name = models.CharField(max_length=200)
    short_description = models.CharField(max_length=1000)
    long_description = models.TextField()
    image = models.ImageField(upload_to='about')

    class Meta:
        verbose_name = "Other business"
        verbose_name_plural = 'Other businesses'

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.name
    
    