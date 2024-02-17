from django.forms import BaseModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from src.post.models import PostModel
from src.post.forms import CreatePostForm
from src.user.mixins import ObjectOwnerRequiredMixin
from src.user.models import UserProfileModel


class CreatePostView(generic.CreateView):
    model = PostModel
    form_class = CreatePostForm
    template_name = "add_post.html"
    success_url = reverse_lazy("home")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({"user": self.request.user})
        return kwargs

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        self.object = form.save()
        self._increase_posts_amount()
        return HttpResponseRedirect(self.get_success_url())

    def _increase_posts_amount(self):
        user_profile = UserProfileModel.objects.get(user=self.request.user)
        user_profile.posts_amount += 1
        user_profile.save()


class EditPostView(ObjectOwnerRequiredMixin, generic.edit.UpdateView):
    model = PostModel
    form_class = CreatePostForm
    template_name = "edit_post.html"
    success_url = reverse_lazy("home")

    owner_field_name = "user"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({"user": self.request.user})
        return kwargs


class DeletePostView(ObjectOwnerRequiredMixin, generic.edit.DeleteView):
    model = PostModel
    template_name = "delete_post_confirm.html"
    success_url = reverse_lazy("home")

    owner_field_name = "user"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        self.object.delete()
        self._decrease_posts_amount()
        return HttpResponseRedirect(self.get_success_url())

    def _decrease_posts_amount(self):
        user_profile = UserProfileModel.objects.get(user=self.request.user)
        user_profile.posts_amount -= 1
        user_profile.save()
