from django import forms
from users.models import User, Profile


class SignupForm(forms.Form):

    username = forms.CharField(min_length=4, max_length=50)
    password = forms.CharField(max_length=70, widget=forms.PasswordInput)
    password_confirmation = forms.CharField(
        max_length=70, widget=forms.PasswordInput)
    first_name = forms.CharField(min_length=2, max_length=50)
    last_name = forms.CharField(min_length=2, max_length=50)

    email = forms.CharField(
        min_length=6,
        max_length=70,
        widget=forms.EmailInput()
    )

    def clean_username(self):
        """Username must be unique"""

        username = self.cleaned_data['username']
        username_exist = User.objects.filter(username=username).exists()

        if username_exist:
            raise forms.ValidationError('Username is already in use')
        else:
            return username

    def clean(self):
        """Verify password confirmation match"""
        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Password does not match')
        else:
            return data

    def save(self):
        """Create user and profile."""
        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()
