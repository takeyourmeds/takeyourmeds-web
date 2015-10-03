from django.conf import settings
from django.shortcuts import render, redirect

from takeyourmeds.account.utils import login

from .forms import RegistrationForm

def view(request):
    if request.user.is_authenticated():
        return redirect(settings.LOGIN_REDIRECT_URL)

    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect(settings.LOGIN_REDIRECT_URL)

    else:
        form = RegistrationForm()

    return render(request, 'registration/view.html', {
        'form': form,
    })
