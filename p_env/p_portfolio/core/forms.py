from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        labels  = {
        'name':'Your name', 
        'email':'Your email', 
        'phone':'Your phone', 
        'service':'Choose the service you wanna talk about', 
        'comment':'Write your message'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'service': forms.Select(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(
                attrs={'class': 'form-control'}),
        }
        fields = ['name', 'email', 'phone', 'service', 'comment']
