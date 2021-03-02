import ijson
import csv
import re
import wget
import json
import os
import shutil
from pathlib import Path


""" Copy Review files in distination Folder """
read_dir = 'C:/Users/mdkafiluddin/Downloads/review/review/'
write_dir= 'C:/Users/mdkafiluddin/Desktop/Research/[1]DATASET_v1/Category/COMMUNICATION/Experiment_1/Five_Apps/'

def read_five_app_dataset():
	f_five_app_dataset = csv.reader(open('C:/Users/mdkafiluddin/Desktop/Research/[1]DATASET_v1/Category/COMMUNICATION/Experiment_1/Five_Apps/five_apps_Communication.csv', 'r', encoding="utf8"))
	count=0		#ignore first line
	
	for line in f_five_app_dataset:
		if count==1:
			app_id=line[0]
			comparison_five_app_dataset(app_id)
		count=1

def comparison_five_app_dataset(app_id):
	for any_file in os.listdir(read_dir):
		if(app_id==any_file):
			srcpath = os.path.join(read_dir, any_file)
			dstpath = os.path.join(write_dir, any_file)
			shutil.copytree(srcpath, dstpath)
			break

read_five_app_dataset()
