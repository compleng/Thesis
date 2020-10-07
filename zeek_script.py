import subprocess
import shutil
import os
import csv
import time
year ="2013"
for x in range(8):
	
	for root, dirs, files in os.walk(year):
	    for filename in files:
		with open('/opt/zeek/logs/current/notice.log', 'w') as fp: 
	    		pass

		subprocess.call(["tcpreplay", "-i","ens33","-t","-K", os.path.abspath(year + "/"+filename)])
		alert_file = open("/opt/zeek/logs/current/notice.log",'r')	
		output = alert_file.read()

		output_file = open("Zeek_Alerts", "a")
		output_file.write("+++++++++++++++"+filename+"+++++++++++++++\n")
		for line in output.splitlines():
	    	  
			output_file.writelines(line + "\n")
			with open('Zeek_Results.csv', 'a') as file:
				writer = csv.writer(file)
				writer.writerow([filename,"1"])
		if (os.stat("/opt/zeek/logs/current/notice.log").st_size == 0):
		  with open('Zeek_Results.csv', 'a') as file:
			writer = csv.writer(file)
			writer.writerow([filename,"0"])
		output_file.write("-----------------------------------------------------------------\n\n\n\n")
		
		os.remove("/opt/zeek/logs/current/notice.log")
		time.sleep(1)
		

	year = str(int(year)+1)
