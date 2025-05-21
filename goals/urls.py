from django.urls import path
from . import views

urlpatterns = [
    path('', views.goals),    # 목표 조회, 생성
    path('<int:goal_pk>/', views.goal_detail),    # 목표 상세 조회, 수정, 삭제
]
