from django import forms
from django.contrib.auth.password_validation import validate_password

from takeyourmeds.groups.models import AccessToken
from takeyourmeds.account.models import User

class RegistrationForm(forms.ModelForm):
    password = forms.CharField()
    access_token = forms.CharField(required=False)

    class Meta:
        model = User
        fields = (
            'email',
        )

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.access_token = None

    def save(self):
        # Create user
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.save()

        # Associate user with this access token if one was provided
        if self.access_token is not None:
            self.access_token.user = user
            self.access_token.save()

        return user

    def clean_email(self):
        email = self.cleaned_data['email'].strip()

        if not email:
            raise forms.ValidationError("This field is required.")

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("That email address is already in use.")

        return email

    def clean_password(self):
        val = self.cleaned_data.get('password')
        validate_password(val)
        return val

    def clean_access_token(self):
        val = self.cleaned_data['access_token'].strip()

        if not val:
            return val

        try:
            self.access_token = AccessToken.objects.get(
                access_token__iexact=val,
            )
        except AccessToken.DoesNotExist:
            raise forms.ValidationError(
                "Could not recognise this access token."
            )

        if self.access_token.user_id is not None:
            raise forms.ValidationError(
                "This access token has already been used."
            )

        return self.access_token.val
