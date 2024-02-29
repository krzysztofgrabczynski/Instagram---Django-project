from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

from src.post.models import PostModel
from src.social_actions.models import FollowModel
from src.user.mixins import SaveLastVisitedUrl


@method_decorator(SaveLastVisitedUrl(), name="dispatch")
class HomeView(LoginRequiredMixin, generic.TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        followers = [
            x.user_followed for x in FollowModel.objects.filter(user=self.request.user)
        ]
        extra_context = {
            "posts": PostModel.objects.filter(user__in=followers).order_by("-date")
        }
        context = super().get_context_data(**kwargs)
        context.update(extra_context)
        return context


class Search(LoginRequiredMixin, generic.RedirectView):
    url = reverse_lazy("home")

    def get(self, request, *args, **kwargs):
        username = request.GET.get("username_search")
        try:
            result = User.objects.get(username=username)
            self.url = reverse_lazy(
                "user_profile", kwargs={"pk": result.userprofilemodel.pk}
            )
            return super().get(request, *args, **kwargs)
        except ObjectDoesNotExist:
            return super().get(request, *args, **kwargs)
