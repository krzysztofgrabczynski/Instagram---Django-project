from django.views import generic

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
