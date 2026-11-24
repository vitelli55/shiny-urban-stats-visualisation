"""Exportação dos resultados e enriquecimento opcional do GeoJSON."""

import pandas as pd
import geopandas as gpd

def export_geojson(numeric_stats, categorical_stats, geojson_path, output_path):
    
    regions = gpd.read_file(geojson_path)
    if "localidade" not in regions.columns:
        raise ValueError(
            "O GeoJSON precisa ter uma coluna 'localidade' com o mesmo código "
            "usado em moradores.csv. Ajuste o nome/chave antes do merge."
        )

    regions["localidade"] = regions["localidade"].astype(str).str.strip()

    # Colunas numéricas: uma coluna por variável, por região.
    if not numeric_stats.empty:
        numeric_wide = numeric_stats.pivot(
            index="localidade", columns="variable", values="weighted_mean"
        ).reset_index()
        regions = regions.merge(numeric_wide, on="localidade", how="left")

    # Distribuições categóricas ficam em CSV (formato longo), porque colocá-las
    # todas como propriedades GeoJSON criaria muitas colunas.
    regions.to_file(output_path, driver="GeoJSON")
