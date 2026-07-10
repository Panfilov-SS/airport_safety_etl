import pandas as pd

def extract_events(path):
    df = pd.read_csv(path)

    return df