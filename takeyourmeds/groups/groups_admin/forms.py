from django import forms

from ..models import Group, AccessToken
from ..groups_billing.plans import PLANS

class AddEditForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = (
            'name',
        )

    def save(self):
        # Updating
        if self.instance.pk:
            return super(AddEditForm, self).save()

        # Creating new group, so use ``create_group``.
        return Group.objects.create_group(
            name=self.cleaned_data['name'],
            stripe_kwargs={
                'plan': PLANS['free'].slug,
            },
        )

class AccessTokenForm(forms.Form):
    num_tokens = forms.IntegerField(min_value=1)

    def save(self, group):
        instances = [
            AccessToken(group=group)
            for _ in range(self.cleaned_data['num_tokens'])
        ]

        return AccessToken.objects.bulk_create(instances)
