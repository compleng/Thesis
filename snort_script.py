import subprocess
import shutil
import os
import csv
year ="2013"
for x in range(8):
	
	for root, dirs, files in os.walk(year):
	    for filename in files:
		with open('/var/log/snort/alert', 'w') as fp: 
	    		pass
		shutil.copy("/var/log/snort/alert","/var/log/snort/old_alert")
		#sudo snort -v -c /etc/snort/snort.conf -r filename -A full
		subprocess.call(["snort", "-v", "-c", "/etc/snort/snort.conf", "-r", os.path.abspath(year + "/"+filename),"-A", "full"])
		alert_file = open("/var/log/snort/alert",'r')	
		output = alert_file.read()

		output_file = open("Snort_Alerts", "a")
		output_file.write("+++++++++++++++"+filename+"+++++++++++++++\n")
		for line in output.splitlines():
	    	  if "[**]" in line:
			output_file.writelines(line + "\n")
			with open('Snort_Results.csv', 'a') as file:
				writer = csv.writer(file)
				writer.writerow([filename,"1"])
		  else:
			with open('Snort_Results.csv', 'a') as file:
				writer = csv.writer(file)
				writer.writerow([filename,"0"])
		output_file.write("-----------------------------------------------------------------\n\n\n\n")
		
    			
    			  

		os.remove("/var/log/snort/alert")
		os.remove("/var/log/snort/old_alert")

	year = str(int(year)+1)
