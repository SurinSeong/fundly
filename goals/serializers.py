from rest_framework import serializers

from .models import Goal, WishList
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
class WishListCDSerializer(serializers.ModelSerializer):
    product_name = serializers.SerializerMethodField()
    product_type = serializers.SerializerMethodField()

    class Meta:
        model = WishList
        fields = ('id', 'product_name', 'product_name', )

    def get_product_name(self, obj):
        if obj.financial_product:
            return obj.financial_product.name
        elif obj.additional_product:
            return obj.additional_product.product_name
        return None
    
    def get_product_type(self, obj):
        if obj.financial_product:
            return "API"
        elif obj.additional_product:
            return "USER"
        return None