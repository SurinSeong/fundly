from django.urls import path
from . import views

urlpatterns = [
    path('auth/signup/', views.signup),    # 회원가입
    # path('auth/login/', views.login),    # 로그인
    # path('auth/social-login/', views.social_login),    # 소셜 로그인
    # path('user/', views.profile),    # 회원 정보
    # path('user/nickname/', views.nickname),    # 닉네임
    # path('auth/<str:provider>/callback/', views.callback),
]
