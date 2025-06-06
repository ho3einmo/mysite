from django import forms
from django.utils.translation import gettext_lazy as _
from . import models
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