from django.urls import path, include

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from . import views

urlpatterns = [
    # 회원가입 / 로그인 / 로그아웃 
    path('auth/signup/', views.signup),                         # 회원가입
    path('auth/login/', views.login),                           # 로그인
    path('auth/logout/', views.logout),                  # 로그아웃
    path('auth/<str:provider>/login/', views.social_login),     # 소셜 로그인
    path('auth/<str:provider>/callback/', views.callback),      # 콜백 함수

    # 회원 정보 관련
    path('user/profile/', views.profile),                       # 회원 정보
    path('user/nickname/', views.set_nickname),                 # 닉네임
    path('user/change-password/', views.change_password),       # 비밀번호 수정
    
    # 토큰 관련
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('token/verify/', TokenVerifyView.as_view()),
]
