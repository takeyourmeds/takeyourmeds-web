from django import forms
from django.conf import settings

from takeyourmeds.utils.url import resolve_absolute
from takeyourmeds.utils.twilio import get_twilio_client, sanitise_phone_number

from .models import CreateRequest

class CreateForm(forms.ModelForm):
    class Meta:
        model = CreateRequest
        fields = (
            'phone_number',
        )

    def save(self, user):
        instance = super(CreateForm, self).save(commit=False)
        instance.user = user
        instance.twilio_sid = None # We populate this later
        instance.save()

        resource = get_twilio_client().calls.create(
            to=sanitise_phone_number(instance.phone_number),
            from_=settings.TWILIO_CALL_FROM,
            url=resolve_absolute(
                'recordings:create:twiml-callback', instance.ident,
            ),
        )

        instance.twilio_sid = resource.sid
        instance.save(update_fields=('twilio_sid',))

        return instance
