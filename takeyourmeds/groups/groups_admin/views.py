from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from takeyourmeds.utils.decorators import superuser_required

from ..models import Group

from .forms import GroupForm

@superuser_required
def index(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Group created.")

            return redirect(request.path)
    else:
        form = GroupForm()

    groups = Group.objects.all()

    return render(request, 'groups/admin/index.html', {
        'form': form,
        'groups': groups,
    })

@superuser_required
def view(request, group_id):
    group = get_object_or_404(Group, pk=group_id)

    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)

        if form.is_valid():
            form.save()
            messages.success(request, "Group updated.")

            return redirect(request.path)
    else:
        form = GroupForm(instance=group)

    return render(request, 'groups/admin/view.html', {
        'form': form,
        'group': group,
    })
