from django import forms

from ..models import Group

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = (
            'name',
        )

    def save(self, created_by=None):
        instance = super(GroupForm, self).save(commit=False)

        if created_by is not None:
            instance.created_by = created_by

        instance.save()

        return instance
