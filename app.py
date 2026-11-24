from shiny import reactive, App, ui, render
from shinywidgets import output_widget, render_widget
import ipyleaflet as ipyl

import os
import json
from pathlib import Path
import random

#loading geojson data
REGIONS_PATH = Path("geojson/distrito_federal.geo.json")
with open(REGIONS_PATH, "r", encoding="utf-8") as f:
   geodata = json.load(f)

DF_COORDS = (-15.807616488540408, -47.9509412304779)

region_info = reactive.value({})


# --------- UI

#app_ui = ui.page_fillable(
app_ui = ui.page_navbar(
    # HOME PANEL
    # Current issue: map and sidebar only occupy a small section of the screen
    ui.nav_panel(
        "Home",
        ui.layout_sidebar(
            ui.sidebar(
                ui.output_ui("region_info_display"),

                width="300px",
                open="closed",
                id="info_sidebar",
            ),

            output_widget("map", width="100%", height="100%"),

            fillable=True,
        )),
        ui.nav_panel("Extra", "WIP"),
        fillable=True


)

# ------------- HELPER FUNCTIONS

def random_color(feature):
    return {
        'color': 'black',
        'fillColor': random.choice(['red', 'yellow', 'green', 'orange', 'blue', 'purple', 'pink']),
    }



# ------------- SERVER

def server(input, output, session):

    @render.ui
    def region_info_display():
        selected_region = region_info.get() # dictionary of the properties of selected region

        name = selected_region['name']

        population = selected_region['population']
        demographic_density = selected_region['demographic_density']
        avg_household_size = selected_region['avg_household_size']

        VALUE_BOX_HEIGHT = "150px"

        display = ui.TagList(
            ui.h3(name),
            ui.value_box("Population", f"{population} people", theme='blue', fill=True, height=VALUE_BOX_HEIGHT),
            ui.value_box("Pop. Density", f"{demographic_density} people per km^2", theme='cyan',fill=True, height=VALUE_BOX_HEIGHT),
            ui.value_box("Avg. Household Size", f"{avg_household_size} people",theme='teal', fill=True, height=VALUE_BOX_HEIGHT),

        )

        return display



    def handle_click(**kwargs): #kwargs allows passing a variable number of keyword args to a function

        properties = kwargs.get("properties", {})
        coords = kwargs.get("coordinates", {})


        print("Selected:", properties)
        #print(kwargs.keys())
        
        region_info.set(properties)
        map.widget.center = coords
        
    
        if input.info_sidebar() is False:
            #print("sidebar is closed")
            ui.update_sidebar("info_sidebar", show=True)

        
        

    @render_widget
    def map():
        m = ipyl.Map(
            center = DF_COORDS, 
            zoom=10.5,
            scroll_wheel_zoom = True,
            #min_zoom = 1000
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