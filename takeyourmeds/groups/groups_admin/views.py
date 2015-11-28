from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from takeyourmeds.utils.decorators import superuser_required

from ..models import Group

from .forms import AddEditForm, AccessTokenForm

@superuser_required
def index(request):
    if request.method == 'POST':
        form = AddEditForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, "Group created.")

            return redirect('groups:admin:index')
    else:
        form = AddEditForm()

    return render(request, 'groups/admin/index.html', {
        'form': form,
        'groups': Group.objects.all(),
    })

@superuser_required
def view(request, group_id):
    group = get_object_or_404(Group, pk=group_id)

    if request.method == 'POST':
        form = AddEditForm(request.POST, instance=group)

        if form.is_valid():
            form.save()

            messages.success(request, "Group updated.")

            return redirect('groups:admin:index')
    else:
        form = AddEditForm(instance=group)

    access_tokens = group.access_tokens.select_related('user')

    return render(request, 'groups/admin/view.html', {
        'form': form,
        'group': group,
        'access_tokens': access_tokens,
        'access_token_form': AccessTokenForm(initial={'num_tokens': 10})
    })

@require_POST
@superuser_required
def create_access_tokens(request, group_id):
    group = get_object_or_404(Group, pk=group_id)

    form = AccessTokenForm(request.POST)

    if form.is_valid():
        access_tokens = form.save(group)

        messages.success(
            request,
            "%d access token(s) created." % len(access_tokens),
        )
    else:
        messages.error(request, "Please enter a valid number.")

    return redirect('groups:admin:view', group.pk)
