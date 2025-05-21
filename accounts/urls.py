from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views

urlpatterns = [
    path('auth/signup/', views.signup),    # 회원가입
    path('auth/login/', views.login),    # 로그인
    path('auth/logout/', views.logout),    # 로그아웃
    path('auth/<str:provider>/social-login/', views.social_login),    # 소셜 로그인
    path('auth/<str:provider>/callback/', views.callback),    # 콜백 함수
    # path('user/', views.profile),    # 회원 정보
    # path('user/nickname/', views.nickname),    # 닉네임
]
