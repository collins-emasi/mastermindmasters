from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import ContactForm
from .models import Pillars, VisionMissionAbout


def home(request):
    context = {
        'title': "Home",
        "about": VisionMissionAbout.objects.filter(title='about').first(),
        "pillars": Pillars.objects.all(),
    }
    return render(request, 'home/index.html', context)


def about(request):
    context = {
        "title": "About Us",
        "about": VisionMissionAbout.objects.filter(title='about').first(),
        "mission": VisionMissionAbout.objects.filter(title='mission').first(),
        "vision": VisionMissionAbout.objects.filter(title='vision').first(),
        "pillars": Pillars.objects.all(),
    }
    return render(request, 'home/about.html', context)


def contact(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            subject = form.cleaned_data.get('subject')
            message = form.cleaned_data.get('message')

            send_mail(
                subject,
                message + "\n\n" + "Regards\n" + name + "\n" + email,
                'emasicollins@gmail.com',
                ['emasicollins@gmail.com']
            )
            messages.success(request, f"Thank you {name} for your email, We'll get back to you as soon as possible!")
    else:
        if request.user.is_authenticated:
            data = {
                'name': request.user.username,
                'email': request.user.email,
            }
            form = ContactForm(data)

    context = {
        "title": "Contact us",
        "form": form,
    }
    return render(request, 'home/contact.html', context)
