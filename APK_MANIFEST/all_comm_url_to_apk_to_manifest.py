import os
from pathlib import Path
import sys
import shutil
import csv
import wget


# Get directory name
path_apk_dir='C:\\Users\\mdkafiluddin\\Desktop\\Research\\[1]DATASET_v1\\Category\\COMMUNICATION\\Experiment_2\\All_APK'
path_apk_manifest_dir='C:\\Users\\mdkafiluddin\\Desktop\\Research\\[1]DATASET_v1\\Category\\COMMUNICATION\\Experiment_2\\All_APK_Manifest'
path_temp_dir ='C:\\Users\\mdkafiluddin\\Desktop\\Research\\[1]DATASET_v1\\Category\\COMMUNICATION\\Experiment_2\\temp'


#Check if the directory exists of not create NEW directory
if not os.path.exists(path_apk_dir):
	write_dir=os.mkdir(path_apk_dir)

#Check if the directory exists of not create NEW directory
if not os.path.exists(path_apk_manifest_dir):
	write_dir=os.mkdir(path_apk_manifest_dir)

#Check if the directory exists of not create NEW directory
if not os.path.exists(path_temp_dir):
	write_dir=os.mkdir(path_temp_dir)



def read_and_download_all_comm_app_apk_url():
	f_csv = csv.reader(open('C:/Users/mdkafiluddin/Desktop/Research/[1]DATASET_v1/Category/COMMUNICATION/Experiment_2/all_communication_apk_url.csv', 'r', encoding="unicode_escape"))
	count=0		#ignore first line
	for line in f_csv:
		if count==1:
			app_url=line[3]
			wget.download(app_url,path_apk_dir)
			print(app_url)
		count=1

read_and_download_all_comm_app_apk_url()





"""RUN CMD COMMAND"""
"""++++++++++++++++++++++++++++++++++++"""






# path_apk_file=path_apk_dir+'\\'+'com.tomasperez.dictionary.pkg-4.apk'

# cmd = 'apktool -v d -o'+' '+path_temp_dir+' '+ path_apk_file
# os.system(cmd)


# Create Temporary directory for processing
# def create_temp_dir():
# 	if not os.path.exists(path_temp_dir):
# 		os.mkdir(path_temp_dir)
		

# Execute CMD command to RUN apktool
def run_cmd_to_extract_apk(_apk_file_name):
	# create_temp_dir()
	path_apk_file= os.path.join(path_apk_dir, _apk_file_name)
	print(path_apk_file)
	#VERBOSE was showing some errors. Need to fix it at a later time
	# cmd = 'apktool -v d -o'+' '+path_temp_dir+' '+ path_apk_file
	cmd = 'apktool -f d -o'+' '+path_temp_dir+' '+ path_apk_file
	os.system(cmd)
	APK_Manifest_file=path_temp_dir+'\\'+'AndroidManifest.xml'
	newfile=_apk_file_name+"_AndroidManifest.xml"
	manifest_file=path_apk_manifest_dir+'\\'+newfile
	shutil.copy2(APK_Manifest_file , manifest_file)
	remove_temp_directory()


# Try to remove Temporary directory tree; if failed show an error using try...except on screen
def remove_temp_directory():
	try:
	    shutil.rmtree(path_temp_dir)
	except OSError as e:
	    print ("Error: %s - %s." % (e.filename, e.strerror))


# run_cmd_to_extract_apk("com.tomasperez.dictionary.pkg-4.apk")

# """ READ Entire FILES from THE DIRECTORY"""
# """+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"""

for apk_file in os.listdir(path_apk_dir):
	print(apk_file)
	run_cmd_to_extract_apk(apk_file)
	print('+++++++++++++++++++++++')
