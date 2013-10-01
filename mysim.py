#!/usr/bin/env python

import numpy as np
import math

__author__ = "Dan Rugeles"
__copyright__ = "Copyright 2013, <Project>"
__credits__ = ["Dan Rugeles"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Dan Rugeles"
__email__ = "danrugeles@gmail.com"
__status__ = "Production"

#--Root Sum Square Differences---------------------------------------
"""Compute the root sum square difference for two iterables

a: list, matrix or ndarray
b: list, matrix or ndarray

Note. Both elements must have the same amount of primitive elements
"""
#---------------------------------------------------------------
def rssd(a,b):
	a=np.array(a).flatten()
	b=np.array(b).flatten()
	return np.sum((a-b)**2)**0.5


#--Adaptive Root Sum Square Differences---------------------------------------
"""Compute the root sum square difference for two iterables
	Each dimension in the matrix will be weighted proportonally to how much information
	contains each dimension in the matrix.

a: list, matrix or ndarray
b: list, matrix or ndarray

Note. Both elements must have the same amount of primitive elements
"""
#---------------------------------------------------------------
def rssd(a,b):
	a=np.array(a).flatten()
	b=np.array(b).flatten()
	return np.sum((a-b)**2)**0.5

#--Distance Triangle inconsistency ---------------------------------------
"""Compute the sum of inconsistencies for all pair of distances in the
similarity matrix. The function also return the number of inconsistencies found

d:matrix of distances
"""
#---------------------------------------------------------------
def distanceinconsistency(d):
	totalinconsistency=0
	numinconsistencies=0
	maxinconsistencies=0
	numusers=len(d[0])
	
	for a in range(numusers):
		for b in range(numusers):
			if b<=a:continue
			for user in range(numusers):
				maxinconsistencies+=1
				if  user==a or user==b: continue
				oneinconsistency=triangleinconsistency(d[a][user],d[b][user],d[a][b])
				totalinconsistency+=oneinconsistency
				if oneinconsistency!=0 : numinconsistencies+=1
	return numinconsistencies*1.0/maxinconsistencies,totalinconsistency
		

#--Triangle inconsistency for three distances of triangle--------------
"""Compute the sum of inconsistencies for the triangle inequality:
abs(distance1-distance2)<=distance1_2<=distance1+distance2

distance1: integer or float
distance2: integer or float
distance1_2: integer or float

Note. Both elements must have the same amount of primitive elements
"""
#---------------------------------------------------------------
def triangleinconsistency(distance1,distance2,distance1_2):
	#** if the values are non negative there is an inconsistency
	total=max(math.fabs(distance1-distance2)-distance1_2,0) + max(distance1_2-(distance1+distance2),0)
	return total 
						

"""----------------------------*
*                              *
*   |\  /|   /\    |  |\  |    * 
*   | \/ |  /__\   |  | \ |    *
*   |    | /    \  |  |  \|    *
*                              *
*----------------------------"""
if __name__=="__main__":

	a=[[0,1,2],[3,4,2],[0,0,1]]
	b=[[0,1,2],[3,4,1],[0,0,6]]
	print "a\n",a
	print "\nb\n",b
	d=rssd(a,b)
	print "\nRoot Sum Square(a,b)\n",d
	
	print "\n (numInconsistency,Inconsistency) in distance matrix b\n",distanceinconsistency(b)
	
	validdistancematrix=[[0,184,222,177,216,231],
						[184,0,45,123,128,200],
						[222,45,0,129,121,203],
						[177,193,129,0,46,83],
						[216,128,121,46,0,83],
						[231,200,203,83,83,0]]
	print "\nValid Distance Matrix\n",validdistancematrix
	print "\n(numInconsistency,Inconsistency) in valid distance matrix\n",distanceinconsistency(validdistancematrix)
	
	


	
