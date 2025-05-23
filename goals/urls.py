from django.urls import path
from . import views

urlpatterns = [
    path('goals/', views.goals),    # 목표 조회, 생성
    path('goals/<int:goal_pk>/', views.goal_detail),    # 목표 상세 조회, 수정, 삭제
    path('wishlist/', views.wish_list),    # 찜하기 전체 조회 / 찜하기 / 삭제
    # 사용자 설정 상품
    path('custom/', views.custom_product),
    path('custom/<int:custom_pk>/', views.custom_detail)
]
