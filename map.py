import webbrowser
import numpy as np
import math
import os
import gmplot
import functools
import AlgorithmFactory
from plot_aggregator import plot

# mport plot_aggregator
import ipywidgets as widgets
from ipywidgets import interact, interactive, fixed, interact_manual


button = widgets.Button(description="Click Me!")
api = widgets.Text(description='api:')
buttonClick = False
class MapPlot(plot):

        map_data_mod = {}
        city = ""
        slider = ""
        pin = ""
        api = ""
        slider = widgets.IntSlider(value = 30, min = 5, max = 50, step = 5, 
                              description = "clusters num", continuous_update=False, readout = True)
        def __init__(self, map_data):
            
            
            self.map_data_mod = map_data
            self.map_data_mod['CMPLNT_FR_TM'] = self.map_data_mod['CMPLNT_FR_TM'].str.split(':').str[0]
            self.map_data_mod['CMPLNT_FR_DT'] = self.map_data_mod['CMPLNT_FR_DT'].str.split('/').str[0] + '/' + self.map_data_mod['CMPLNT_FR_DT'].str.split('/').str[2]

            self.map_data_mod = self.map_data_mod.loc[(self.map_data_mod['CMPLNT_FR_DT'].str.split('/').str[1] == '2018'
            self.map_data_mod = self.map_data_mod.loc[(self.map_data_mod['CMPLNT_FR_DT'].str.split('/').str[0] == '08')]     
            
            print(self.map_data_mod)
            
        
        def draw(self, col):
            def setbuttonclick(b, city="", slider = "", pin="", api=""):
                city = self.city
                slider = self.slider
                pin = self.pin
                api = self.api
                global buttonClick
                if api == "":
                    buttonClick = True
                    return
              
                curr_data = self.map_data_mod
                first_place = "New York, USA"
                if city != 'ALL':
                    curr_data = curr_data.loc[curr_data['BORO_NM'] == city]
                    first_place = city + ", USA"
                min_num = len(curr_data)
                min_num = min(1000, len(curr_data))
                curr_data = curr_data.sample(n = min_num, replace = False)
                coords = np.array(curr_data[['Latitude', 'Longitude']], dtype='float64')
                mask = np.any(np.isnan(coords) | np.equal(coords, 0), axis=1)
                coords[~mask]
                for i in range(len(coords)):
                    if math.isnan (coords[i][1]):
                        print(i)
                        print(coords[i])
                        print('have null')
                up = slider
                Ks = range(1, up)
                algorithmFactory = AlgorithmFactory.AlgorithmFactory.create("kmean")
                
                kmean = algorithmFactory.calculate(up, Ks, coords)
                lat_list = []
                long_list = []

                for i in range(len(kmean)):
                    lat_list.append(kmean[up - 2].cluster_centers_[i][0])
                    long_list.append(kmean[up - 2].cluster_centers_[i][1])

                apikey = str(api)
                gmap = gmplot.GoogleMapPlotter.from_geocode("New York, USA", apikey=apikey)

                if pin == "HEAT":
                    gmap.heatmap( lat_list, long_list, radius = 15)
                else:
                    gmap.scatter(lat_list, long_list, "cornflowerblue")
                gmap.draw('map.html')

                filename = 'file:///'+os.getcwd()+'/' + 'map.html'
                webbrowser.open_new_tab(filename)
                buttonClick = False
            @interact
            def map_plot(city = (['ALL', 'BRONX', 'BROOKLYN', 'MANHATTAN', 'QUEENS', 'STATEN ISLAND']), 
                                      pin = (['HEAT', 'SCATTER']), 
                                       slider = self.slider, api = api):
                self.city = city
                self.slider = slider
                self.pin = pin
                self.api = api
                display(button)
            button.on_click(functools.partial(setbuttonclick, city=self.city, slider = self.slider, pin=self.pin, api=self.api))
                
                
                
                