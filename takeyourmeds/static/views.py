from django.contrib import messages
from django.shortcuts import render, render_to_response, redirect

from takeyourmeds.utils.decorators import superuser_required

from .forms import ContactForm

def landing(request):
    if request.user.is_authenticated():
        return redirect('dashboard:view')

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

def http500(request):
    # Django does not render this page with a RequestContext
    return render_to_response('500.html')

def http404(request):
    # Django *does* render this page with a RequestContext.
    return render(request, '404.html')

@superuser_required
def admin(request):
    return render(request, 'static/admin.html', {
    })
