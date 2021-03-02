import ijson
import csv
import re
import wget
import json
import os
from pathlib import Path


""" READING JSON AS A NORMAL FILE READING """
read_dir = 'C:/Users/mdkafiluddin/Downloads/meta_(1)/meta/'
write_dir= 'C:/Users/mdkafiluddin/Desktop/Research/Dataset/SimApp/'



#Check if the directory exists of not create NEW directory
if not os.path.exists(write_dir):
	write_dir=os.mkdir(write_dir)

#Declare your own OUTPUT file
new_write_name = 'Intersection_Lists.csv'
new_write_file = os.path.join(write_dir, new_write_name)

# Open file such that it appends PACKAGE, NAME & CATEGORY
# Get Rid of Unicode Error, New Rows in Output file
write_f=open(new_write_file,'a',encoding="utf8",newline='')


"""Reading and Writing Only Part of a JSON file into CSV Format"""
"""++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"""
def file_reading(filename_):
	read_path=os.path.join(read_dir, filename_)
	read_f = open(read_path,encoding="utf8")
	data = json.load(read_f)
	keys=list(data.keys())
	values=list(data.values())
	comparison_with_ucl_dataset(keys,values)
	read_f.close()


def comparison_with_ucl_dataset(keys,values):
	f_ucl_dataset = csv.reader(open('C:/Users/mdkafiluddin/Desktop/Research/Dataset/UCLappA/test.csv', 'r', encoding="utf8"))
	count=0		#ignore first line
	
	app_id=values[0]
	app_name=values[1]
	
	for line in f_ucl_dataset:
		if count==1:
			if((app_id==line[1]) or (app_name==line[2])):
				print(app_id, line[1], app_name,line[2])
				write_to_file(keys,values, write_f)
				break
		count=1

	# f_ucl_dataset.close()


flag =0		#WRITE HEADER FOR FIRST ITERATION

def write_to_file(keys,values, write_file):
	fieldnames = [keys[0],keys[1], keys[2]]
	writer = csv.DictWriter(write_file, fieldnames=fieldnames)
	if flag==1:
		writer.writerow({keys[0]: values[0], keys[1]:values[1], keys[2]:values[2]})
	else :
		writer.writeheader()
		writer.writerow({keys[0]: values[0], keys[1]:values[1], keys[2]:values[2]})


""" READ ALL THE FILES FROM THE DIRECTORY"""
"""+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"""
for any_file in os.listdir(read_dir):
	print(any_file)
	file_reading(any_file)
	print('+++++++++++++++++++++++')
	flag=1

write_f.close()

