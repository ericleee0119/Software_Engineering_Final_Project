from plot_aggregator import plot
import matplotlib.pyplot as plt
import seaborn as sns
import registry

class line_chart(plot):
	def __init__(self, data):
		self.curr_data = data

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
