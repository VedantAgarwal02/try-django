from django.shortcuts import render
from django.http import HttpResponse
import json
import os
from .forms import ContactForm

# Create your views here.

def home_view(request, *args, **kwargs):
    print("User: ", request.user)
    return render(request, "home.html", {})
    # return HttpResponse("<H1> Hello World ! </H1>")

def about_view(request):
    # Load resume data from JSON
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    resume_path = os.path.join(base_dir, 'resume.json')
    
    with open(resume_path, 'r') as f:
        resume_data = json.load(f)
    
    context = {
        'resume': resume_data
    }
    
    return render(request, "about.html", context)

def contact_view(request):
    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            form = ContactForm()

    context = {
        'form': form
    }
    return render(request, "contact.html", context)