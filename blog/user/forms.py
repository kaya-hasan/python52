from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=150, label="Username")
    password1 = forms.CharField(
        max_length=20, widget=forms.PasswordInput, label="Password")
    password2 = forms.CharField(
        max_length=20, widget=forms.PasswordInput, label="Confirm Password")

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("confirm_password")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data
