from plot_aggregator import plot
import matplotlib.pyplot as plt
import seaborn as sns
import registry


class plot_chart(plot):

	def __init__(self, data):
		self.curr_data = data

	##############use previous created data generate plot###############
	def draw(self, col):
		line_chart = plt.subplots(figsize=(15, 10))

		#['CMPLNT_NUM', 'CMPLNT_FR_DT', 'CMPLNT_FR_TM', 'CMPLNT_TO_DT', 'CMPLNT_TO_TM', 'ADDR_PCT_CD', 'RPT_DT', 'KY_CD', 'OFNS_DESC', 'PD_CD', 'PD_DESC', 'CRM_ATPT_CPTD_CD', 'LAW_CAT_CD', 'BORO_NM', 'LOC_OF_OCCUR_DESC', 'PREM_TYP_DESC', 'JURIS_DESC', 'JURISDICTION_CODE', 'PARKS_NM', 'HADEVELOPT', 'HOUSING_PSA', 'X_COORD_CD', 'Y_COORD_CD', 'SUSP_AGE_GROUP', 'SUSP_RACE', 'SUSP_SEX', 'TRANSIT_DISTRICT', 'Latitude', 'Longitude', 'Lat_Lon', 'PATROL_BORO', 'STATION_NAME', 'VIC_AGE_GROUP', 'VIC_RACE', 'VIC_SEX'] 
		temp = self.curr_data.groupby(col).size().reset_index(name='count')
		print(temp)
		line_chart = sns.lineplot(data=temp, x=col,y = 'count', sort=True)


		plt.show()



