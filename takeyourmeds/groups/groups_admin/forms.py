from django import forms

from ..models import Group
from ..groups_billing.plans import PLANS

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = (
            'name',
        )

    def save(self):
        # Updating
        if self.instance.pk:
            return super(GroupForm, self).save()

        # Creating new group, so use ``create_group``.
        return Group.objects.create_group(
            name=self.cleaned_data['name'],
            stripe_kwargs={
                'plan': PLANS['free'].slug,
            },
        )
