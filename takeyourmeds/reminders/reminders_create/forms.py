import re

from django import forms

from ..reminders_calls.reminders_calls_audio.models import RecordRequest

from ..apps import RemindersConfig
from ..enums import TypeEnum
from ..models import Reminder

NUM_REMINDERS = 4
HOUR_MIN, HOUR_MAX = 5, 24

TIME_CHOICES = [(y, y) for y in [
    '%02d:00' % (x % 24) for x in range(HOUR_MIN, HOUR_MAX + 1)
]]

re_phone_number = re.compile(r'^\d{9,14}$')

class CreateForm(forms.ModelForm):
    frequency = forms.ChoiceField(
        choices=[(x, x) for x in range(1, NUM_REMINDERS + 1)],
    )

    message_type = forms.ChoiceField(choices=[
        ('voice', u"Voice"),
        ('text', u"Text"),
    ])

    class Meta:
        model = Reminder
        fields = (
            'message',
            'audio_url',
            'phone_number',
        )

    def __init__(self, *args, **kwargs):
        super(CreateForm, self).__init__(*args, **kwargs)

        # Dynamically generate enough time selector fields
        self.time_fields = []
        for x in range(NUM_REMINDERS):
            name = 'times_%d' % x
            self.fields[name] = forms.ChoiceField(choices=TIME_CHOICES)
            self.initial[name] = '%02d:00' % (9 + (3 * x))
            self.time_fields.append(self[name])

        self.fields['audio_url'].choices = RemindersConfig.voice_reminders

        self.initial['message_type'] = self.fields['message_type'].choices[0][0]

    def save(self, user):
        instance = super(CreateForm, self).save(commit=False)
        instance.user = user
        instance.type = TypeEnum.message if \
            self.cleaned_data['message_type'] == 'text' else TypeEnum.call
        instance.save()

        for x in self.get_times():
            instance.times.create(time=x.value())

        return instance

    def clean(self):
        # Check for duplicate times
        seen = set()
        for x in self.get_times():
            val = x.value()
            if val in seen:
                self.add_error(x.name, "You have already selected this time.")
            seen.add(val)

        if self.cleaned_data['message_type'] == 'text':
            val = self.cleaned_data.get('message', '').strip()
            self.cleaned_data['message'] = val

            if not val:
                self.add_error('message', "Please enter a message.")

        return self.cleaned_data

    def clean_phone_number(self):
        val = self.cleaned_data['phone_number']

        # Strip all whitespace
        val = ''.join(val.split())

        if re_phone_number.match(val) is None:
            raise forms.ValidationError(
                "This does not appear to be a valid UK phone number.",
            )

        return val

    def get_times(self):
        num_times = int(self.cleaned_data['frequency'])

        return self.time_fields[:num_times]


class CreateRecordRequestForm(forms.ModelForm):
    class Meta:
        model = RecordRequest
        fields = (
            'phone_number',
        )

    def save(self, user):
        return user.audio_recording_requests.start_record_request(
            self.cleaned_data['phone_number'],
        )
