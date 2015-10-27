import re

from django import forms

from .models import Reminder

re_telnumber = re.compile(r'^\d{9,14}$')

class CreateForm(forms.ModelForm):
    frequency = forms.ChoiceField(
        choices=[(x, x) for x in range(1, 4 + 1)],
    )

    message_type = forms.ChoiceField(
        choices=[
            ('voice', u"Voice"),
            ('text', u"Text"),
        ],
    )

    class Meta:
        model = Reminder
        fields = (
            'telnumber',
        )

    def __init__(self, *args, **kwargs):
        super(CreateForm, self).__init__(*args, **kwargs)

        self.initial['message_type'] = self.fields['message_type'].choices[0][0]

    def clean_telnumber(self):
        val = self.cleaned_data['telnumber']

        # Strip all whitespace
        val = ''.join(val.split())

        if re_telnumber.match(val) is None:
            raise forms.ValidationError(
                "This does not appear to be a valid UK phone number.",
            )

        return val

    def save(self, user):
        instance = super(CreateForm, self).save(commit=False)
        instance.user = user
        instance.save()

        return instance
