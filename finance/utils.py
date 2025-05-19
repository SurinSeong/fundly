# 금감원 API 사용해서 데이터 받아오기
import requests
import json
import re

from django.conf import settings

# 요청 url
BASE_URL = 'http://finlife.fss.or.kr/finlifeapi/'

# 정기 예금 : depositProductsSearch >> (030300) max_page_no=4
# 적금 : savingProductsSearch >> (030300) max_page_no=3
# => 020000, 030300 밖에 상품이 없음.
# 금융회사 : companySearch >> max_page_no=1

# 데이터 불러오기
def get_fin_data(topFinGrpNo, target):
    # 요청 URL
    API_URL = BASE_URL + target + '.json'
    params = {
        'auth': settings.FINANCE_API_KEY,
        'topFinGrpNo': topFinGrpNo,
        'pageNo': 1
    }
    
    response = requests.get(API_URL, params=params).json()
    
    # 상품 리스트 추출
    products = response['result']['baseList']
    
    # 옵션 리스트 추출
    options = response['result']['optionList']
    
    # 원하는 필드 추출하기 - products
    extracted_products = []
    for product in products:
        new_fields = {}
        for key in product.keys():
            if key in ['fin_prdt_cd', 'kor_co_nm', 'fin_prdt_nm', 'etc_note', 'join_deny', 'join_member', 'join_way', 'spcl_cnd']:
                new_fields[key] = product.get(key, '')
        extracted_products.append(new_fields)
