from django import forms
from django.contrib.auth import authenticate

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()

    def __init__(self, request=None, *args, **kwargs):
        self.user = None
        self.request = request

        super(LoginForm, self).__init__(*args, **kwargs)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            user = authenticate(username=email, password=password)

            if user is None:
                raise forms.ValidationError(
                    "Please enter a valid email address and password",
                )

            self.cleaned_data['user'] = user

        return self.cleaned_data

