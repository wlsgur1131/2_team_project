import pandas as pd

def preprocess_production() -> pd.DataFrame:
    df = pd.read_csv("your_file.csv")
    # 전처리 작업
    
    # 컬럼명 변경
    df = df.rename(columns={
        "시도-공업구조별": "region",
        "시점": "month",
        "생산지수(원지수)": "prod_index"
    })
    
    #첫 번째 행 제거
    df = df.drop(index=0)
    df.columns = df.iloc[0]
    df = df[1:]

    # "month"를 datetime 형식으로 변환
    df["month"] = df["month"].str.extract(r"(\d{4}\.\d{2})")[0]
    df["month"] = pd.to_datetime(df["month"], format="%Y.%m")

    return df[["month", "region", "prod_index"]]
