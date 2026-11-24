import pandas as pd

def _to_number(series):
    return pd.to_numeric(
        series.astype(str).str.strip().str.replace(",", ".", regex=False),
        errors="coerce",
    )

def clean_dataset(df, variables, region_column, weight_column):
    cleaned = df.copy()
    cleaned[region_column] = cleaned[region_column].astype(str).str.strip()
    cleaned.loc[cleaned[region_column].isin(["", "nan", "None"]), region_column] = pd.NA

    cleaned[weight_column] = _to_number(cleaned[weight_column])
    cleaned.loc[cleaned[weight_column] <= 0, weight_column] = pd.NA

    for spec in variables.values():
        column = spec["column"]
        values = _to_number(cleaned[column])
        special_codes = set(spec.get("special_codes", []))

        special_mask = values.isin(special_codes)
        cleaned[column] = values.mask(special_mask)

        if spec["kind"] == "numeric":
            # no special codes that are not in the dictionary.
            # values ​​falling outside the configured range are removed 
            low = spec.get("valid_min")
            high = spec.get("valid_max")
            invalid = cleaned[column].notna()
            if low is not None:
                invalid &= cleaned[column] < low
            if high is not None:
                invalid |= cleaned[column].notna() & (cleaned[column] > high)
            invalid_count = int(invalid.sum())
            cleaned.loc[invalid, column] = pd.NA
        else:
            invalid_count = 0

    return cleaned
