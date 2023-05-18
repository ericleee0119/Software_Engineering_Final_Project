from plot_aggregator import plot
import matplotlib.pyplot as plt
import seaborn as sns
import registry


class plot_chart(plot):

	def __init__(self, data_mod):
		data_mod['CMPLNT_FR_TM'] = data_mod['CMPLNT_FR_TM'].str.split(':').str[0]
		data_mod['month'] = data_mod['CMPLNT_FR_DT'].str.split('/').str[0]
		data_mod['CMPLNT_FR_DT'] = data_mod['CMPLNT_FR_DT'].str.split('/').str[2]

		#print(data_mod)
		data_mod = data_mod.loc[(data_mod['CMPLNT_FR_DT'] == '2012') | (data_mod['CMPLNT_FR_DT'] == '2013') |
		                        (data_mod['CMPLNT_FR_DT'] == '2014') | (data_mod['CMPLNT_FR_DT'] == '2015') |
		                        (data_mod['CMPLNT_FR_DT'] == '2016') | (data_mod['CMPLNT_FR_DT'] == '2017') |
		                        (data_mod['CMPLNT_FR_DT'] == '2018') | (data_mod['CMPLNT_FR_DT'] == '2019') |
		                        (data_mod['CMPLNT_FR_DT'] == '2020') | (data_mod['CMPLNT_FR_DT'] == '2021')]
		self.curr_data = data_mod

	##############use previous created data generate plot###############
	def draw(self, col):
		line_chart = plt.subplots(figsize=(15, 10))

		#['CMPLNT_NUM', 'CMPLNT_FR_DT', 'CMPLNT_FR_TM', 'CMPLNT_TO_DT', 'CMPLNT_TO_TM', 'ADDR_PCT_CD', 'RPT_DT', 'KY_CD', 'OFNS_DESC', 'PD_CD', 'PD_DESC', 'CRM_ATPT_CPTD_CD', 'LAW_CAT_CD', 'BORO_NM', 'LOC_OF_OCCUR_DESC', 'PREM_TYP_DESC', 'JURIS_DESC', 'JURISDICTION_CODE', 'PARKS_NM', 'HADEVELOPT', 'HOUSING_PSA', 'X_COORD_CD', 'Y_COORD_CD', 'SUSP_AGE_GROUP', 'SUSP_RACE', 'SUSP_SEX', 'TRANSIT_DISTRICT', 'Latitude', 'Longitude', 'Lat_Lon', 'PATROL_BORO', 'STATION_NAME', 'VIC_AGE_GROUP', 'VIC_RACE', 'VIC_SEX'] 
		temp = self.curr_data.groupby(col).size().reset_index(name='count')
		line_chart = sns.lineplot(data=temp, x=col,y = 'count', sort=True)


		plt.show()



