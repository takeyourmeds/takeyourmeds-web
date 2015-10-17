from django.contrib import messages
from django.shortcuts import render, redirect

from takeyourmeds.utils.decorators import superuser_required

from .forms import ContactForm

def landing(request):
    if request.user.is_authenticated():
        return redirect('reminders:index')

    return render(request, 'static/landing.html', {
    })

def about(request):
    return render(request, 'static/about.html', {
    })

def faq(request):
    return render(request, 'static/faq.html', {
    })

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent.")
            return redirect(request.path)
    else:
        form = ContactForm()

    return render(request, 'static/contact.html', {
        'form': form,
    })

def terms(request):
    return render(request, 'static/terms.html', {
    })

def privacy(request):
    return render(request, 'static/privacy.html', {
    })

@superuser_required
def admin(request):
    return render(request, 'static/admin.html', {
    })
