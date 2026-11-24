import pandas as pd

def read_pdad_csv(path):
    return pd.read_csv(
        path,
        sep=None,
        engine="python",
        encoding="utf-8-sig",
        dtype=str,
        keep_default_na=False,
    )

def extract_columns(path, variables, region_column, weight_column):
    df = read_pdad_csv(path)

    required = {region_column, weight_column}
    required.update(spec["column"] for spec in variables.values())

    missing = sorted(required - set(df.columns))
    if missing:
        raise ValueError(f"Missing columns in {path}: {missing}")

    columns = [region_column, weight_column]
    columns += [spec["column"] for spec in variables.values()]
    columns = list(dict.fromkeys(columns))

    return df[columns].copy()
