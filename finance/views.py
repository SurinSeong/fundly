from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .utils_company import create_company_data
from .utils_product import create_finance_data
from .serializers import (
                            FinancialCompanySerializer,
                            FinancialProductSerializer,
                            OptionProductSerializer,
                            ProductReadSerializer,
                            ProductCreateSerializer,
                            AdditionalProductReadSerializer,
                        )
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
        financial_company = FinancialCompany.objects.get(code=product['financial_company_id'])
        product['financial_company'] = financial_company.id
        serializer = FinancialProductSerializer(data=product)
        if serializer.is_valid(raise_exception=True):
            serializer.save(financial_company=financial_company)
        else:
            print(product)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    # 금융 옵션 저장
    for option in options:
        financial_company = FinancialCompany.objects.get(code=option['financial_company_id'])
        financial_products = FinancialProduct.objects.filter(code=option['financial_product_id'], financial_company=financial_company)

        for financial_product in financial_products:

            option['financial_company'] = financial_company.id
            option['financial_product'] = financial_product.id

            serializer = OptionProductSerializer(data=option)
            if serializer.is_valid(raise_exception=True):
                serializer.save(financial_company=financial_company,
                                financial_product=financial_product)
            else:
                print(option)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response({'save': 'completed'}, status=status.HTTP_202_ACCEPTED)


# 금융 상품 목록 조회 및 생성
@api_view(['GET', 'POST'])
def finance_product(request):
    if request.method == 'POST':
        serializer = ProductCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    if request.method == 'GET':
        # 검색 키워드 받기
        keyword = request.data['keyword']
        # 키워드가 있으면
        if keyword:
            official_product = FinancialProduct.objects.filter(product_name__icontains=keyword)
            additional_product = AdditionalProduct.objects.filter(product_name__icontains=keyword)
        else:
            official_product = FinancialProduct.objects.all()
            additional_product = AdditionalProduct.objects.all()
        
        official_serializer = ProductReadSerializer(official_product, many=True)
        additional_serializer = AdditionalProductReadSerializer(additional_product, many=True)

        return Response({
            'official_products': official_serializer.data,
            'additional_products': additional_serializer.data
        })


# 상품 + 옵션 상세 조회
@api_view(['GET'])
def product_detail(request, product_pk):
    # 조회하려는 상품명
    product_name = request.data.get(product_name)

    official_product = FinancialProduct.objects.get(pk=product_pk)
    additional_product = AdditionalProduct.objects.get(pk=product_pk)
    
    if official_product and official_product.product_name == product_name:
        options = OptionProduct.objects.filter(finance_product=official_product)
        product = official_product
    
    elif additional_product and additional_product.product_name == product_name:
        options = OptionProduct.objects.filter(finance_product=additional_product)
        product = additional_product

    else:
        return Response({'error':'상품이 존재하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
    
    product_serializer = FinancialProductSerializer(product)
    options_serializer = OptionProductSerializer(options, many=True)
    return Response({
        'product': product_serializer.data,
        'options': options_serializer.data
    })


