import pandas as pd

def load_data():
    """Load COVID-19 data from local CSV file."""
    df = pd.read_csv("data/covid_data.csv")
    df["Date"] = pd.to_datetime(df["Date"])
    return df
