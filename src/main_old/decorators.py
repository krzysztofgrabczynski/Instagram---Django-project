# from django.shortcuts import redirect
# from .models import Post, Comment


# def if_logged(func):
#     def wrapper_func(request, *args, **kwargs):
#         if request.user.is_authenticated:
#             return redirect("home")

#         return func(request, *args, **kwargs)

#     return wrapper_func


# def authorization_id(func):
#     def wrapper_func(request, *args, **kwargs):
#         userprofile = request.user.userprofile
#         id = kwargs["id"]

#         if not userprofile.id == id:
#             return redirect("home")

#         return func(request, *args, **kwargs)

#     return wrapper_func


# def authorization_id_post(func):
#     def wrapper_func(request, *args, **kwargs):
#         id = kwargs["id"]
#         post = Post.objects.get(id=id)

#         if request.user != post.user:
#             return redirect("home")

#         return func(request, *args, **kwargs)

#     return wrapper_func


# def authorization_id_comment(func):
#     def wrapper_func(request, *args, **kwargs):
#         id = kwargs["id"]
#         comment = Comment.objects.get(id=id)

#         if request.user != comment.user:
#             return redirect("home")

#         return func(request, *args, **kwargs)

#     return wrapper_func
