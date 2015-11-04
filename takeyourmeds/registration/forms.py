from django import forms

from takeyourmeds.account.utils import validate_password

from takeyourmeds.account.models import User

class RegistrationForm(forms.ModelForm):
    password = forms.CharField()

    class Meta:
        model = User
        fields = (
            'email',
        )

    def save(self):
        # Create user
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.save()

        return user

    def clean_password(self):
        return validate_password(self.cleaned_data.get('password'))

    def clean_email(self):
        email = self.cleaned_data['email'].strip()

        if not email:
            raise forms.ValidationError("This field is required.")

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("That email address is already in use.")

        return email
