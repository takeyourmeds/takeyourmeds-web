from email.utils import formataddr
from email_from_template import send_mail

from django import forms
from django.conf import settings

class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    subject = forms.CharField()
    message = forms.CharField()

    def save(self):
        from_email = formataddr((
            self.cleaned_data['name'],
            self.cleaned_data['email'],
        ))

        send_mail(
            (settings.DEFAULT_FROM_EMAIL,),
            'static/contact.email',
            self.cleaned_data,
            from_email,
        )
