#!/usr/bin/env python

from mysys import *
from mycsv import *
import numpy as np
import path

__author__ = "Dan Rugeles"
__copyright__ = "Copyright 2013, Accelerometrics"
__credits__ = ["Dan Rugeles"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Dan Rugeles"
__email__ = "danrugeles@gmail.com"
__status__ = "Production"

# 1.0.1
# Improve Speed of markov chain by using numpy and map function.

SAVE=False

#--markovchain------------------------------------------------------
"""Returns Markov Chain Matrix dimension numchanges x numchanges 
Each column and row represent a change in the data size separation.
change = current value - past value (local derivative)

e.g. 
if separation=4 and numchanges=5 then the columns and rows represent  
the following changes
[-8,-4,0,4,8] 

x: list or 1darray
"""
#-------------------------------------------------------------------
def markovchain(x,numchanges,separation):
 
 	x-=np.mean(x)
	MC=np.zeros((numchanges,numchanges))

	#** Use the rounding trick for O(1) computing of nearest neighbor 
	#   in equally separated spaces
	#   neirestneighbor=(round(floatnum/separation))*separation
	
	#** Get allchanges from the newspace definition
	allchanges=map(lambda x : (round(x*1.0/separation)),x)
	
	#** Adjust allchanges from 0 to numchanges-1
	adjustedchanges=map(lambda x : max(min(x+numchanges/2,numchanges-1),0) ,allchanges)
	
	prevchange=adjustedchanges[0]
	for onechange in adjustedchanges[1:]:
		MC[prevchange][onechange]+=1
		prevchange=onechange
	
	#** Normalize per row
	return (MC.T/(np.sum(MC,axis=1)+0.0000001)).T

#--MarkovChain-AllUsers------------------------------------------------------
"""Returns Markov Chain Matrix dimension numchanges x numchanges 
Computes the Markov Chain for all Users

dirnameMC: String representing directory for MCDiff featur
dirnameMCDiff: String representing directory for MCDiff feature
"""
#-------------------------------------------------------------------
def markovchainAllUsers(filepath,dirnameMC,dirnameMCDiff):
	#** Definitions
	#newspace=[ .. -8,-4,0,4,8 ..] if separation=4 
	#len(newspace)=numchanges 
	
	#For x : 0~0.5 to 25~30
	#For x_:  -20 to 20

	dirnameMC=	path.getPath(filepath,"MarkovChain")
	dirnameMCDiff=	path.getPath(filepath,"MarkovChainDiff")
	#shell("mkdir "+dirnameMC)
	#shell("mkdir "+dirnameMCDiff)
	
	if SAVE:
		allx=[]
		for filename in shell("ls "+filepath+" | grep .csv"):
			userid=filename.rstrip(".csv")
			x=getCol(filepath+str(userid)+".csv",-1)
			allx=allx+[float(num) for num in x]
			#x=np.asarray(x).astype(float)		
			#allx=np.hstack((allx,x))
			#x_=np.diff(x)
			#allx_=np.hstack((allx_,x_))
	
		allx=np.array(allx)
		allx_=np.diff(allx)
		meanallx=np.mean(allx)
		stdallx=np.std(allx)
		meanallx_=np.mean(allx_)
		stdallx_=np.std(allx_)
	
		np.save("Save/meanallseqx",meanallx)
		np.save("Save/meanallseqx_",meanallx_)
		np.save("Save/stdallseqx",stdallx)
		np.save("Save/stdallseqx_",stdallx_)
	else:
		meanallx=np.load("Save/meanallx.npy")
		meanallx_=np.load("Save/meanallx_.npy")
		stdallx=np.load("Save/stdallx.npy")
		stdallx_=np.load("Save/stdallx_.npy")
		
	
	#** For each user
	for filename in shell("ls "+filepath+" | grep .csv"):
		userid=filename.rstrip(".csv")

		#** Get RSS information
		x=getCol(filepath+str(userid)+".csv",-1)
		x=np.asarray(x).astype(float)		
				
		#** Store MarkovChain for all users
		separation=stdallx#3
		numchanges=3
		np.save(dirnameMC+userid,markovchain(x,numchanges,separation))
		
		#** Find the derivative of the signal
		x_=np.diff(x)
	
		#** Store MarkovChainDiff for all users
		separation=stdallx_#4
		numchanges=3
		np.save(dirnameMCDiff+userid,markovchain(x_,numchanges,separation))
	
	
"""----------------------------*
*                              *
*   |\  /|   /\    |  |\  |    * 
*   | \/ |  /__\   |  | \ |    *
*   |    | /    \  |  |  \|    *
*                              *
*----------------------------"""
if __name__=="__main__":
	#x=[2.3,1.3,12.3,15.3,16.3,18.3,19.3,6.3,-4.3,-3.3,-6.3,-7.3]
	#print markovchain(x,5,5)
	
	
	#** Directory
	MarkovChaindir="MarkovChain"
	MarkovChainDiffdir="MarkovChainDiff"
	#markovchainAllUsers(path.sequence,MarkovChaindir,MarkovChainDiffdir)
	markovchainAllUsers(path.sequence,MarkovChaindir,MarkovChainDiffdir)
	
	
	
	
	
	
	
	
