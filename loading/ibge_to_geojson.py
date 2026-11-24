import json
import pandas as pd
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent.parent
CENSUS_DIR = ROOT_DIR / "data" / "df" / "output" / "census"
POPULATION_DIR = CENSUS_DIR / "populacao_por_regiao.csv"
DENSITY_DIR = CENSUS_DIR / "densidade_por_regiao.csv"
HOUSEHOLDS_DIR = CENSUS_DIR / "media_pessoas_por_domicilio_por_regiao.csv"

GEOJSON_DIR = ROOT_DIR / "geojson" / "distrito_federal.geo.json"

with open(GEOJSON_DIR, encoding="utf-8") as f:
    geojson = json.load(f)

population = pd.read_csv(POPULATION_DIR)
density = pd.read_csv(DENSITY_DIR)
households = pd.read_csv(HOUSEHOLDS_DIR)

population_data = population.set_index("regiao")["populacao"].to_dict()
density_data = density.set_index("regiao")["densidade_demografica_hab_km2"].to_dict()
households_data = households.set_index("regiao")["media_pessoas_por_domicilio"].to_dict()

for feature in geojson["features"]:
    region = feature["id"]

    if not pd.isna(population_data.get(region)):
        feature["properties"]["population"] = round(population_data.get(region))
    if not pd.isna(density_data.get(region)):
        feature["properties"]["demographic_density"] = round(density_data.get(region))
    if not pd.isna(households_data.get(region)):
        feature["properties"]["avg_household_size"] = (households_data.get(region))

# Export updated GeoJSON
with open(GEOJSON_DIR, "w", encoding="utf-8") as f:
    json.dump(geojson, f, ensure_ascii=False, indent=2)