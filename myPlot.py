#!/usr/bin/env python
import matplotlib.pyplot as plt
import csv

__author__ = "Dan Rugeles"
__copyright__ = "Copyright 2013, Accelerometrics"
__credits__ = ["Dan Rugeles"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Dan Rugeles"
__email__ = "danrugeles@gmail.com"
__status__ = "Production"

#--CSVCol------------------------------------------------------
"""Plots the selected column from the selected csv file

filename: String representing path to csv file
col: integer representing the column of the csv file"""
#---------------------------------------------------------------
def CSVCol(filename,col):

	with open(filename,"r") as f:
		alldata=csv.reader(f,delimiter=",")
		plotdata=[]
		for row in alldata:
			plotdata.append(row[col])
	
	plt.plot(plotdata, 'r-')
	#plt.xticks(range(len(b)), b, rotation="vertical",size='small')
	plt.title(filename+", col:"+str(col))
	plt.ylabel("Y label")
	plt.grid(True)
	plt.show()

"""----------------------------*
*                              *
*   |\  /|   /\    |  |\  |    * 
*   | \/ |  /__\   |  | \ |    *
*   |    | /    \  |  |  \|    *
*                              *
*----------------------------"""
if __name__=="__main__":

	CSVCol("user2.csv",-1)
	CSVCol("user6.csv",-1)
	CSVCol("user80.csv",-1)
	CSVCol("user280.csv",-1)

	
	
	

