from django.urls import reverse_lazy
from django.views import generic
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User

from src.post.models import PostModel


class HomeView(generic.TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        extra_context = {
            "posts": PostModel.objects.filter(user=self.request.user).order_by(
                "-date"
            )  # has to be change for all posts of the people you are following
        }
        context = super().get_context_data(**kwargs)
        context.update(extra_context)
        return context


class Search(generic.RedirectView):
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
