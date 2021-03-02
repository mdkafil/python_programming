import os
import sys
import json
import subprocess
import time
import datetime
import csv
from pathlib import Path
import numpy as np
import re
import ijson
import wget
import shutil

"""RUN CMD COMMAND"""
"""++++++++++++++++++++++++++++++++++++"""
# data=os.system('curl -d "text=the day is so beautiful!!!" http://text-processing.com/api/sentiment/')


""" Copy Review files in distination Folder """
read_dir = 'C:\\Users\\mdkafiluddin\\Desktop\\Research\\Experiments\\RQ2\\all_app_sentiments\\'

write_dir= 'C:\\Users\\mdkafiluddin\\Desktop\\Research\\Experiments\\RQ2\\all_app_sentiments\\'


#Check if the directory exists of not create NEW directory
if not os.path.exists(write_dir):
	write_dir=os.mkdir(write_dir)



fieldnames = ["Review_NO", "Rating", "Neg_Sen", "Neutral_Sen","Pos_Sen", "Overall_Sen"]

""" Extracted Review values will be saved in a LIST variable called VALUES"""
values = []

def process_each_review(each_user_review):
	# review_string=review_f.readline()
	str_list=each_user_review.split()
	per_review_rating=str_list[0]
	
	# per_review_timestamp_UNIX=int(str_list[1])
	# per_review_timestamp_UNIX=int(round(per_review_timestamp_UNIX/1000))        #milli sec to Sec conversion

	#POSIX/Epoch/Unix-time format to UTC time format conversion
	# universal_time=datetime.datetime.utcfromtimestamp(per_review_timestamp_UNIX)
	# values.append(universal_time)
	values.append(per_review_rating)
	# values[1]=universal_time
	# values[2]=per_review_rating
	# datetime.datetime.fromtimestamp(int(per_review_timestamp_UNIX)).strftime('%Y-%m-%d %H:%M:%S')
	# time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(per_review_timestamp_UNIX))
	
	# print(per_review_timestamp_UNIX)
	# print(universal_time)
	print(per_review_rating)
	
	# print(type(str_list))
	# print(len(str_list))
	
""" Run CURL command in Command Prompt and Get a reply in JSON format"""
"""+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"""
def run_curl_command(each_user_review):
	# print(each_user_review)
	# print(type(each_user_review))
	
	each_user_review=re.sub('\d', '',each_user_review)
	each_user_review=re.sub('\W', ' ',each_user_review)
	each_user_review=re.sub("\n", "",each_user_review)

	cmd = 'curl -d'+' text='+'"'+ each_user_review+'"'+' http://text-processing.com/api/sentiment/'
	
	# print(cmd)
	p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	
	api_response_data=p.stdout.read()   # RETURN api RESPONSE in a json format
	p.stdout.flush()
	# print(type(api_response_data))
	# json.dumps(api_response_data.values())

	# print(type(json.loads(api_response_data)))
	api_response_dict_keys=json.loads(api_response_data).keys()
	api_response_dict_values=json.loads(api_response_data).values()
	# print(api_response_dict_keys)
	# print(api_response_dict_values)

	# print(type(api_response_dict_values))
	# print(type(json.loads(data)))
	# print(list(api_response_dict_values)[0]['neg'])
	# print(list(api_response_dict_values)[1])

	api_response_dict_values=list(api_response_dict_values)

	negetive_sentiment = api_response_dict_values[0]['neg']
	neutral_sentiment  = api_response_dict_values[0]['neutral']
	positive_sentiment = api_response_dict_values[0]['pos']
	overall_sentiment  = api_response_dict_values[1]
	print('\n',negetive_sentiment,'\n',neutral_sentiment,'\n',positive_sentiment,'\n',overall_sentiment)

	values.append(negetive_sentiment)
	values.append(neutral_sentiment)
	values.append(positive_sentiment)
	values.append(overall_sentiment)

	api_response_dict_values.clear()
	# api_response_dict_keys.clear()
	
	# values[3]=negetive_sentiment
	# values[4]=neutral_sentiment
	# values[5]=positive_sentiment
	# values[6]=overall_sentiment


def write_to_file(keys,values,writer):
	# print(type(values))
	# print(values)

	""" CONVERSION OF LIST TO ARRAY """
	values=np.asarray(values)
	# print(type(values))

	writer.writerow({keys[0]: values[0], keys[1]:values[1], keys[2]:values[2], keys[3]:values[3], keys[4]:values[4], keys[5]:values[5]})


def file_reading(review_file_path,writer):
	review_f = open(review_file_path,'r')
	# review_f = open(review_file_path,'r', encoding="utf8")  """Sometimes used to solove Unicode Error"""
	count=0
	for each_user_review in review_f:
		"""Clear the value List before analysing each revew""" 
		values.clear()
		
		if(count<30):
			# each_user_review=review_f.readline()
			# print(each_user_review)
			# print(type(each_user_review))
			# print(each_user_review)
			
			values.append(count+1)
			process_each_review(each_user_review)
			run_curl_command(each_user_review)
			write_to_file(fieldnames,values,writer)
			
			count=count+1
		else:
			break
	
	review_f.close()


"""Read the whole/portion of review file and save its Ratings, Sentiments according to timestamp"""
"""+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"""



# def read_all_communication_app_dataset():
# 	f_csv = csv.reader(open('C:/Users/mdkafiluddin/Desktop/Research/[1]DATASET_v1/Category/COMMUNICATION/Experiment_2/Reviews/all_communication_reviews.csv', 'r', encoding="unicode_escape"))
# 	count=0		#ignore first line
# 	for line in f_csv:
# 		if count==1:
# 			app_id=line[1]
# 			compare_all_communication_app_dataset(app_id)
# 		count=1


def create_write_file_for_sentiments(any_file):
	#Declare your own OUTPUT file
	new_write_name = any_file+'_review_sentiment.csv'
	new_write_file = os.path.join(write_dir, new_write_name)

	# Open file such that it appends PACKAGE, NAME & CATEGORY
	# Get Rid of Unicode Error, New Rows in Output file
	# review_f= open(review_file_path, 'r')

	##WRITE FILE IS ALWAYS OPEN
	write_f=open(new_write_file,'a',encoding="utf8",newline='')
	writer = csv.DictWriter(write_f, fieldnames=fieldnames)
	writer.writeheader()
	return writer








def read_all_communication_app_reviews(read_dir):
	# count =0;
	for any_file in os.listdir(read_dir):
		# if count<3:
			review_file_path=os.path.join(read_dir, any_file)
			# write_app_sentiments_in_file(any_file)
			writer=create_write_file_for_sentiments(any_file)
			file_reading(review_file_path,writer)

			# count=count+1
		# else:
		# 	break

		



if __name__ == '__main__':
	# read_all_communication_app_reviews(read_dir)


	# with open('H:/Research/GooglePlayApps/Communication/comm_trending/reviews/app.fake.caller_helpful_reviews.json', encoding='utf-8',errors='ignore') as f_a:
 #        f_csv_a = csv.DictReader(f_a)
 #        for line_a in f_csv_a:
