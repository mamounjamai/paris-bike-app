import pandas as pd

def filter_by_values(df: pd.DataFrame, col: str, values: list) -> pd.DataFrame:
    if col not in df.columns:
        raise KeyError(f"{col} not in DataFrame")
    return df[df[col].isin(values)]
