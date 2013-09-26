#**Algorithm only works for csv without header
import csv

#last ID read
lastId=7
#File to store new user
userfile= open(str(lastId)+".csv","w")
#In seconds
windowduration=0.5
#Contain aggregated data
x_s=[];y_s=[];z_s=[];rss_s=[]
#Inititalize time quantization
lastnewtime=0
average = lambda x: sum(x)/len(x)

with open("train.csv","rb") as csvfile:
	alldata=csv.reader(csvfile,delimiter=",")

	for idx,row in enumerate(alldata):
		
		#** Definitions
		firstsample_ = (idx==0)
		f_row=[float(x) for x in row]
		time=f_row[0];x=f_row[1];y=f_row[2];z=f_row[3];Id=int(f_row[-1])
		rss=(x**2+y**2+z**2)**0.5
		newuser_= (Id!=lastId)
		if firstsample_ or newuser_: initialtime=time; lastnewtime=0
		newtime=int((time-initialtime)/(windowduration*1000))
		newwindow_=(newtime!=lastnewtime or newuser_)
		aggregatedtime=lastnewtime*windowduration
		
	
		#** Filter wrong data
		if x==0 and y==0 and z == 0: continue
		
		#** New window? Write aggregated result and start aggregating
		if newwindow_:
			lastnewtime=newtime
			userfile.write(str(aggregatedtime)+
							","+str(average(x_s))+
							","+str(average(y_s))+
							","+str(average(z_s))+
							","+str(average(rss_s))+"\n")
			x_s[:]=[];y_s[:]=[];z_s[:]=[];rss_s[:]=[]
					
		#** New User? Create File
		if newuser_:
			lastId=Id	
			userfile.close()
			userfile= open("User/"+str(Id)+".csv","w")
			currenttime=0;	
				
		#** Aggregate data in windows of time.
		x_s.append(x);y_s.append(y);z_s.append(z);rss_s.append(rss)

		#** Uncomment to see individual data
		#userfile.write("_"+str(newtime*windowduration)+","+",".join(row[:-1])+","+str(rss)+"\n")
	
	userfile.close()
	
