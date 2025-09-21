import pandas as pd

def load_parquet_with_time_features(path: str) -> pd.DataFrame:
    df = pd.read_parquet(path)  # requires fastparquet or pyarrow
    for col in ["date","bike_count"]:
        if col not in df.columns:
            raise KeyError(f"Missing required column: {col}")
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month
    df["day"] = df["date"].dt.date
    df["hour"] = df["date"].dt.hour
    df["weekday_idx"] = df["date"].dt.dayofweek
    df["bike_count"] = pd.to_numeric(df["bike_count"], errors="coerce")
    return df
