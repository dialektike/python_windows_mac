import pandas as pd

temp_url = "https://raw.githubusercontent.com/plotly/datasets/master/auto-mpg.csv"


def load_data():
    try:
        temp = pd.read_csv(temp_url)
    except:
        file_name = "data/mpg_data.json"
        print(f"'{file_name}'를 읽습니다.")
        temp = pd.read_json(file_name, orient="records")
        print(temp.head())
    return temp
