from django import forms

from nabes_app.models import Profile

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['primary_last_name', 'primary_email', 'street', 'number']
