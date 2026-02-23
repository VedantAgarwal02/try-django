from django import forms
from .models import ContactMessage

# Create your forms here.
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'John Doe',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'your@email.com',
            }),
            'subject': forms.TextInput(attrs={
                'placeholder': 'What is this about?',
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Tell us more about your inquiry...',
                'rows': '6',
            }),
        }
        labels = {
            'name': 'Full Name',
            'email': 'Email Address',
            'subject': 'Subject',
            'message': 'Message',
        }