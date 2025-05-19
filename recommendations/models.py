from django.db import models
from django.conf import settings

from finance.models import FinancialProduct, AdditionalProduct
from goals.models import Goal

# 추천
class Recommendation(models.Model):
    # 사용자
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 목표
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    # 상품
    finance_product = models.ForeignKey(FinancialProduct, on_delete=models.CASCADE, null=True, blank=True)
    additional_product = models.ForeignKey(AdditionalProduct, on_delete=models.CASCADE, null=True, blank=True)
    # 추천 점수
    score = models.FloatField()
    
