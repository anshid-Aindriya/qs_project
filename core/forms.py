from django import forms
from .models import Contact,Email




class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'qualification', 'question']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'}),
            'qualification': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your qualification'}),
            'question': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your question', 'rows': 4}),
        }

class EmailForm(forms.ModelForm):  # Correct model reference
    class Meta:
        model = Email  # Updated to reference correct model
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
        }