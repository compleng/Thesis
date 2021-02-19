import subprocess
import shutil
import os
import re
import string
folder ="SO_All_Pcaps"

	
for root, dirs, files in os.walk(folder):
    for filename in files:
      
        alert_file = open(folder + "_protocol_results.txt",'a')
        subprocess.call(["tshark", "-r", os.path.abspath(folder + "/"+filename),"-T", "fields", "-e", "_ws.col.Protocol"],stdout=alert_file)
        alert_file.write("----End----"+filename+"----End----\n")


#        frequency = {}
#        document_text = open('result.txt', 'r')
#        text_string = document_text.read().lower()
#        match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)
# 
#        for word in match_pattern:
#          count = frequency.get(word,0)
#          frequency[word] = count + 1
#     
#        frequency_list = frequency.keys()
# 
#        for words in frequency_list:
#          print(words, frequency[words])
