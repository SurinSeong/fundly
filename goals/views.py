from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import GoalSerializer, GoalTitleSerializer
from .models import Goal

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