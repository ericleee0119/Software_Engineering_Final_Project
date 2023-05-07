from aggregator_line_chart import plot
import matplotlib.pyplot as plt
import seaborn as sns
import registry

class line_chart(plot):
	def __init__(self, plot):
		
	def draw(col):
		ax=sns.countplot(x=col, data=self.curr_data, order= HistogramRegistry[col])
		ax.set_xticklabels(ax.get_xticklabels(), rotation=90, ha="right")
		plt.show()
