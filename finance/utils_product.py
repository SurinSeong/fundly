# 금감원 API 사용해서 데이터 받아오기
import requests
import json
import re
import os

from django.conf import settings

# 요청 url
BASE_URL = 'http://finlife.fss.or.kr/finlifeapi/'

# 정기 예금 : depositProductsSearch >> (030300) max_page_no=4
# 적금 : savingProductsSearch >> (030300) max_page_no=3
# => 020000, 030300 밖에 상품이 없음.

# 데이터 불러오기 >> 정기 예금, 적금 관련
def get_fin_data(topFinGrpNo, target):

    products, options = [], []

    for n in range(1, 5):
        # 요청 URL
        API_URL = BASE_URL + target + '.json'
        params = {
            'auth': settings.FINANCE_API_KEY,
            'topFinGrpNo': topFinGrpNo,
            'pageNo': n
        }
    
        response = requests.get(API_URL, params=params).json()

        if not response['result']['baseList']:
            break

        # 상품 리스트 추출
        products.extend(response['result']['baseList'])

        # 옵션 리스트 추출
        options.extend(response['result']['optionList'])
    
    # 모든 필드 추출하기 - products
    extracted_products = []
    for product in products:
        product_dict = {}

        # 예금 or 적금
        if target == 'depositProductsSearch':
            product_dict['product_type'] = 'D'
        elif target == 'savingProductsSearch':
            product_dict['product_type'] = 'S'

        for key in product.keys():
            if key not in ['kor_co_nm']:
                product_dict[key] = product.get(key, '')
        extracted_products.append(product_dict)

    # 모든 필드 추출하기 - options
    extracted_options = []
    for option in options:
        option_dict = {}
        for key in option.keys():
            if key not in ['dcls_month', 'fin_co_no', 'intr_rate_type_nm', 'rsrv_type_nm']:
                option_dict[key] = option.get(key, '')
        extracted_options.append(option_dict)

    return extracted_products, extracted_options

# fixture 만들기 >> 상품, 옵션
def create_fixture():

    all_extracted_products, all_extracted_options = [], []

    all_data = {}

    for topFinGrpNo in ['020000', '030300']:
        for target in ['depositProductsSearch', 'savingProductsSearch']:
            extracted_products, extracted_options = get_fin_data(topFinGrpNo, target)
            
            all_extracted_products.extend(extracted_products)
            all_extracted_options.extend(extracted_options)
    
    for extracted_data in [all_extracted_products, all_extracted_options]:
        # 모델명 추가하기
        if extracted_data == all_extracted_products:
            model_name = 'financialproduct'
        elif extracted_data == all_extracted_options:
            model_name = 'optionproduct'

        total_data = []
    
        # 키값 바꿔주기
        for data in extracted_data:

            fixture_fields = {}

            for key in data.keys():
                if key == 'fin_co_no':
                    fixture_fields['financial_company_id'] = data[key]

                elif key == 'dcls_month':
                    fixture_fields['published_date'] = data[key]
                
                elif key == 'fin_prdt_cd':
                    if extracted_data == all_extracted_products:
                        fixture_fields['code'] = data[key]
                    elif extracted_data == all_extracted_options:
                        fixture_fields['finance_product_id'] = data[key]

                elif key == 'fin_prdt_nm':
                    fixture_fields['name'] = data[key]

                elif key == 'spcl_cnd':
                    fixture_fields['special_condition'] = data[key]

                elif key == 'mtrt_int':
                    fixture_fields['end_interest_rate'] = data[key]

                elif key == 'dcls_strt_day':
                    fixture_fields['product_start_date'] = data[key]

                elif key == 'dcls_end_day':
                    fixture_fields['product_end_date'] = data[key]

                elif key == 'fin_co_subm_day':
                    fixture_fields['submit_date'] = data[key]

                elif key == 'intr_rate_type':
                    fixture_fields['save_type'] = data[key]

                elif key == 'intr_rate_type_nm':
                    fixture_fields['save_type_name'] = data[key]

                elif key == 'rsrv_type':
                    fixture_fields['reward_type'] = data[key]

                elif key == 'rsrv_type_nm':
                    fixture_fields['reward_type_name'] = data[key]

                elif key == 'save_trm':
                    fixture_fields['save_month'] = data[key]

                elif key == 'intr_rate':
                    fixture_fields['interest_rate'] = data[key]

                elif key == 'intr_rate2':
                    fixture_fields['max_interest_rate'] = data[key]
                
                else:
                    fixture_fields[key] = data[key]
        
            total_data.append(fixture_fields)

        all_data[model_name] = total_data


        print(f'총 {len(total_data)}개의 fixture.{model_name} 항목이 저장되었습니다.')
    
    return all_data


# 전처리하기
def create_finance_data():
    all_data = create_fixture()
    
    product_data = all_data['financialproduct']
    option_data = all_data['optionproduct']

    # 상품 데이터 전처리
    for product in product_data:
        for key in product.keys():
            if key == 'join_deny':
                product[key] = int(product[key])
            
            if key == 'etc_note' or key == 'special_condition':
                if product[key] == '없음':
                    product[key] = None

    # 옵션 데이터 전처리
    for option in option_data:
        for key in option.keys():
            if key == 'save_month':
                option[key] = int(option[key])
    
    product_result_string = json.dumps(product_data)
    product_result = json.loads(product_result_string)

    option_result_string = json.dumps(option_data)
    option_result = json.loads(option_result_string)

    return product_result, option_result
    

# if __name__ == "__main__":
#     product_result, option_result = preprocessing()
#     print(product_result[:5])
#     print(option_result[:5])