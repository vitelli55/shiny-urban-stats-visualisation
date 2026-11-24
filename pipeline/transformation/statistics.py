import pandas as pd

def _label(code, labels):
    if pd.isna(code):
        return None
    integer_code = int(code)
    return labels.get(integer_code, f"Código {integer_code} (rótulo não configurado)")

def calculate_numeric_statistics(df, variables, region_column, weight_column):
    rows = []
    for variable, spec in variables.items():
        if spec["kind"] != "numeric":
            continue
        column = spec["column"]
        valid = df[[region_column, weight_column, column]].dropna()
        for region, group in valid.groupby(region_column):
            weight_sum = group[weight_column].sum()
            if weight_sum <= 0:
                continue
            weighted_mean = (group[column] * group[weight_column]).sum() / weight_sum
            rows.append({
                "localidade": str(region),
                "variable": variable,
                "description": spec["description"],
                "unit": spec.get("unit", ""),
                "weighted_mean": weighted_mean,
                "weighted_population_estimate": weight_sum,
                "sample_n": len(group),
            })
    return pd.DataFrame(rows)

def calculate_categorical_statistics(
    df, variables, region_column, weight_column, min_cell_size
):
    rows = []
    for variable, spec in variables.items():
        if spec["kind"] != "categorical":
            continue
        column = spec["column"]
        valid = df[[region_column, weight_column, column]].dropna()
        labels = spec.get("labels", {})

        for region, region_group in valid.groupby(region_column):
            denominator = region_group[weight_column].sum()
            if denominator <= 0:
                continue
            for code, group in region_group.groupby(column):
                sample_n = len(group)
                suppressed = sample_n < min_cell_size
                weighted_n = group[weight_column].sum()
                rows.append({
                    "localidade": str(region),
                    "variable": variable,
                    "description": spec["description"],
                    "code": int(code),
                    "label": _label(code, labels),
                    "sample_n": None if suppressed else sample_n,
                    "weighted_frequency": None if suppressed else weighted_n,
                    "weighted_percentage": (
                        None if suppressed else 100 * weighted_n / denominator
                    ),
                    "suppressed": suppressed,
                    "valid_weight_denominator": denominator,
                })
    return pd.DataFrame(rows)

def calculate_all_statistics(df, variables, region_column, weight_column, min_cell_size):
    numeric = calculate_numeric_statistics(df, variables, region_column, weight_column)
    categorical = calculate_categorical_statistics(
        df, variables, region_column, weight_column, min_cell_size
    )
    return numeric, categorical
