from rest_framework import serializers

from .models import Goal
from accounts.serializers import UserSimpleInfoSerializer


# 목표 시리얼라이저
class GoalSerializer(serializers.ModelSerializer):

    user = UserSimpleInfoSerializer(read_only=True)

    class Meta:
        model = Goal
        fields = '__all__'


# 목표 타이틀 시리얼라이저
class GoalTitleSerializer(serializers.ModelSerializer):

    user = UserSimpleInfoSerializer(read_only=True)

    class Meta:
        model = Goal
        fields = ('id', 'goal_name', 'product_type', 'achievement_rate', )