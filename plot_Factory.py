from abc import ABC
import plot_aggregator
#from registry import ModelRegistry

class plot_Factory(plot_aggregator.plot):

	def create(plot_name, **params):
############redirect to the model algorithm py file base on yml and registry dictionary file################
		#return ModelRegistry[model_name](**params)
		

	def draw():
		pass
