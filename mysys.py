#!/usr/bin/env python
import subprocess 
import re

__author__ = "Dan Rugeles"
__copyright__ = "Copyright 2013, Accelerometrics"
__credits__ = ["Dan Rugeles"]
__license__ = "GPL"
__version__ = "1.1.0"
__maintainer__ = "Dan Rugeles"
__email__ = "danrugeles@gmail.com"
__status__ = "Production"

#1.1.0
"shell(): Added Commands with pipes"

#--shell------------------------------------------------------
"""Executes a linux shell comand and returns results as a list

command: String representing command linux
Note. Commands with slow response times breaks the pipe
e.g. cat * | grep "Linux" | grep -v "UNIX" | wc -l """
#-------------------------------------------------------------------
def shell(command):

	#Parse command into Pipes
	pipes=re.findall(r"([\*\"\.\s\w/-]*)\|*",command)
	result=None
	
	#print "Execute Command: \n",pipes
	
	#Execute each of the pipes sequentially
	for com in pipes[:-1]:
		process = subprocess.Popen(com, stdin=result, stdout=subprocess.PIPE,shell=True)
		result=process.stdout
		
	(output,err) = process.communicate()
	output=output.rstrip("\n").split("\n")
	
	return output
	
"""----------------------------*
*                              *
*   |\  /|   /\    |  |\  |    * 
*   | \/ |  /__\   |  | \ |    *
*   |    | /    \  |  |  \|    *
*                              *
*----------------------------"""
if __name__=="__main__":
	print shell("mkdir Dannnii")
	print shell("ls | grep .py")

	
