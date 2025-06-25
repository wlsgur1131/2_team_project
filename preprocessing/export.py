import pandas as pd

def preprocess_export() -> pd.DataFrame:
    df = pd.read_csv('your_file.csv')
    # 전처리 작업

    # 컬럼명 변경
    df.rename(columns={'수출금액': 'export_amount'}, inplace=True)

    # 'month' 열을 datetime 형식으로 변환하고 'YYYY-MM-DD' 형식으로 변경
    df = df[df['month'].str.contains("월")]
    df['month'] = df['month'].str.replace('년', '-').str.replace('월', '-01')

    return df[["month", "region", "export_amount"]]



