from django import forms

from src.post.models import PostModel


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ["user", "post_img", "description"]
        widgets = {"user": forms.HiddenInput()}

    def __init__(self, *args, **kwargs):
        current_user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        self._set_current_user(current_user)

    def _set_current_user(self, user):
        if user is not None:
            self.initial["user"] = user
        else:
            raise forms.ValidationError(
                "Class %s requires the 'user' keyword argument in the "
                "get_form_kwargs method. Please override the 'get_form_kwargs' method in the "
                "view that calls this class and include 'user' as 'request.user'."
                % self.__class__.__name__
            )
