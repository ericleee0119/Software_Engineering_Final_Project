from plot_aggregator import plot
import matplotlib.pyplot as plt
import seaborn as sns
import registry

class line_chart(plot):
	def __init__(self, data_mod):
		print(data_mod)
		data_mod['CMPLNT_FR_TM'] = data_mod['CMPLNT_FR_TM'].str.split(':').str[0]
		data_mod['month'] = data_mod['CMPLNT_FR_DT'].str.split('/').str[0]
		data_mod['CMPLNT_FR_DT'] = data_mod['CMPLNT_FR_DT'].str.split('/').str[2]

		#print(data_mod)
		data_mod = data_mod.loc[(data_mod['CMPLNT_FR_DT'] == '2012') | (data_mod['CMPLNT_FR_DT'] == '2013') |
		                        (data_mod['CMPLNT_FR_DT'] == '2014') | (data_mod['CMPLNT_FR_DT'] == '2015') |
		                        (data_mod['CMPLNT_FR_DT'] == '2016') | (data_mod['CMPLNT_FR_DT'] == '2017') |
		                        (data_mod['CMPLNT_FR_DT'] == '2018') | (data_mod['CMPLNT_FR_DT'] == '2019') |
		                        (data_mod['CMPLNT_FR_DT'] == '2020') | (data_mod['CMPLNT_FR_DT'] == '2021')]
		print(data_mod)
		self.curr_data = data_mod

		##############use previous created data generate plot###############
	def draw(self, col):
		#print(self.curr_data)
		ax = plt.subplots(figsize=(15, 10))
		print(col)
		print(self.curr_data)
		ax=sns.countplot(x=col, data=self.curr_data, order= registry.ColRegistry[col])
		ax.set_xticklabels(ax.get_xticklabels(), rotation=90, ha="right")
		plt.tight_layout()
		plt.show()
