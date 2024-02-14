from django.http import HttpResponseNotAllowed, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from src.user.mixins import ObjectOwnerRequiredMixin
from src.comment.models import CommentModel
from src.comment.forms import CommentCreateForm
from src.post.models import PostModel


class CreateCommentView(generic.edit.BaseFormView):
    form_class = CommentCreateForm
    success_url = reverse_lazy("home")

    permitted_methods = ("POST",)

    def get(self):
        raise HttpResponseNotAllowed(self.permitted_methods)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.user = self.request.user
        comment.post = PostModel.objects.get(pk=self.kwargs["pk"])
        comment.save()

        return super().form_valid(form)

    def form_invalid(self):
        return HttpResponseRedirect(self.request.path)


class DeleteCommentView(
    ObjectOwnerRequiredMixin,
    generic.edit.DeletionMixin,
    generic.detail.SingleObjectMixin,
    generic.base.View,
):
    model = CommentModel
    success_url = reverse_lazy("home")

    owner_field_name = "user"

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
