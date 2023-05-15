import line_chart
import histogram_chart
import map

PlotRegistry= {
'line_plot' : line_chart.plot_chart,
'histogram_plot' : histogram_chart.line_chart
'map_plot' : map.map_plot
}


ColRegistry = {
'CMPLNT_FR_DT' : ['2012','2013','2014', '2015','2016', '2017', '2018', '2019', '2020', '2021'],
'month' : ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
'CMPLNT_FR_TM' : ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12','13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']
}