from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .utils_company import create_company_data
from .utils_product import create_finance_data
from .serializers import FinancialCompanySerializer, FinancialProductSerializer, OptionProductSerializer, AdditionalProductSerializer
from .models import FinancialCompany, FinancialProduct, AdditionalProduct, OptionProduct

# 금감원 API 활용 데이터 저장하기
@api_view(['GET'])
def save_financial_data(request):
    products, options = create_finance_data()
    companys = create_company_data()

    # 금융 회사 저장
    for company in companys:
        serializer = FinancialCompanySerializer(data=company)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

    # 금융 상품 저장
    for product in products:
        financial_company = FinancialCompany.objects.get(code=product['finance_company_id'])
        product['financial_company'] = financial_company.id
        serializer = FinancialProductSerializer(data=product)
        if serializer.is_valid(raise_exception=True):
            serializer.save(financial_company=financial_company)

    # 금융 옵션 저장
    for option in options:
        financial_product = FinancialProduct.objects.get(code=option['finance_product_id'])
        option['financial_product'] = financial_product.id
        serializer = OptionProductSerializer(data=option)
        if serializer.is_valid(raise_exception=True):
            serializer.save(financial_product=financial_product)

    return Response({'save': 'completed'}, status=status.HTTP_202_ACCEPTED)

    