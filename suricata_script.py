import subprocess
import shutil
import os
import csv
year ="2013"
for x in range(8):
	
	for root, dirs, files in os.walk(year):
	    for filename in files:
		with open('fast.log', 'w') as fp: 
	    		pass
		subprocess.call(["suricata", "-c", "/etc/suricata/suricata.yaml", "-r", os.path.abspath(year + "/"+filename), "-v"])
		alert_file = open("fast.log",'r')	
		output = alert_file.read()

		output_file = open("Suricata_Alerts", "a")
		output_file.write("+++++++++++++++"+filename+"+++++++++++++++\n")
		for line in output.splitlines():
	    	  if "[**]" in line:
			output_file.writelines(line + "\n")
			with open('Suricata_Results.csv', 'a') as file:
				writer = csv.writer(file)
				writer.writerow([filename,"1"])
		if (os.stat("fast.log").st_size == 0):
		  with open('Suricata_Results.csv', 'a') as file:
			writer = csv.writer(file)
			writer.writerow([filename,"0"])
		output_file.write("-----------------------------------------------------------------\n\n\n\n")
	
		os.remove("fast.log")
		

	year = str(int(year)+1)
