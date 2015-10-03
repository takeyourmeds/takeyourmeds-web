from django.shortcuts import render

def index(request):
    return render(request, 'static/index.html', {
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
