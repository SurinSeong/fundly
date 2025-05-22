from django.db import models
from django.conf import settings

from finance.models import FinancialProduct, AdditionalProduct, OptionProduct

# 금융 목표
class Goal(models.Model):
    TYPE_CHOICES = [
        ('deposit', '예금'),
        ('savings', '적금'),
    ]
    # 사용자
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 목표명
    goal_name = models.CharField(max_length=100)
    # 목표 실현 방식 (상품 타입)
    product_type = models.CharField(max_length=10,
                                    choices=TYPE_CHOICES,
                                    default='deposit',
                                    help_text='목표 실현을 위한 상품 타입을 선택해주세요.',
                                    verbose_name='상품 타입',)
    # 목표 금액
    target_amount = models.IntegerField()
    # 시작 날짜
    start_date = models.DateField()
    # 마지막 날짜
    end_date = models.DateField()
    # 월 소득
    monthly_income = models.IntegerField()
    # 현재 자산
    assets = models.IntegerField()
    # 목표 달성률
    achievement_rate = models.FloatField()
    # 생성 날짜
    created_at = models.DateTimeField(auto_now_add=True)
    # 수정 날짜
    updated_at = models.DateTimeField(auto_now=True)
    

# 찜한 상품
class WishList(models.Model):
    # 사용자
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 금융 상품
    finance_product = models.ForeignKey(FinancialProduct, on_delete=models.CASCADE, null=True, blank=True)
    # 사용자가 추가한 상품
    additional_product = models.ForeignKey(AdditionalProduct, on_delete=models.CASCADE, null=True, blank=True)
    # 생성 일자
    created_at = models.DateTimeField(auto_now_add=True)
    # 수정 일자
    updated_at = models.DateTimeField(auto_now=True)
    
    
# 사용자가 커스텀한 상품 정보
class UserCustomProduct(models.Model):
    # 사용자
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 목표
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    # 선택한 상품
    finance_product = models.ForeignKey(FinancialProduct, on_delete=models.CASCADE, null=True, blank=True)
    additional_product = models.ForeignKey(AdditionalProduct, on_delete=models.CASCADE, null=True, blank=True)
    # 옵션
    option_product = models.ForeignKey(OptionProduct, on_delete=models.CASCADE, null=True, blank=True)
    # 납입 금액
    amount = models.IntegerField()
    # 시작 날짜
    start_date = models.DateField()
    # 지속 기간
    duration_months = models.IntegerField(null=True, blank=True)
    # 중도 해지 여부
    is_active = models.BooleanField(default=False)
    # 생성 날짜
    created_at = models.DateTimeField(auto_now_add=True)
    # 수정 날짜
    updated_at = models.DateTimeField(auto_now=True)
    