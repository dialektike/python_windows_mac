import pandas as pd

temp_url = "https://raw.githubusercontent.com/plotly/datasets/master/auto-mpg.csv"


def load_data():
    temp = pd.read_csv(temp_url)
    print(temp.head())
    return temp
