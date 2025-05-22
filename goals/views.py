from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import GoalSerializer, GoalTitleSerializer, WishListReadSerializer
from .models import Goal, WishList
from finance.models import FinancialProduct, AdditionalProduct

# Create your views here.
# 목표 조회, 생성
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def goals(request):
    user = request.user
    if request.method == 'GET':
        goals = Goal.objects.all()
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
        

# 찜한 상품 전체 목록 조회 >> 마이페이지용
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def wish_list(request):
    user = request.user
    wish_list = WishList.objects.filter(user=user)
    serialzier = WishListReadSerializer(wish_list)
    return Response(serialzier.data)


# 찜하기
@api_view(['POST', 'DELETE'])
def wish(request, product_pk):
    user = request.user
    come_from = request.data.get('come_from')
    if come_from == 'API':
        product = FinancialProduct.objects.get(pk=product_pk)
    elif come_from == 'USER':
        product = AdditionalProduct.objects.get(pk=product_pk)

    if request.method == 'POST':
        pass

    if request.method == 'DELETE':
        if come_from == 'API':
            wish_list = get_object_or_404(WishList, user=user, financial_product=product)
        elif come_from == 'USER':
            wish_list = get_object_or_404(WishList, user=user, financial_product=product)

    
       
    
