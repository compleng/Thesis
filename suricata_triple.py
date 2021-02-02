import subprocess
import shutil
import os
import csv
folder ="Others"

	
for root, dirs, files in os.walk(folder):
    for filename in files:
        with open('fast.log', 'w') as fp: 
                pass
        subprocess.call(["suricata", "-c", "/home/snort3/Desktop/Suricata_Rules/Community_Rules/suricata.yaml", "-r", os.path.abspath(folder + "/"+filename), "-v"])
        alert_file = open("fast.log",'r')	
        output = alert_file.read()

        output_file = open("Suricata_Alerts_Community_"+folder, "a")
        output_file.write("+++++++++++++++"+filename+"+++++++++++++++\n")
        for line in output.splitlines():
          if "[**]" in line:
                output_file.writelines(line + "\n")
                with open('Suricata_Results_Community_'+folder+'.csv', 'a') as file:
                        writer = csv.writer(file)
                        writer.writerow([filename,"1"])
        if (os.stat("fast.log").st_size == 0):
          with open('Suricata_Results_Community_'+folder+'.csv', 'a') as file:
                writer = csv.writer(file)
                writer.writerow([filename,"0"])
        output_file.write("-----------------------------------------------------------------\n\n\n\n")
	
		
		  

        os.remove("fast.log")
	

#---------------------------------------------

for root, dirs, files in os.walk(folder):
    for filename in files:
        with open('fast.log', 'w') as fp: 
                pass
        subprocess.call(["suricata", "-c", "/home/snort3/Desktop/Suricata_Rules/Registered Rules/suricata.yaml", "-r", os.path.abspath(folder + "/"+filename), "-v"])
        alert_file = open("fast.log",'r')	
        output = alert_file.read()

        output_file = open("Suricata_Alerts_Registered_"+folder, "a")
        output_file.write("+++++++++++++++"+filename+"+++++++++++++++\n")
        for line in output.splitlines():
          if "[**]" in line:
                output_file.writelines(line + "\n")
                with open('Suricata_Results_Registered_'+folder+'.csv', 'a') as file:
                        writer = csv.writer(file)
                        writer.writerow([filename,"1"])
        if (os.stat("fast.log").st_size == 0):
          with open('Suricata_Results_Registered_'+folder+'.csv', 'a') as file:
                writer = csv.writer(file)
                writer.writerow([filename,"0"])
        output_file.write("-----------------------------------------------------------------\n\n\n\n")
	
		
		  

        os.remove("fast.log")

#----------------------------------------------

#for root, dirs, files in os.walk(folder):
#    for filename in files:
#        with open('fast.log', 'w') as fp: 
#                pass
#        subprocess.call(["suricata", "-c", "/home/cmplng/Desktop/Rules/Suricata/Emerging Threats/suricata.yaml", "-r", os.path.abspath(folder + "/"+filename), "-v"])
#        alert_file = open("fast.log",'r')	
#        output = alert_file.read()

#        output_file = open("Suricata_Alerts_Emerging", "a")
#        output_file.write("+++++++++++++++"+filename+"+++++++++++++++\n")
#        for line in output.splitlines():
#          if "[**]" in line:
#                output_file.writelines(line + "\n")
#                with open('Suricata_Results_Emerging.csv', 'a') as file:
#                        writer = csv.writer(file)
#                        writer.writerow([filename,"1"])
#        if (os.stat("fast.log").st_size == 0):
#          with open('Suricata_Results_Emerging.csv', 'a') as file:
#                writer = csv.writer(file)
#                writer.writerow([filename,"0"])
#        output_file.write("-----------------------------------------------------------------\n\n\n\n")
#	
#		
#		  

#        os.remove("fast.log")
#	
