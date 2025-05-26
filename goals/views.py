from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import (
                            GoalSerializer, 
                            GoalTitleSerializer, 
                            WishListReadSerializer, 
                            WishListCreateSerializer,
                            TotalCustomReadSerializer,
                            CustomCreateSerializer,
                            CustomDetailSerializer,
                        )

from .models import Goal, WishList, ConnectedToGoal

# Create your views here.
# 목표 조회, 생성
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def goals(request):
    user = request.user
    print(request.user)
    if request.method == 'GET':
        goals = Goal.objects.filter(user=user)
        serializer = GoalTitleSerializer(goals, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = GoalSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

# 목표 상세 조회, 수정, 삭제
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def goal_detail(request, goal_pk):
    user = request.user
    goal = get_object_or_404(Goal, pk=goal_pk)

    if request.method == 'GET':
        serializer = GoalSerializer(goal)
        return Response(serializer.data)
    
    if goal.user.id == user.pk:
        if request.method == 'PUT':
            serializer = GoalSerializer(goal, request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            
        if request.method == 'DELETE':
            goal.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        

# 찜한 상품 전체 목록 조회 (마이페이지에서), 상품 찜하기/삭제하기 (상품 목록에서)
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def wish_list(request):
    user = request.user
    
    if request.method == 'GET':
        wish_list = WishList.objects.filter(user=user)
        serialzier = WishListReadSerializer(wish_list)
        return Response(serialzier.data)
    
    if request.method == 'POST':
        serializer = WishListCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            product = serializer.validated_data['product']
            come_from = serializer.validated_data['come_from']
            if come_from == 'API':
                wish_list, created = WishList.objects.get_or_create(
                    user=user, financial_product=product
                )
            elif come_from == 'USER':
                wish_list, created = WishList.objects.get_or_create(
                    user=user, additional_product=product
                )
            
            # 이미 찜한 상품이라면
            if not created:
                wish_list.delete()    # 삭제
                return Response({'message': '찜 해재'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': '찜 등록'}, status=status.HTTP_201_CREATED)

       
# 사용자가 설정한 상품 전체 조회 및 생성
@api_view(['GET', 'POST'])
def custom_product(request):
    if request.method == 'GET':
        user_custom_products = ConnectedToGoal.objects.all()
        serializer = TotalCustomReadSerializer(user_custom_products, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        data = request.data.copy()
        data['user'] = request.user.id
        serializer = CustomCreateSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

# 사용자가 설정한 특정 상품 조회, 삭제, 수정
@api_view(['GET', 'PUT', 'DELETE'])
def custom_detail(request, custom_pk):
    user = request.user
    custom_product = ConnectedToGoal.objects.get(pk=custom_pk)
    
    if custom_product.user == user:
        if request.method == 'GET':
            serializer = CustomDetailSerializer(custom_product)
            return Response(serializer.data)
        
        if request.method == 'PUT':
            serializer = CustomDetailSerializer(custom_product, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            
        if request.method == 'DELETE':
            custom_product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
