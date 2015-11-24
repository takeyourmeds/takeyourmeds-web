from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from .forms import CreateForm

@login_required
def view(request):
    if request.method == 'POST':
        form = CreateForm(request.user, request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Your reminder has been created.",
            )

            return redirect('dashboard:view')
    else:
        form = CreateForm(request.user)

    return render(request, 'reminders/create/view.html', {
        'form': form,
    })
