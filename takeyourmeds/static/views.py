from django.shortcuts import render, redirect

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
