import pandas as pd
import plot_Factory as PF
from registry import ColRegistry

data = pd.read_csv('test_data.csv')
data_mod = data
'''
data_mod['CMPLNT_FR_TM'] = data_mod['CMPLNT_FR_TM'].str.split(':').str[0]
data_mod['month'] = data_mod['CMPLNT_FR_DT'].str.split('/').str[0]
data_mod['CMPLNT_FR_DT'] = data_mod['CMPLNT_FR_DT'].str.split('/').str[2]



data_mod = data_mod.loc[(data_mod['CMPLNT_FR_DT'] == '2012') | (data_mod['CMPLNT_FR_DT'] == '2013') |
                        (data_mod['CMPLNT_FR_DT'] == '2014') | (data_mod['CMPLNT_FR_DT'] == '2015') |
                        (data_mod['CMPLNT_FR_DT'] == '2016') | (data_mod['CMPLNT_FR_DT'] == '2017') |
                        (data_mod['CMPLNT_FR_DT'] == '2018') | (data_mod['CMPLNT_FR_DT'] == '2019') |
                        (data_mod['CMPLNT_FR_DT'] == '2020') | (data_mod['CMPLNT_FR_DT'] == '2021')]
'''
#city = (['ALL', 'BRONX', 'BROOKLYN', 'MANHATTAN', 'QUEENS', 'STATEN ISLAND']), 

def test_histogram():
    plot1 = PF.plot_Factory.create('histogram_plot', data_mod)
    plot1.draw('month')

def test_linechart():
    plot2 = PF.plot_Factory.create('line_plot', data_mod)
    plot2.draw('month')

'''
def test_map():
    plot2 = PF.plot_Factory.create('map_plot', data_mod)
    plot2.draw('month')
'''
'''
for generate line plot 
$$ plot1 = PF.plot_Factory.create('line_plot', data_mod)
$$ plot1.draw('month')

for generate histogram plot
$$ plot1 = PF.plot_Factory.create('histogram_plot', data_mod)
$$ plot1.draw('month')

for order by month
$$ plot1.draw('month')

for order by year
$$ plot1.draw('CMPLNT_FR_DT')

for order by time of day
$$ plot1.draw('CMPLNT_FR_TM')

'''