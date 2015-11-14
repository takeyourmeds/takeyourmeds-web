from email_from_template import send_mail

from django import forms
from django.utils.http import int_to_base36
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator

from ..utils import validate_password

User = get_user_model()

class ForgotPasswordForm(forms.Form):
    email = forms.CharField(max_length=75)

    def save(self):
        user = self.cleaned_data['user']

        send_mail((user.email,),
            'account/forgot_password/forgot_password.email', {
                'user': user,
                'token': default_token_generator.make_token(user),
                'uidb36': int_to_base36(user.id),
            },
        )

    def clean_email(self):
        val = self.cleaned_data['email'].strip()

        try:
            self.cleaned_data['user'] = User.objects.get(email__iexact=val)
        except User.DoesNotExist:
            raise forms.ValidationError("Email address doesn't exist.")

        return val

class ResetPasswordForm(forms.Form):
    password = forms.CharField()

    def save(self):
        self.user.set_password(self.cleaned_data['password'])
        self.user.save()

        return self.user

    def clean_password(self):
        return validate_password(self.cleaned_data.get('password'))
