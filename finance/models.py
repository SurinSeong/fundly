from django.db import models

# 금융 회사 모델
class FinancialCompany(models.Model):
    # 회사 코드
    code = models.CharField(max_length=20, unique=True)
    # 회사명
    name = models.CharField(max_length=20)
    # 홈페이지 주소
    homepage_url = models.CharField(max_length=50)
    # 콜센터 전화번호
    phone_number = models.CharField(max_length=20)


# 금융 상품 모델
class FinancialProduct(models.Model):
    # 코드
    code = models.CharField(max_length=20, unique=True)
    # 공시 제출년월
    published_date = models.CharField(max_length=6)
    # 상품명
    name = models.CharField(max_length=20)
    # 종류
    product_type = models.CharField(max_length=5)
    # 금융회사
    financial_company = models.ForeignKey(FinancialCompany, on_delete=models.CASCADE)
    # 우대 조건
    special_condition = models.CharField(max_length=200)
    # 가입 방법
    join_way = models.TextField()
    # 만기 후 이자율
    end_interest_rate = models.FloatField()
    # 가입 제한
    join_deny = models.CharField(max_length=10)
    # 가입 대상
    join_member = models.CharField(max_length=20)
    # 기타 유의사항
    etc_note = models.TextField()
    # 최고한도
    max_limit = models.IntegerField(null=True, blank=True)
    # 공시 시작일
    product_start_date = models.DateField()
    # 공시 종료일
    product_end_date = models.DateField(null=True, blank=True)
    # 금융회사 제출일
    submit_date = models.DateTimeField()


# 추가 금융 상품
class AdditionalProduct(models.Model):
    TYPE_CHOICES = [
        ('deposit', '예금'),
        ('savings', '적금'),
    ]
    # 상품명
    name = models.CharField(max_length=100)
    # 종류
    product_type = models.CharField(max_length=5,
                                    choices=TYPE_CHOICES,
                                    default='deposit',
                                    help_text='금융 상품 타입을 선택해주세요.',
                                    verbose_name='상품 타입',)
    # 금융회사
    financial_company = models.ForeignKey(FinancialCompany, on_delete=models.CASCADE)
    # 우대조건
    special_condition = models.TextField()
    # 가입 방법
    join_way = models.TextField()
    # 만기 후 이자율
    end_interest_rate = models.FloatField()
    # 가입 제한
    join_deny = models.CharField(max_length=10)
    # 가입 대상
    join_member = models.CharField(max_length=20)
    # 기타 유의사항
    etc_note = models.TextField()
    # 최고한도
    max_limit = models.IntegerField(null=True, blank=True)
    # 생성날짜
    created_at = models.DateTimeField(auto_now_add=True)
    

# 금융 상품 옵션
class OptionProduct(models.Model):
    # 금융 상품
    finance_product = models.ForeignKey(FinancialProduct, on_delete=models.CASCADE)
    # 저축 금리 유형
    save_type = models.CharField(max_length=5)
    # 저축 금리 유형명
    save_type_name = models.CharField(max_length=10)
    # 적립 유형
    reward_type = models.CharField(max_length=5, default='')
    # 적립 유형명
    reward_type_name = models.CharField(max_length=10, default='')
    # 저축 기간
    save_month = models.IntegerField()
    # 저축 금리
    interest_rate = models.FloatField()
    # 최고 우대 금리
    max_interest_rate = models.FloatField()
