import pandas as pd
import map


# map_data = pd.read_csv('NYPD_Complaint_Data_Current__Year_To_Date_1.csv')
map_data = pd.read_csv('NYPD_Complaint_Data_Historic.csv')
mapPlot = map.MapPlot()
plotname = "abc"
col = "abc"
mapPlot.create(plotname, map_data)
mapPlot.draw(col)