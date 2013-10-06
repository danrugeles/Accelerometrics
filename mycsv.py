#!/usr/bin/env python
import csv
from mysys import *
import numpy as np

__author__ = "Dan Rugeles"
__copyright__ = "Copyright 2013, Accelerometrics"
__credits__ = ["Dan Rugeles"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Dan Rugeles"
__email__ = "danrugeles@gmail.com"
__status__ = "Production"

#1.0.1
#Oct 6, 2013
#getCol(): Added Support for all columns

#--getCol------------------------------------------------------
"""Gets the data of a set of columns of a csv file

filename: String representing path to file
col: integer representing the column of the csv file"""
#-------------------------------------------------------------------
def getCol(filename,col):
	result=[]
	with open(filename,"rb") as csvfile:
		alldata=csv.reader(csvfile,delimiter=",")
		for idx,row in enumerate(alldata):
			if type(col)==list:
				if len(col)>1:
					result.append([row[x] for x in col])
				else:
					result.append(row[col[0]])
			elif type(col)==int:
				result.append(row[col])
			elif type(col)==str:
				if col=="all":
					result.append(row)
				else:
					print "Warning: "+col+" is an incorrect argument in getCol() in mycsv.py"
					break
			else:
				print "Warning: Incorrect type of argument in getCol() in mycsv.py"
				break
	return result

#--csv2numpy------------------------------------------------------
"""Gets the data from a csv file and store its selected columns as 
a .npy object

filename: String representing path to file
directory: string representing where the feature will be stored
col: integer representing the column of the csv file
type_: string representing the type of data in the .npy object
Note. Only csv files without header."""
#---------------------------------------------------------------
def csv2numpy(filename,directory,cols,type_):
	shell("mkdir "+ directory)
	allelements=getCol(filename,cols)
	for element in allelements:
		values=np.array([element[1:]]).astype(type_)
		np.save(directory+"/"+str(element[0]),values)
	
	

"""----------------------------*
*                              *
*   |\  /|   /\    |  |\  |    * 
*   | \/ |  /__\   |  | \ |    *
*   |    | /    \  |  |  \|    *
*                              *
*----------------------------"""
if __name__=="__main__":
	#print "First\n"
	#print getCol("User/73.csv",[0,1])
	#print "\nSecond\n"
	#print getCol("User/73.csv",0.9)
	#print "\nThird\n"
	#print getCol("User/73.csv",[0])
	dummy=0
