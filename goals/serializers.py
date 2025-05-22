from django.shortcuts import get_object_or_404

from rest_framework import serializers

from .models import Goal, WishList
from finance.models import FinancialProduct, AdditionalProduct
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


# 찜한 상품 확인 시리얼라이저
class WishListReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishList
        fields = '__all__'


# 찜한 상품 등록 및 삭제
class WishListCreateSerializer(serializers.ModelSerializer):
    
    product_pk = serializers.IntegerField()
    come_from = serializers.CharField()

    def validate(self, data):
        product_pk = data['product_pk']
        come_from = data['come_from']
        
        if come_from == 'API':
            product = get_object_or_404(FinancialProduct, pk=product_pk)
            data['product'] = product
            return data
        
        elif come_from == 'USER':
            product = get_object_or_404(AdditionalProduct, pk=product_pk)
            data['product'] = product
            return data
        
        else:
            raise serializers.ValidationError("잘못된 상품입니다.")
        