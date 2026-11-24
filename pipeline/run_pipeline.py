"""extract -> clean -> stats -> export."""
"""moradores.csv = residents survey, domicilios.csv = household survey"""

import logging
from pipeline.config import (
    REGION_COLUMN, MIN_CELL_SIZE, PROCESSED_DIR, OUTPUT_DIR,
    MORADORES_FILE, MORADORES_VARIABLES, MOR_WEIGHT_COLUMN,
    DOMICILIOS_FILE, DOMICILIO_VARIABLES, DOM_WEIGHT_COLUMN,
)
from pipeline.extraction.extract_pdad import extract_columns
from pipeline.transformation.clean import clean_dataset
from pipeline.transformation.statistics import calculate_all_statistics

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)
logger = logging.getLogger(__name__)

def run_pipeline():
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    #---------------- moradores.csv

    logger.info("Reading moradores.csv")
    moradores = extract_columns(MORADORES_FILE, MORADORES_VARIABLES, REGION_COLUMN, MOR_WEIGHT_COLUMN)
    logger.info("Residents surveyed: %s", f"{len(moradores):,}")

    logger.info("Cleaning variables and weightage for moradores.csv")
    mor_cleaned = clean_dataset(moradores, MORADORES_VARIABLES, REGION_COLUMN, MOR_WEIGHT_COLUMN)
    mor_cleaned.to_parquet(PROCESSED_DIR / "moradores_cleaned.parquet", index=False)

    logger.info("Calculating statistics for moradores.csv")
    mor_numeric, mor_categorical = calculate_all_statistics(mor_cleaned, MORADORES_VARIABLES, REGION_COLUMN, MOR_WEIGHT_COLUMN, MIN_CELL_SIZE)
    mor_numeric.to_csv(
        OUTPUT_DIR / "moradores_numeric_statistics.csv",
        index=False, encoding="utf-8-sig",
    )
    mor_categorical.to_csv(
        OUTPUT_DIR / "moradores_categorical_distributions.csv",
        index=False, encoding="utf-8-sig",
    )

    # ----------- domicilios.csv

    logger.info("Reading domicilios.csv")
    domicilios = extract_columns(DOMICILIOS_FILE, DOMICILIO_VARIABLES, REGION_COLUMN, DOM_WEIGHT_COLUMN)
    logger.info("Households surveyed: %s", f"{len(domicilios):,}")

    logger.info("Cleaning variables and weightage for domicilios.csv")
    dom_cleaned = clean_dataset(domicilios, DOMICILIO_VARIABLES, REGION_COLUMN, DOM_WEIGHT_COLUMN)
    dom_cleaned.to_parquet(PROCESSED_DIR / "domicilios_cleaned.parquet", index=False)

    logger.info("Calculating statistics for moradores.csv")
    dom_numeric, dom_categorical = calculate_all_statistics(dom_cleaned, DOMICILIO_VARIABLES, REGION_COLUMN, DOM_WEIGHT_COLUMN, MIN_CELL_SIZE)
    dom_numeric.to_csv(
        OUTPUT_DIR / "domicilios_numeric_statistics.csv",
        index=False, encoding="utf-8-sig",
    )
    dom_categorical.to_csv(
        OUTPUT_DIR / "domicilios_categorical_distributions.csv",
        index=False, encoding="utf-8-sig",
    )

    #---------------- 
    logger.info("Pipeline completed. Results in %s", OUTPUT_DIR)

if __name__ == "__main__":
    run_pipeline()
