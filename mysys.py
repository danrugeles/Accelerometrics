#!/usr/bin/env python
import subprocess 
import re

__author__ = "Dan Rugeles"
__copyright__ = "Copyright 2013, Accelerometrics"
__credits__ = ["Dan Rugeles"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Dan Rugeles"
__email__ = "danrugeles@gmail.com"
__status__ = "Production"

#--shell------------------------------------------------------
"""Executes a linux shell comand and returns result as a list

command: String representing command linux
Note. Piped commands such "ls | grep <something>" are not supported"""
#-------------------------------------------------------------------
def shell(command):

	p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
	(output,err) = p.communicate()
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
	print shell(" ls User ")
	
