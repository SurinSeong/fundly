import os
from django.conf import settings

# 쉼표 제거 + 숫자인지 확인 후 float 변환
def clean_to_float(value):
    try:
        return float(str(value).replace(',', ''))
    except ValueError:
        return None  # 이상값은 None 처리


def preprocessing(spot_type):
    
    # 엑셀 데이터 불러오기
    file_path = os.path.join(settings.BASE_DIR, 'finance', 'data', f'{spot_type}_prices.xlsx') 
    df = pd.read_excel(file_path, sheet_name=f'{spot_type}')

    # 필요한 컬럼만 추출 및 컬럼명 정리
    df = df[['Date', 'Open', 'High', 'Low', 'Close/Last', 'Volume']]
    df.columns = ['date', 'open_price', 'high_price', 'low_price', 'close_price', 'volume']

    # 쉼표 제거 + float 변환
    for col in ['open_price', 'high_price', 'low_price', 'close_price', 'volume']:
        df[col] = df[col].apply(clean_to_float)
        df[col] = df[col].astype(str).str.replace(',', '').astype(float)
        

    # 결측치 제거 및 날짜형 변환
    df = df.dropna()
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df = df.dropna(subset=['date'])  # 날짜 오류 있는 행 제거

    
    return df


