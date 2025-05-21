# from django.contrib.auth import backends, get_user_model
# from django.db.models import Q

# User = get_user_model()

# class EmailorUsernameAuthBackend(backends.ModelBackend):
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         if username is None or password is None:
#             print('실패')
#             return
        
#         try:
#             user = User.objects.get(
#                 Q(username__exact=username) | Q(email__exact=username)
#             )

#             print(user)

#             if user.check_password(password) and self.user_can_authenticate(user):
#                 print('성공')
#                 return user

#         except User.DoesNotExist:
#             print('실패')
#             return None
        
#         except:
#             print('실패')
#             return None
