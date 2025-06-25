import pandas as pd

def preprocess_precipitation() -> pd.DataFrame:
    df = pd.read_csv("your_file_path.csv")
    # 전처리 작업

    # 컬럼명 변경
    df.rename(columns={
        '지역명': 'region',
        '일시': 'month',
        '평균월강수량(mm)': 'precipitation'
    }, inplace=True)

    # month 열을 datetime 형식으로 변환하고 'YYYY-MM-DD' 형식으로 변경
    df['일시'] = pd.to_datetime(df['일시']).dt.strftime('%Y-%m-%d')
    
    return df[["month", "region", "precipitation"]]