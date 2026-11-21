#vibe-coded script to combine all seperate region files into 1 single file for better loading

import json
from pathlib import Path

# Directory containing the individual GeoJSON files
data_dir = Path("geojson-data/divided-files")

combined = {
    "type": "FeatureCollection",
    "features": []
}

# Iterate through every .geo.json file
for file in sorted(data_dir.glob("*.geo.json")):

    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Handle files containing a single Feature
    if data["type"] == "Feature":
        combined["features"].append(data)

    # Handle files containing multiple Features
    elif data["type"] == "FeatureCollection":
        combined["features"].extend(data["features"])

    else:
        raise ValueError(f"Unsupported GeoJSON type in {file}")

# Save the combined GeoJSON
with open("distrito_federal.geo.json", "w", encoding="utf-8") as f:
    json.dump(combined, f, ensure_ascii=False, indent=4)