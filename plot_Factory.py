from abc import ABC
import plot_aggregator
import registry

class plot_Factory(plot_aggregator.plot):

	def create(plot_name, data):
############redirect to the model algorithm py file base on yml and registry dictionary file################
		return registry.PlotRegistry[plot_name](data)
		

	def draw(col):
		pass
