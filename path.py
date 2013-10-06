from mysys import *

root=shell("pwd")[0]+"/"
user=shell("locate -b User | grep "+root)[0]+"/"
sequence=shell("locate -b Sequence | grep "+root)[0]+"/"
save=shell("locate -b Save | grep "+root)[0]+"/"


#--get------------------------------------------------------
"""Returns path for <name> inside a directory called <inside>

inside: String representing container directory
name: String representing directory or file
"""
#-------------------------------------------------------------------
def getPath(inside,name):
	result=shell("locate -b "+name+" | grep "+inside)[0]
	return result+"/"
	
	
"""----------------------------*
*                              *
*   |\  /|   /\    |  |\  |    * 
*   | \/ |  /__\   |  | \ |    *
*   |    | /    \  |  |  \|    *
*                              *
*----------------------------"""
if __name__=="__main__":
	print getPath("User","MarkovChain")





