#!/usr/bin/env python

from mysys import *
import numpy as np
import mysim
import markovchain as mc

__author__ = "Dan Rugeles"
__copyright__ = "Copyright 2013, <Project>"
__credits__ = ["Dan Rugeles"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Dan Rugeles"
__email__ = "danrugeles@gmail.com"
__status__ = "Production"

#** Directories
MarkovChaindir="MarkovChain"
MarkovChainDiffdir="MarkovChainDiff"

#** Process
# 1
FEATURES=False
# 2
DISTANCES=True
# 3
INCONSISTENCY=True



#Note. Must be .npy files
def loadfeature(directory):	
	Mat_id=[]
	Mats=[]
	for Mat_file in shell("ls "+directory):
		user_id=int(Mat_file.rstrip(".npy"))
		Mat_id.append(user_id)	
		Mats.append(np.load(directory+"/"+Mat_file))
	return Mats,user_id

def allPairRSSD(Mats):
	numusers=len(Mats)
	Mat_distance=np.zeros((numusers,numusers))
	for i in range(numusers):
		for j in range(numusers):
			if j<=i: continue
			else:
				Mats_distance=mysim.rssd(Mats[i],Mats[j])
				Mat_distance[i][j]=Mats_distance
				Mat_distance[j][i]=Mats_distance
	return Mat_distance
	
def allPairWeightedRSSD(Mats):

	Mats=np.array(Mats)
	print Mats[300]
	Mats=Mats.reshape([Mats.shape[0],Mats.shape[1]*Mats.shape[2]])
	print Mats[300]
	
	"""numusers=len(Mats)
	Mat_distance=np.zeros((numusers,numusers))
	for i in range(numusers):
		for j in range(numusers):
			if j<=i: continue
			else:
				Mats_distance=mysim.rssd(Mats[i],Mats[j])
				Mat_distance[i][j]=Mats_distance
				Mat_distance[j][i]=Mats_distance
	return Mat_distance"""

	
"""----------------------------*
*                              *
*   |\  /|   /\    |  |\  |    * 
*   | \/ |  /__\   |  | \ |    *
*   |    | /    \  |  |  \|    *
*                              *
*----------------------------"""
if __name__=="__main__":



	if FEATURES:
		#1a. Compute feature directories for all users 		
		mc.markovchainAllUsers(MarkovChaindir,MarkovChainDiffdir)
	else:		
		#1b. Load features from directory
		allfeaturesMC,user_id=loadfeature(MarkovChaindir)
		allfeaturesMCD,user_id=loadfeature(MarkovChainDiffdir)
	
	if DISTANCES:
		#2a. Compute all pair of distances according to a similarity function
		MC_distances=allPairRSSD(allfeaturesMC)
		np.save(MarkovChaindir+"_distances",MC_distances)
		MCD_distances=allPairRSSD(allfeaturesMCD)
		np.save(MarkovChainDiffdir+"_distances",MCD_distances) 
	else:
		#2b. Load Distances
		MC_distances =np.load(MarkovChaindir+"_distances.npy")	
		MCD_distances =np.load(MarkovChainDiffdir+"_distances.npy")	
		
	if INCONSISTENCY:	
		#3. Compute Inconsistency of distance
		print mysim.distanceinconsistency(MC_distances)
		print mysim.distanceinconsistency(MCD_distances)

	#print accelerometrics(MarkovChaindir,allPairRSSD)
	#(0.0007264554822878536, 1.2523412565401372e-15)
	#print accelerometrics(MarkovChainDiffdir,allPairRSSD)
	#(0.0007264554822878536, 1.2523412565401372e-15)

	#print accelerometrics(MarkovChaindir,allPairWeightedRSSD)
	#print accelerometrics(MarkovChainDiffdir,allPairWeightedRSSD)
	
	
	
	
		
	

	
