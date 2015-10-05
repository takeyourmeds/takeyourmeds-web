from django.shortcuts import render, redirect

from takeyourmeds.utils.decorators import superuser_required

def landing(request):
    if request.user.is_authenticated():
        return redirect('reminders:index')

    return render(request, 'static/landing.html', {
    })

def about(request):
    return render(request, 'static/about.html', {
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
