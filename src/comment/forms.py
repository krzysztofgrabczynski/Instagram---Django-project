from django import forms

from src.comment.models import CommentModel


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = [
            "text",
        ]
