from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def view(request):
    reminders = request.user.reminders.order_by('-pk')

    return render(request, 'dashboard/view.html', {
        'reminders': reminders,
    })
