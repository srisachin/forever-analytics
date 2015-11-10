import PlotObj;
import seaborn as sns;
import matplotlib.pyplot as plt
import matplotlib
import Genplots
import pandas as pd
import settings


class BarPlot(PlotObj.PlotObj):
#	def __init__(self,exp):
	def plotExp(self,exp,myData):
		plt.figure();
#		print (exp[1]['xaxis'])
		g=sns.countplot(myData[exp[1]['xaxis']]);
		plt.savefig("/home/sachin/Documents/forever/plots/%d.jpg" %settings.count);
		plt.clf()
		plt.close()
		settings.count=settings.count+1;

	def check(self,myStr):
		return myStr=="barcount"