from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import ContactForm
from .forms import EmailForm
# Create your views here.


def home(request):
    return render(request, 'core/public_acces/home.html')


def contact_view(request):
    contact_form = ContactForm(request.POST or None)
    email_form = EmailForm()  # Ensure email_form is always passed

    if request.method == "POST" and "contact_submit" in request.POST:
        if contact_form.is_valid():
            contact_form.save()
            return redirect("core:home")  # Redirect to homepage after submission
        else:
            print(contact_form.errors)  # Debugging: Print form errors

    return render(request, "core/public_acces/home.html", {"contact_form": contact_form, "email_form": email_form})

def email_view(request):
    email_form = EmailForm(request.POST or None)
    contact_form = ContactForm()  # Ensure contact_form is always passed

    if request.method == "POST" and "email_submit" in request.POST:
        if email_form.is_valid():
            email_form.save()
            return redirect("core:home")
        else:
            print(email_form.errors)  # Debugging: Print form errors

    return render(request, "core/public_acces/home.html", {"contact_form": contact_form, "email_form": email_form})