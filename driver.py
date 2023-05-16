import pandas as pd
import map


# map_data = pd.read_csv('NYPD_Complaint_Data_Current__Year_To_Date_1.csv')
map_data = pd.read_csv('test_data.csv')
mapPlot = map.MapPlot()
plotname = "map_plot"
col = "abc"
mapPlot.create(plotname, map_data)
mapPlot.draw(col)