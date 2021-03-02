import ijson
import json
import csv
import re
import wget
import os
from pathlib import Path

filename ="C:/Users/mdkafiluddin/Downloads/playDrone/2014-10-31.json"




""" READING JSON AS A NORMAL FILE READING """
read_file = 'C:/Users/mdkafiluddin/Desktop/Research/Dataset/SimApp/Intersection_Lists.csv'
write_dir= 'C:/Users/mdkafiluddin/Desktop/Research/Dataset/PlayDrone/'



# #Check if the directory exists of not create NEW directory
if not os.path.exists(write_dir):
	write_dir=os.mkdir(write_dir)

# #Declare your own OUTPUT file
new_write_name = 'Intersection_of_APKLists.csv'
new_write_file = os.path.join(write_dir, new_write_name)

url_lists='apk_url_lists.txt'
new_url_file = os.path.join(write_dir, url_lists)
# # Open file such that it appends PACKAGE, NAME & CATEGORY
# # Get Rid of Unicode Error, New Rows in Output file
write_f=open(new_write_file,'a',encoding="utf8",newline='')
write_url_file=open(new_url_file,'a',encoding="utf8",newline='\n')

# # Declaring Key fieldnames in CSV file
# Write Header in the beginning
fieldnames = ['App_id','Title','Category','Apk_url']
csv_writer = csv.DictWriter(write_f, fieldnames=fieldnames)
csv_writer.writeheader()





"""PRINTING FIRST OBJECT META FIELDS FROM A LARGE JSON OBJECT"""
"""++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"""

# count=True
# count=0
# with open(filename, 'rb') as f:
# 	data = ijson.items(f,'item')
# 	for x in data:
		# if count==True:
		# if count<10000:
			# print(x['apk_url'])
			# print(x.get('apk_url'))
			# print(x.keys(),x.values())
			# keys=list(x.keys())
			# values=list(x.values())
			# print(keys,values)
			# print(list(x.keys()).index('apk_url'))
			# csv_writer.writerow({fieldnames[0]:x.get('app_id'),fieldnames[1]:x.get('title'),fieldnames[2]:x.get('category'),fieldnames[3]:x.get('apk_url')})
			# count=count+1
			# count=False
		# else:
		# 	break

"""++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"""






""" READING JSON AS A NORMAL FILE READING """
# read_file = 'C:/Users/mdkafiluddin/Desktop/Research/Dataset/SimApp/Intersection_Lists.csv'
# write_dir= 'C:/Users/mdkafiluddin/Desktop/Research/Dataset/PlayDrone/'



# #Check if the directory exists of not create NEW directory
# if not os.path.exists(write_dir):
# 	write_dir=os.mkdir(write_dir)

# #Declare your own OUTPUT file
# new_write_name = 'Intersection_of_APKLists.csv'
# new_write_file = os.path.join(write_dir, new_write_name)

# # Open file such that it appends PACKAGE, NAME & CATEGORY
# # Get Rid of Unicode Error, New Rows in Output file
# write_f=open(new_write_file,'a',encoding="utf8",newline='')

# #Declaring Key fieldnames in CSV file
# #Write Header in the beginning
# # fieldnames = ['app_id','title','category','apk_url']
# # csv_writer = csv.DictWriter(write_f, fieldnames=fieldnames)
# # csv_writer.writeheader()

#Write the values based on their given keys 
def write_to_file(app_id,app_name,app_category,apk_url):
	# csv_writer.writerow({'app_id':app_id,'title':app_name,'category':app_category,'apk_url':apk_url})
	csv_writer.writerow({fieldnames[0]:app_id,fieldnames[1]:app_name,fieldnames[2]:app_category,fieldnames[3]:apk_url})
	write_url_file.write(apk_url+os.linesep)

