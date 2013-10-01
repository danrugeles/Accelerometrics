#!/usr/bin/env python

import mysys
import numpy as np
import mysim

__author__ = "Dan Rugeles"
__copyright__ = "Copyright 2013, <Project>"
__credits__ = ["Dan Rugeles"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Dan Rugeles"
__email__ = "danrugeles@gmail.com"
__status__ = "Production"


"""----------------------------*
*                              *
*   |\  /|   /\    |  |\  |    * 
*   | \/ |  /__\   |  | \ |    *
*   |    | /    \  |  |  \|    *
*                              *
*----------------------------"""
if __name__=="__main__":

	#** Definitions
	numusers=387
	MC_distance=np.zeros((numusers,numusers))
	MCs=[]
	MC_id=[]
	

	#1. Generate MC for all users executing python markovchain.py
	
	#2. Load all Markov Chains
	for mc_file in shell("ls MarkovChain"):
		user_id=int(mc_file.rstrip(".csv"))
		MC_id.append(user_id)	
		MCs.append(np.load(mc_file))
	

	#3. Compute user distance according to their MC representation
	size=len(MC_id.append(user_id))
	for i in range(size):
		for j in range(size):
			if j<=i: continue
			else:
				mcs_distance=mysim.rssd(MCs[i],MCs[j])
				MC_distance[i][j]=mcs_distance
				MC_distance[j][i]=mcs_distance
				
	#4. Compute Inconsistency of MC_distance
	mysim.distanceinconsistency(MC_distance)
	
		
	

	
