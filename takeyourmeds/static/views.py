from django.shortcuts import render

def index(request):
    return render(request, 'static/index.html', {
    })

def about(request):
    return render(request, 'static/about.html', {
    })

def terms_and_conditions(request):
    return render(request, 'static/terms_and_conditions.html', {
    })

def privacy_policy(request):
    return render(request, 'static/privacy_policy.html', {
    })
