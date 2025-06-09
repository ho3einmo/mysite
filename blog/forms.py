from django import forms
from django.utils.translation import gettext_lazy as _
from . import models
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['comment']
        labels = {
            "comment": _("Comment"),
        }
        help_texts = {
            "comment": _("Write your comment here."),
        }
class SignUpForm(UserCreationForm):
    class Meta:
        model = models.User
        fields = ('username', 'email', 'password1', 'password2')
        labels = {
            "username": _("Username"),
            "email": _("Email"),
            "password1": _("Password"),
            "password2": _("Confirm Password"),
        }
        help_texts = {
            "username": _("Enter a unique username."),
            "email": _("Enter a valid email address."),
            "password1": _("Enter your password."),
            "password2": _("Re-enter your password for confirmation."),
        }

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
