# class FollowContextManager:
#     def __init__(self, user, profile):
#         self.user = user
#         self.profile = profile
#         self.is_followed = False

#     def __enter__(self):
#         for item in self.user.follower.all():
#             if item in self.profile.user.followed.all():
#                 self.is_followed = True
#                 break
#             else:
#                 self.is_followed = False

#         return self

#     def __exit__(self, exc_type, exc_value, trace):
#         pass


# class ThumbUpContexManager:
#     def __init__(self, user, post):
#         self.user = user
#         self.post = post

#     def __enter__(self):
#         for item in self.post.like_set.all():
#             if item in self.user.like_set.all():
#                 item.delete()
#                 return self
#         return None

#     def __exit__(self, exc_type, exc_value, trace):
#         pass
