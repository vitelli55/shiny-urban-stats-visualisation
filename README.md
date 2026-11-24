# Distrito Federal Statistics Map

My submission for the Maynooth Data Science Society Shiny Competition. 

An interactive data visualisation project exploring demographic, socioeconomic, and household statistics across the Administrative Regions (Regiões Administrativas, RAs) of Brazil's Federal District (Distrito Federal, DF).

The project combines public survey microdata, regional statistics, and geographic boundaries to make differences between regions easier to explore through an interactive map.

## Project goals

-   Process  microdata into regional indicators.
-   Calculate weighted statistics using the appropriate survey weight for each dataset.
-   Combine regional statistics with GeoJSON boundaries for the DF.
-   Present the results through an interactive map, where selecting a region reveals its indicators.
-   Keep data processing separate from the visualisation application so that the statistics can be regenerated independently.

## Current data sources

### PDAD (Pesquisa Distrital por Amostra de Domicílios)

The pipeline works with two separate PDAD datasets:
- `moradores.csv`: Survey of individual residents 
- `domicilios.csv`: Survey of households             

### Census 2022 indicators

The project also includes regional indicators transcribed from a Censo 2022 publication, such as population, demographic density, and average persons per household. These are separate from the PDAD microdata pipeline.

## Pipeline

The pipeline is intended to perform these stages:

1.  **Extraction**: read the PDAD resident and household files and select the configured columns.
2.  **Cleaning**: standardise region identifiers, convert numeric values (including decimal commas), handle missing values, remove documented special codes, and validate configured numeric ranges.
3.  **Statistics**: calculate regional weighted means and weighted categorical frequencies/percentages.
4.  **Loading**: attach the regional results to the corresponding GeoJSON features and export the enriched geographic data.

## Survey weights

Use the weight that corresponds to the unit of observation:

-   `peso_mor` for resident-level statistics.
-   `peso_dom` for household-level statistics.

For a numeric variable (x), the regional weighted mean is:

\[ \\bar{x}\_w = \\frac{\\sum_i w_i x_i}{\\sum_i w_i} \]

For a category (c), the weighted percentage is:

\[ P_w(c) = 100 \\times \\frac{\\sum\_{i \\in c} w_i}{\\sum\_{i \\in
valid} w_i} \]

## Running the visualisation

To be deployed!!