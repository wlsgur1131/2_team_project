import pandas as pd

def preprocess_weather() -> pd.DataFrame:
    df = pd.read_csv("your_file_path.csv")
    # 전처리 작업

    # 컬럼명 변경
    df.rename(columns={
        '지역명': 'region',
        '일시': 'month',
        '평균기온(℃)': 'temp_avg'
    }, inplace=True)
    
    return df[["month", "region", "temp_avg"]]