import pandas as pd
from src.data_io import load_parquet_with_time_features

def test_time_features(tmp_path):
    p = tmp_path / "mini.parquet"
    df = pd.DataFrame({
        "date": pd.to_datetime(["2024-01-01 08:00","2024-01-01 09:00"]),
        "bike_count": [10, 20]
    })
    df.to_parquet(p, index=False)
    out = load_parquet_with_time_features(str(p))
    assert {"year","month","day","hour","weekday_idx"}.issubset(out.columns)
    assert out["bike_count"].sum() == 30
