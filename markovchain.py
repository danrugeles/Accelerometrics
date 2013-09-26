#!/usr/bin/env python

from mysys import *
from mycsv import *
import numpy as np

__author__ = "Dan Rugeles"
__copyright__ = "Copyright 2013, Accelerometrics"
__credits__ = ["Dan Rugeles"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Dan Rugeles"
__email__ = "danrugeles@gmail.com"
__status__ = "Production"

#--markovchain------------------------------------------------------
"""Returns Markov Chain Matrix dimension numchanges x numchanges 
Each column and row represent a change in the data size separation.
change = current value - past value (local derivative)

e.g. 
if separation=4 and numchanges=5 then the columns and rows represent  
the following changes
[-8,-4,0,4,8] 

x: list
numchanges: integer
separation: integer"""
#-------------------------------------------------------------------
def markovchain(x,numchanges,separation):
 
	MC=np.zeros((numchanges,numchanges))

	#** Find the derivative of the signal
	x_=np.diff(x)

	#** Use the rounding trick for O(1) computing of nearest neighbor 
	#   in equally separated spaces
	#   neirestneighbor=(round(floatnum/separation))*separation

	#** Get allchanges from the newspace definition
	allchanges=map(lambda x : (round(x*1.0/separation)),x_)

	#** Adjust allchanges from 0 to numchanges-1
	adjustedchanges=map(lambda x : max(min(x+numchanges/2,numchanges-1),0) ,allchanges)

	prevchange=adjustedchanges[0]
	for onechange in adjustedchanges[1:]:
		MC[prevchange][onechange]+=1
		prevchange=onechange
	
	#** Normalize per row
	return (MC.T/(np.sum(MC,axis=1)+0.0000001)).T

"""----------------------------*
*                              *
*   |\  /|   /\    |  |\  |    * 
*   | \/ |  /__\   |  | \ |    *
*   |    | /    \  |  |  \|    *
*                              *
*----------------------------"""
if __name__=="__main__":

	#** Definitions
	#newspace=[ .. -8,-4,0,4,8 ..] if separation=4 
	separation=4
	#len(newspace)=numchanges 
	numchanges=5
	
	#** For each user
	for filename in shell("ls /User"):
		userid=filename.rstrip(".csv")

		#** Get RSS information
		x=getCol("/User/"+str(userid)+".csv",-1)
		x=[float(elem) for elem in x]
	
		#** Store MarkovChain for all users
		np.save("MarkovChain/"+userid,markovchain(x,numchanges,separation))
	
