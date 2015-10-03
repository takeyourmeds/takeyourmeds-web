from django import forms
from django.contrib.auth.models import User

from takeyourmeds.account.utils import validate_password

class RegistrationForm(forms.ModelForm):
    username = forms.RegexField(
        regex=r'^[\w+-]+$',
        max_length=30,
        error_messages={
            'invalid': "This value may contain only letters, numbers and "
                "./+/-/_ characters.",
        },
    )

    password = forms.CharField()

    class Meta:
        model = User
        fields = (
            'email',
            'username',
        )

    def save(self):
        # Create user
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.save()

        return user

    def clean_username(self):
        username = self.cleaned_data['username'].strip()

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("That username is already taken.")

        return username

    def clean_password(self):
        return validate_password(self.cleaned_data.get('password'))

    def clean_email(self):
        email = self.cleaned_data['email'].strip()

        if not email:
            raise forms.ValidationError("This field is required.")

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("That email address is already in use.")

        return email
