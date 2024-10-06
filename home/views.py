# views.py
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.conf import settings
from django.http import HttpResponse
from django.http import JsonResponse
from django.urls import reverse

def home(request):
    return render(request, 'index.html')




def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save form data to the database
            form.save()
            
            # Send email notification
            subject = 'New Contact Form Submission'
            message = f"Name: {form.cleaned_data['name']}\nEmail: {form.cleaned_data['email']}\nMobile Number: {form.cleaned_data['mobile_number']}\nMessage: {form.cleaned_data['message']}"
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [settings.NOTIFICATION_EMAIL]
            send_mail(subject, message, from_email, recipient_list)

            return redirect(reverse('home') + '?submitted=True')
        else:
            form = ContactForm()
            return render(request, 'index.html', {'form': form})



def success_view(request):
    return HttpResponse("Form submission successful!")
