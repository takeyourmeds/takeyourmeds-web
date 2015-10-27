from django import forms

from .models import Reminder

class CreateForm(forms.ModelForm):
    frequency = forms.ChoiceField(
        choices=[(x, x) for x in range(1, 4 + 1)],
    )

    message_type = forms.ChoiceField(
        choices=[
            ('voice', u"Voice"),
            ('text', u"Text"),
        ],
        default='voice',
    )

    class Meta:
        model = Reminder
        fields = (
            'telnumber',
        )

    def save(self, user):
        instance = super(CreateForm, self).save(commit=False)
        instance.user = user
        instance.save()

        return instance
