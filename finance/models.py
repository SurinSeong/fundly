from django.db import models

# 금융 회사 모델
class FinancialCompany(models.Model):
    # 회사 코드
    code = models.CharField(max_length=20)
    # 회사명
    name = models.CharField(max_length=20)
    # 홈페이지 주소
    homepage_url = models.CharField(max_length=50)
    # 콜센터 전화번호
    phone_number = models.CharField(max_length=20)


# 금융 상품 모델
class FinancialProduct(models.Model):
    # 코드
    code = models.CharField(max_length=20)
    # 공시 제출년월
    # 상품명
    # 종류
    # 금융회사
    # 우대 조건
    # 가입 방법
    # 만기 후 이자율
    # 가입 제한
    # 가입 대상
    # 기타 유의사항
    # 최고한도
    # 공시 시작일
    # 공시 종료일
    # 금융회사 제출일

# 추가 금융 상품
class AdditionalProduct(models.Model):
    pass


# 금융 상품 옵션
class OptionProduct(models.Model):
    pass

