import os
from pathlib import Path
import sys
import shutil


"""RUN CMD COMMAND"""
"""++++++++++++++++++++++++++++++++++++"""


# Get directory name
path_apk_dir='C:\\Users\\mdkafiluddin\\Desktop\\Research\\Dataset\\PlayDrone\\All_APK'
path_apk_manifest_dir='C:\\Users\\mdkafiluddin\\Desktop\\Research\\Dataset\\PlayDrone\\APK_Manifest'
path_temp_dir ='C:\\Users\\mdkafiluddin\\Desktop\\Research\\Dataset\\PlayDrone\\temp'

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
	cmd = 'apktool -v d -o'+' '+path_temp_dir+' '+ path_apk_file
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
