from django.conf import settings
from django.contrib import auth, messages
from django.shortcuts import redirect, render

from .forms import LoginForm

def login(request):
    if request.user.is_authenticated():
        return redirect(settings.LOGIN_REDIRECT_URL)

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            auth.login(request, form.cleaned_data['user'])

            return redirect(request.path)

        for x in form.non_field_errors():
            messages.error(request, x)

    else:
        form = LoginForm()

    request.session.set_test_cookie()

    return render(request, 'account/login.html', {
        'form': form,
    })

def logout(request):
    if request.method == 'POST' or not request.user.is_authenticated():
        auth.logout(request)
        return redirect('static:landing')

    return render(request, 'account/logout.html')
