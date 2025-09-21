import pandas as pd
import pytest
from src.filters import filter_by_values

def test_filter_by_values_ok():
    df = pd.DataFrame({"counter_name":["A","B","A"], "bike_count":[1,2,3]})
    out = filter_by_values(df, "counter_name", ["A"])
    assert set(out["counter_name"].unique()) == {"A"}
    assert out["bike_count"].sum() == 4

def test_filter_by_values_bad_col():
    df = pd.DataFrame({"x":[1,2]})
    with pytest.raises(KeyError):
        filter_by_values(df, "missing", [1])