"""Compare Playdrone 2 Million Apps with UCL and SIMAPP intersection dataset"""
"""CAUTION: The Calculation is Massive here, will take HOURS of time based on your device configuration"""
"""+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"""
def compare_playdrone_with_ucl_and_SimApp_intersection_dataset(app_id,app_name):
	with open(filename, 'rb') as f:
		data = ijson.items(f,'item')
		for an_object in data:
			if(app_id==an_object.get('app_id') or app_name==an_object.get('title')):
				print("match found")
				# print(app_id, app_name)
				# print(an_object.get('apk_url'))						#Returns NULL if it doesnt find the value
				# print(an_object.keys(),an_object.values())
				# write_f.write(an_object['apk_url'])  				#Gives error if it doesnt find the values
				write_to_file(an_object.get('app_id'),an_object.get('title'),an_object.get('category'),an_object.get('apk_url',""))
				break


"""Reading UCL and SimApp intersection Dataset and comparing with Playdrone """
"""+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"""
def read_ucl_and_SimApp_intersection_dataset():
	with open(read_file, 'r', encoding="utf8") as f:
		# count=0
		f_intersection_list = csv.reader(f)
		for line in f_intersection_list:
			# if count<5:
			app_id=line[0]
			app_name=line[1]
			compare_playdrone_with_ucl_and_SimApp_intersection_dataset(app_id,app_name)
			# count=count+1
			# else:
				# break

read_ucl_and_SimApp_intersection_dataset()

"""Close writing file"""
write_f.close()
write_url_file.close()
























# # with open(filename, 'r') as f:
# 	# data = ijson.parse(f)
# 	# for apk_url in data:
# 		# print(apk_url)
    
# # count=0
# # with open(filename, 'rb') as f:
# # 	objects = ijson.items(f,'item.apk_url')
# # 	for apk_url in objects:
# # 		if count<2:
# # 			count=count+1
# # 			print(apk_url)	
# # 		else:
# # 			break
# """	
# f_csv = csv.writer(open('C:/Users/mdkafiluddin/Downloads/meta_(1)/meta/ac.gestureCall.csv', 'w'))
	
# with open(filename, 'rb') as f:
# 	objects = ijson.items(f,'item.apk_url')
# 	for apk_url in objects:
# 		f_csv.writerow(apk_url)		
# """

# # f = open('C:/Users/mdkafiluddin/Downloads/meta_(1)/meta/ac.gestureCall.json')
# # data = json.load(f)
# # f.close()

# # f = open('C:/Users/mdkafiluddin/Downloads/playDrone/2014-10-31.json')
# # data = json.load(f)
# # f.close()

# # output_dir ='C:/Users/mdkafiluddin/Downloads'
# # url =data['apk_url']
# # print(url)

# # for url in data:
# 	# wget.download(url,output_dir)


	
	
	

# # output_dir =  'C:/Users/mdkafiluddin/Downloads'
# # url='https://archive.org/download/playdrone-apk-c9/com.google.android.youtube-51405300.apk'
# # wget.download(url,output_dir)



# # text=data['description_html']
# # text=text.readline()

# #Here, we use the regular expression of <.*?>, 
# #which will capture everything that is between two brackets, no matter what. 
# #Of course, more advanced processing would take into consideration what's actually between them, but our .* will capture everything and the ? 
# #will make sure that the regex is not greedy (meaning it won't capture everything from the first < to the last > in the document).
# # text = re.sub('<.*?>', '', text)

# # this will also substitute all tabs, newlines and other "whitespace-like" characters. 
# # the strip() in the end will cut off any trailing whitespaces
# # text=re.sub( '\s+', ' ', text ).strip()

# # print(text)


# # f = csv.writer(open('C:/Users/mdkafiluddin/Downloads/meta_(1)/meta/ac.gestureCall.csv', 'wb+'))
# # use encode to convert non-ASCII characters
# # for item in data:
#     # values = [ x.encode('utf8') for x in item['fields'].values() ]
#     # f.writerow([item['pk'], item['model']] + values)




# # with open('C:/Users/mdkafiluddin/Downloads/meta_(1)/meta/ac.gestureCall.json','r') as f:
# 	# f_contents =f.read()
# 	# print(f_contents);

# #f.close();


