import fileinput
import subprocess
import shutil
import os
import csv
folder="rules"

for root, dirs, files in os.walk(folder):
    for filename in files:


      with open(folder+"/"+filename, 'r') as file :
         filedata = file.read()

      # Replace the target string
      filedata = filedata.replace('# alert', 'alert')

      # Write the file out again
      with open(folder+"/"+filename, 'w') as file:
         file.write(filedata)
