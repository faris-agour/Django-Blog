from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import EmailForm


def contact(request):
    name = None
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']  # Get email from the form
            user = request.user  # Get the currently logged-in user

            # Check if the entered email matches the user's email
            if user.email == email:
                about = f"{form.cleaned_data['about']} (from {email})"
                message = f"From: {email}\n{name}\n\n{form.cleaned_data['message']}"
                from_email = email  # User's email as sender
                recipient_list = [settings.EMAIL_HOST_USER]  # Your company's email

                send_mail(about, message, from_email, recipient_list)
                return redirect(reverse('contact:success'))  # Redirect to a success page
            else:
                form.add_error('email', 'Please enter your logged-in email.')
    else:
        form = EmailForm()

    return render(request, 'contact.html', {'form': form})


def contact_success(request):
    name = request.GET.get('name')
    return render(request, 'contact_success.html', {'name': name})

# Create your views here.
