from django.http import Http404
from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.utils.http import base36_to_int
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator

from takeyourmeds.utils.decorators import logout_required

from ..utils import login

from .forms import ForgotPasswordForm, ResetPasswordForm

User = get_user_model()

@logout_required
def view(request):
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Instructions to reset your password have been emailed to you.",
            )

            return redirect(request.path)
    else:
        form = ForgotPasswordForm()

    return render(request, 'account/forgot_password/view.html', {
        'form': form,
    })

@logout_required
def reset(request, uidb36, token):
    try:
        user_id = base36_to_int(uidb36)
    except ValueError:
        raise Http404()

    user = get_object_or_404(User, pk=user_id)

    if not default_token_generator.check_token(user, token):
        raise Http404()

    if request.method == 'POST':
        form = ResetPasswordForm(request.POST)

        if form.is_valid():
            form.save(user)

            login(request, user)

            messages.success(
                request,
                "Your password has been changed successfully.",
            )

            return redirect('account:login')
    else:
        form = ResetPasswordForm()

    return render(request, 'account/forgot_password/reset.html', {
        'form': form,
    })
