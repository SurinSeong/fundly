from django.urls import path, include
from . import views

urlpatterns = [
    # path('auth/signup/', views.signup),    # 회원가입
    path('auth/signup/', include('dj_rest_auth.registration.urls')),
    path('auth/login/', views.login),    # 로그인
    path('auth/<str:provider>/social-login/', views.social_login),    # 소셜 로그인
    path('auth/social-logout/', views.social_logout),    # 소셜 로그아웃
    path('auth/<str:provider>/callback/', views.callback),    # 콜백 함수
    path('user/profile/', views.profile),    # 회원 정보
    path('user/nickname/', views.set_nickname),    # 닉네임
    path('user/change-password/', views.change_password),    # 비밀번호 수정
]
