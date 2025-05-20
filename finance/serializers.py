from rest_framework import serializers
from .models import FinancialCompany, FinancialProduct, AdditionalProduct, OptionProduct

# 금융 회사 직렬화 시리얼라이저
class FinancialCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialCompany
        fields = '__all__'


# 금융 상품 직렬화 시리얼라이저
class FinancialProductSerializer(serializers.ModelSerializer):

    # 외래 키인 금융회사에 대해 시리얼라이저 적용
    financial_company = FinancialCompanySerializer(read_only=True)

    class Meta:
        model = FinancialProduct
        fields = '__all__'


# 금융 상품 옵션 직렬화 시리얼라이저
class OptionProductSerializer(serializers.ModelSerializer):

    # 외래 키인 금융 상품에 대해 시리얼 라이저 적용
    financial_product = FinancialProductSerializer(read_only=True)

    class Meta:
        model = OptionProduct
        fields = '__all__'


# 추가 금융 상품 직렬화 시리얼라이저
class AdditionalProductSerializer(serializers.ModelSerializer):

    # 외래 키인 금융 회사에 대해 시리얼라이저 적용
    financial_company = FinancialCompanySerializer(read_only=True)

    class Meta:
        model = AdditionalProduct
        fields = '__all__'