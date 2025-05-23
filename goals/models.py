from django.db import models
from django.conf import settings

from finance.models import FinancialProduct, AdditionalProduct, OptionProduct

# 금융 목표
class Goal(models.Model):
    TYPE_CHOICES = [
        ('D', '예금'),
        ('S', '적금'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)      # 사용자
    goal_name = models.CharField(max_length=100)                                      # 목표명
    product_type = models.CharField(max_length=10,
                                    choices=TYPE_CHOICES,
                                    default='D',
                                    help_text='목표 실현을 위한 상품 타입을 선택해주세요.',
                                    verbose_name='상품 타입',)                         # 목표 실현 방식 (상품 타입)
    saving_target_amount = models.PositiveIntegerField(null=True, blank=True)         # 적금 목표 금액
    deposit_target_amount = models.PositiveIntegerField(null=True, blank=True)        # 예금 목표 금액
    start_date = models.DateField()                                                   # 시작 날짜
    end_date = models.DateField()                                                     # 마지막 날짜
    achievement_rate = models.FloatField()                                            # 목표 달성률
    created_at = models.DateTimeField(auto_now_add=True)                              # 생성 날짜
    updated_at = models.DateTimeField(auto_now=True)                                  # 수정 날짜
    

# 찜한 상품
class WishList(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)                                  # 사용자
    finance_product = models.ForeignKey(FinancialProduct, on_delete=models.CASCADE, null=True, blank=True)        # 금융 상품
    additional_product = models.ForeignKey(AdditionalProduct, on_delete=models.CASCADE, null=True, blank=True)    # 사용자가 추가한 상품
    created_at = models.DateTimeField(auto_now_add=True)                                                          # 생성 일자
    updated_at = models.DateTimeField(auto_now=True)                                                              # 수정 일자
    
    
# 사용자가 커스텀한 상품 정보
class ConnectedToGoal(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)                                 # 사용자
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)                                                     # 목표
    finance_product = models.ForeignKey(FinancialProduct, on_delete=models.CASCADE, null=True, blank=True)       # 선택한 상품
    additional_product = models.ForeignKey(AdditionalProduct, on_delete=models.CASCADE, null=True, blank=True)
    option_product = models.ForeignKey(OptionProduct, on_delete=models.CASCADE, null=True, blank=True)           # 옵션
    current_amount = models.PositiveIntegerField()                                                               # 납입 금액
    target_amount = models.PositiveIntegerField()                                                                # 목표 금액
    start_date = models.DateField()                                                                              # 시작 날짜
    duration_months = models.IntegerField(null=True, blank=True)                                                 # 지속 기간
    is_active = models.BooleanField(default=False)                                                               # 중도 해지 여부
    created_at = models.DateTimeField(auto_now_add=True)                                                         # 생성 날짜
    updated_at = models.DateTimeField(auto_now=True)                                                             # 수정 날짜
    