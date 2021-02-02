import subprocess
import shutil
import os
import csv
folder ="Others"

	
for root, dirs, files in os.walk(folder):
    for filename in files:
        with open('alert.txt', 'w') as fp: 
                pass
	#sudo snort -v -c /etc/snort/snort.conf -r filename -A full
        alert_file = open("alert.txt",'a')
        subprocess.call(["snort", "-q", "-c", "/home/snort3/Desktop/Snort3_Rules/Community_Rules/snort/snort.lua", "-r", os.path.abspath(folder + "/"+filename),"-A", "full"],stdout=alert_file)
        alert_file = open("alert.txt",'r')	
        output = alert_file.read()

        output_file = open("Snort_Alerts_Community_"+folder, "a")
        output_file.write("+++++++++++++++"+filename+"+++++++++++++++\n")
        for line in output.splitlines():
          if "[**]" in line:
                output_file.writelines(line + "\n")
                with open('Snort_Results_Community_'+folder+'.csv', 'a') as file:
                        writer = csv.writer(file)
                        writer.writerow([filename,"1"])
        if (os.stat("alert.txt").st_size == 0):
          with open('Snort_Results_Community_'+folder+'.csv', 'a') as file:
                writer = csv.writer(file)
                writer.writerow([filename,"0"])
        output_file.write("-----------------------------------------------------------------\n\n\n\n")

	
		  

        os.remove("alert.txt")
		
##---------------------------------------------------------------

for root, dirs, files in os.walk(folder):
    for filename in files:
        with open('alert.txt', 'w') as fp: 
                pass
	#sudo snort -v -c /etc/snort/snort.conf -r filename -A full
        alert_file = open("alert.txt",'a')
        subprocess.call(["snort", "-q", "-c", "/home/snort3/Desktop/Snort3_Rules/Registered Rules/snort/snort.lua", "-r", os.path.abspath(folder + "/"+filename),"-A", "full"],stdout=alert_file)
        alert_file = open("alert.txt",'r')	
        output = alert_file.read()

        output_file = open("Snort_Alerts_Registered_"+folder, "a")
        output_file.write("+++++++++++++++"+filename+"+++++++++++++++\n")
        for line in output.splitlines():
          if "[**]" in line:
                output_file.writelines(line + "\n")
                with open('Snort_Results_Registered_'+folder+'.csv', 'a') as file:
                        writer = csv.writer(file)
                        writer.writerow([filename,"1"])
        if (os.stat("alert.txt").st_size == 0):
          with open('Snort_Results_Registered_'+folder+'.csv', 'a') as file:
                writer = csv.writer(file)
                writer.writerow([filename,"0"])
        output_file.write("-----------------------------------------------------------------\n\n\n\n")

	
		  

        os.remove("alert.txt")


#---------------------------------------------------------------

#for root, dirs, files in os.walk(folder):
#    for filename in files:
#        with open('alert.txt', 'w') as fp: 
#                pass
#	#sudo snort -v -c /etc/snort/snort.conf -r filename -A full
#        alert_file = open("alert.txt",'a')
#        subprocess.call(["snort", "-v", "-c", "/home/snort3/Desktop/Rules/Emerging_Rules/snort/snort.lua", "-r", os.path.abspath(folder + "/"+filename),"-A", "full"],stdout=alert_file)
#        alert_file = open("alert.txt",'r')	
#        output = alert_file.read()

#        output_file = open("Snort_Alerts_Emerging_Malware", "a")
#        output_file.write("+++++++++++++++"+filename+"+++++++++++++++\n")
#        for line in output.splitlines():
#          if "[**]" in line:
#                output_file.writelines(line + "\n")
#                with open('Snort_Results_Emerging_Malware.csv', 'a') as file:
#                        writer = csv.writer(file)
#                        writer.writerow([filename,"1"])
#        if (os.stat("alert.txt").st_size == 0):
#          with open('Snort_Results_Emerging_Malware.csv', 'a') as file:
#                writer = csv.writer(file)
#                writer.writerow([filename,"0"])
#        output_file.write("-----------------------------------------------------------------\n\n\n\n")
#	
#		
#		  

#        os.remove("alert.txt")


