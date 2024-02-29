from functools import wraps
from django.core.exceptions import ImproperlyConfigured
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib.auth.mixins import AccessMixin


class RedirectIfLoggedUserMixin:
    redirect_field_name = None

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return self.redirect_authenticated_user()
        return super().dispatch(request, *args, **kwargs)

    def get_redirect_field_name(self) -> str:
        redirect_field_name = (
            self.redirect_field_name or settings.SIGNUP_REDIRECT_URL
            if hasattr(settings, "SIGNUP_REDIRECT_URL")
            else self.redirect_field_name
        )

        if not redirect_field_name:
            raise ImproperlyConfigured(
                f"{self.__class__.__name__} is missing a redirect_field_name attribute. "
                f"Please define {self.__class__.__name__}.redirect_field_name or override "
                f"{self.__class__.__name__}.get_redirect_field_name()."
            )
        return str(redirect_field_name)

    def redirect_authenticated_user(self) -> HttpResponseRedirect:
        return HttpResponseRedirect(self.get_redirect_field_name())


class ObjectOwnerRequiredMixin(AccessMixin):
    permission_denied_message = (
        "You have to be the owner of the object you are trying to delete."
    )
    owner_field_name = None

    def get_object_owner(self):
        assert self.owner_field_name is not None, (
            f"`ObjectOwnerRequiredMixin.owner_field_name` cannot be None."
            f"You must override `ObjectOwnerRequiredMixin.owner_field_name` in {self.__class__.__name__} class."
        )

        fields = [field.name for field in self.model._meta.fields]
        if not self.owner_field_name in fields:
            raise ImproperlyConfigured(
                f"{self.model} needs to define `{self.owner_field_name}` field."
            )

        return getattr(self.get_object(), self.owner_field_name)

    def dispatch(self, request, *args, **kwargs):
        if not request.user == self.get_object_owner():
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class BaseLastVisitedUrlDecorator:
    last_visited_session = "last_visited"


class SaveLastVisitedUrl(BaseLastVisitedUrlDecorator):
    """
    Save into request.session current request path using `last_visited_session` value as session key.
    """

    def __call__(self, view_method):
        @wraps(view_method)
        def wrapper(request, *args, **kwargs):
            request.session[self.last_visited_session] = request.get_full_path()
            return view_method(request, *args, **kwargs)

        return wrapper


class SetLastVisitedUrl(BaseLastVisitedUrlDecorator):
    """
    Set url of the decorated view as last url saved in request.session, under session key as `last_visited_session` value.
    """

    def __call__(self, view_method):
        @wraps(view_method)
        def wrapper(request, *args, **kwargs):
            url = request.session.get(self.last_visited_session)
            cls = view_method.func.__self__
            cls.url = url
            return view_method(request, *args, **kwargs)

        return wrapper
