import markovchain as mc
import mycsv as my
import path 

#print "Computing Features for all users..."
#mc.markovchainAllUsers(path.user,MCbasename,MCDbasename)
#mc.markovchainAllUsers(path.sequence,MCbasename,MCDbasename)

print "Importing Features from CSV ..."
my.csv2numpy("Features_U.csv",path.user+"Aly",[0,4,8],float)
my.csv2numpy("Features_U.csv",path.user+"GJ",[0,39,40,41,42,43,44,45,46,47,48],float)
my.csv2numpy("Features_S.csv",path.sequence+"Aly",[0,4,8],float)
my.csv2numpy("Features_S.csv",path.sequence+"GJ",[0,39,40,41,42,43,44,45,46,47,48],float)
