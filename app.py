from shiny import reactive, App, ui
#from shiny.express import input, ui
from shinywidgets import output_widget, render_widget
import ipyleaflet as ipyl

import os
import json
from pathlib import Path
import random

#loading geojson data
REGIONS_PATH = Path("geojson-data/distrito_federal.geo.json")
with open(REGIONS_PATH, "r", encoding="utf-8") as f:
   geodata = json.load(f)


DF_COORDS = (-15.807616488540408, -47.9509412304779)


# app_ui = ui.page_sidebar(
    
#     ui.sidebar(
#         ui.h3("Info"),
#             ),
            

#     output_widget("map", width="100%", height="100%"),
    
# )

# app_ui = ui.page_fillable(

#     output_widget("map", width="100%", height="100%"),
# )

app_ui = ui.page_fillable(

    ui.layout_sidebar(

        ui.sidebar(
            ui.h3("Info"),
            width="300px",
            open="closed",
        ),

        output_widget("map", width="100%", height="100%"),

        fillable=True,
    )

)




def random_color(feature):
    return {
        'color': 'black',
        'fillColor': random.choice(['red', 'yellow', 'green', 'orange']),
    }

def handle_click(**kwargs): #kwargs allows passing a variable number of keyword args to a function
    properties = kwargs.get("properties", {})
    print("Selected:", properties)

def server(input, output, session):

    @render_widget
    def map():
        m = ipyl.Map(
            center = DF_COORDS, 
            zoom=10.5,
            scroll_wheel_zoom = True
            )


        geo_layer = ipyl.GeoJSON(
            data=geodata, 
            style={
                'opacity': 0.6, 'fillOpacity': 0.3, 'weight': 1
            },
            hover_style={
                'color': 'white', 'dashArray': '0', 'fillOpacity': 0.5
            },
            style_callback=random_color
        )
        m.add(geo_layer)
        geo_layer.on_click(handle_click)

        m.layout.width = "100%"
        m.layout.height = "100%"
       # 

        return m


    @reactive.effect
    def _():
        map.widget.center = DF_COORDS #city_centers[input.center()]

app = App(app_ui, server)