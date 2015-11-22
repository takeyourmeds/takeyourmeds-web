from django import forms

from ..reminders_calls.reminders_calls_audio.models import RecordRequest

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
