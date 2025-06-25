import pandas as pd

def preprocess_power() -> pd.DataFrame:
    df = pd.read_csv("your_file.csv")
    # 전처리 작업
    
    # '시군구' 열 제거
    if '시군구' in df.columns:
        df = df.drop(columns=['시군구'])

    # 컬럼명 변경
    df = df.rename(columns={
        '년월': 'month',
        '시구': 'region',
        '사용량(kWh)': 'power_kwh',
        '계약구분': 'division',
        '고객호수(호)': 'client_num',
        '전기요금(원)': 'price',
        '평균판매단가(원/kWh)': 'mean_price_kwh'
    })
    
    # 'month'를 datetime(YYYY-MM-01) 형식으로 변환
    df['month'] = pd.to_datetime(df['month'].astype(str) + '-01')

    # 시도명 매핑용 딕셔너리 정의
    region_mapping = {
        '강원특별자치도': '강원',
        '경기도': '경기',
        '경상남도': '경남',
        '경상북도': '경북',
        '광주광역시': '광주',
        '대구광역시': '대구',
        '대전광역시': '대전',
        '부산광역시': '부산',
        '서울특별시': '서울',
        '울산광역시': '울산',
        '인천광역시': '인천',
        '전라남도': '전남',
        '전라북도': '전북',
        '제주특별자치도': '제주',
        '충청남도': '충남',
        '충청북도': '충북',
        '세종특별자치시': '세종'
    }
    # 'region' 값 매핑
    df['region'] = df['region'].map(region_mapping).fillna(df['region'])

    # 'division'이 '산업용'인 행만 남김
    df = df[df['division'] == '산업용']

    # 원하는 열 반환
    return df[["month", "region", "power_kwh"]]
