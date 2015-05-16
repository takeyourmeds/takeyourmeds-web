from django.shortcuts import render, redirect


def index(request):
    return render(request, 'index.html')


def send(request):
    if request.method == 'POST':
        return redirect('sent')
    return render(request, 'index.html')


def sent(request):
    return render(request, 'sent.html')
