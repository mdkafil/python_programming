import nltk
import csv
import re
import os
from nltk.corpus import stopwords
from nltk.tag.stanford import StanfordPOSTagger
from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet as wn
from nltk.corpus import wordnet_ic
import sys
from itertools import islice

import gensim
import gensim.models.keyedvectors as word2vec


dir_name='C:/Users/mdkafiluddin/Desktop/Research/Dataset/UCLappA/'

# f_csv = csv.DictReader(open('C:\\Users\\mdkafiluddin\\Desktop\\Research\\[1]DATASET_v1\\Category\\BOOK_AND_REF\\book_and_ref_competitors.csv', encoding="utf-8"))
# f_csv_weather = csv.DictReader(open('C:\\Users\\mdkafiluddin\\Desktop\\Research\\[1]DATASET_v1\\Category\\BOOK_AND_REF\\book_and_ref.csv',encoding="utf-8"))

# f_csv_x = f_csv
# f_csv_y = f_csv

# first_line = next(f_csv)
# print(first_line)

# #where is the word "category" in first line of the Dataset?
# count=0
# category=False

# while category is not True:
#     if first_line[count].upper()=='CATEGORY':
#         category= True
#     else:
#         count=count+1

# print("Category is in line position", count)


# """ Writing a file by using writer object"""
# def fileopener(filename_):
#     f=open(filename_,'a')
#     #print('i have opened a new file')
#     csv_writer= csv.writer(f)
#     return csv_writer   


# """ How many category in the Dataset?"""
# category_array=[]
# isMatch =False
 
# for row in islice(csv.reader(fd), 500, None):
#         print(row)

def text_cleaning(app_desc):
    app_desc=re.sub(r'([--:\w?@%&+~#=]*\.[a-z]{2,4}\/{0,2})((?:[?&](?:\w+)=(?:\w+))+|[--:\w?@%&+~#=]+)?', '', app_desc, flags=re.MULTILINE)
    app_desc = re.sub('<.*?>', ' ', app_desc)
    app_desc=re.sub(r'[^\w]',' ',app_desc)
    app_desc = re.sub( '\s+', ' ', app_desc ).strip()
    return app_desc


# count=0;

# for line in f_csv:
#     # count_=0
#     # print("++++++++++++++++++++++++++++")
#     # print(line['App_id'],"\n",line['Description'])
    
#     app_id=line['App_id']
#     app_desc_x=line['Description']
#     app_desc_x=text_cleaning(app_desc_x)
#     # print(app_id,"\n",app_desc)
#     print(app_id)

#     # f_csv_y.seek(0)
#     for line in islice(f_csv, count, None):
#         # print("++++++++++++++++++++++++++++")
#         # print(line['App_id'],"\n",line['Description'])
        
#         app_id=line['App_id']
#         app_desc_y=line['Description']
#         app_desc_y=text_cleaning(app_desc_y)
#         # print(app_id,"\n",app_desc)
#         print(app_id)

#         # count_=count_+1
#         # if count_==3:
#         #     break;

#     # f_csv_y=f_csv
#     count=count+1
#     if count==1:
#         break;
  
#         if isMatch is False:    
#             filename= dir_name+line[count]+'.csv'
#             #filename=os.path.join(dir_name,line[count])
#             csv_writer=fileopener(filename)
#             csv_writer.writerow(dict.fromkeys(line))
#             category_array.append(line[count])
#         isMatch =False      
#     else:
#         filename= dir_name+line[count]+'.csv'
#         #filename=os.path.join(dir_name,line[count])
#         csv_writer=fileopener(filename)
#         csv_writer.writerow(dict.fromkeys(line))
#         category_array.append(line[count])

# """ Printing all the categories in the Dataset"""
# print("Total number of categories in the Dataset is:",len(category_array))
# for x in range(len(category_array)):       
#     print (category_array[x])


# #filename= dir_name+'test.csv'
# #filename=os.path.join(dir_name,'abc.csv')
# #print(filename)



# """
# category_counter=0; 
# for line in f_csv:
#     if len(category_array)>0:
#         for x in range(len(category_array)):
#             if category_array[x]==line[count]:
#                 isMatch =True
#                 breaks
#         if isMatch is False:    
#             category_array.append(line[count])
            
#         isMatch =False      
#     else:
#         category_array.append(line[count])
#         path='C:/Users/mdkafiluddin/Desktop/Research/Dataset/UCLappA/'
#         filename=path+category_array[category_counter]
#         print(filename)
#         file_opener(filename)
    
    
# def file_opener(filename_):
#     with open(filename_,'w') as f:
#         csv_writer= csv.writer(f)
#     return csv_writer
# """





# # desc_file1= 'C:\\Users\\mdkafiluddin\\Desktop\\Research\\[1]DATASET_v1\\Category\\COMMUNICATION\\Experiment_1\\Five_Apps\\com.facebook.orca\\com.facebook.orca_description.txt'
# desc_file1= 'C:\\Users\\mdkafiluddin\\Desktop\\Research\\[1]DATASET_v1\\Category\\COMMUNICATION\\Experiment_1\\Five_Apps\\com.whatsapp\\com.whatsapp_description.txt'
# desc_f1 = open(desc_file1,'r', encoding="utf8")

# # desc_file2= 'C:\\Users\\mdkafiluddin\\Desktop\\Research\\[1]DATASET_v1\\Category\\COMMUNICATION\\Experiment_1\\Five_Apps\\com.skype.raider\\com.skype.raider_description.txt'
# desc_file2= 'C:\\Users\\mdkafiluddin\\Desktop\\Research\\[1]DATASET_v1\\Category\\COMMUNICATION\\Experiment_1\\Five_Apps\\com.tencent.mm\\com.tencent.mm_description.txt'
# desc_f2 = open(desc_file2,'r', encoding="utf8")


def w2v(s1,s2,wordmodel):
        if(s1==s2):
            return 1.0
        # s1words=s1.split()
        # print("----",s1words)
        # s2words=s2.split()
        # print("----",s2words)
        # s1wordsset=set(s1words)
        # s2wordsset=set(s2words)
        # print(s1wordsset)
        # print(s2wordsset)
        # vocab = wordmodel.vocab #the vocabulary considered in the word embeddings
        # if len(s1wordsset & s2wordsset)==0:
        #     return 0.0
        s1wordsset=set(s1)
        s2wordsset=set(s2)
        # print(s1wordsset)
        print(s2wordsset)
        vocab = wordmodel.vocab #the vocabulary considered in the word embeddings
        if len(s1wordsset & s2wordsset)==0:
            return 0.0
        # for word in s1wordsset.copy(): #remove sentence words not found in the vocab
        #     if (word not in vocab):
        #         print(word,"not in S1words vocab")
        #         s1words.remove(word)
        # for word in s2wordsset.copy(): #idem
        #     if (word not in vocab):
        #         print(word,"not ins S2words vocab")
        #         s2words.remove(word)
        # for word in s1words: #remove sentence words not found in the vocab
        #     if (word not in vocab):
        #         print(word,"not in S1words vocab")
        #         s1words.remove(word)
        # for word in s2words: #idem
        #     if (word not in vocab):
        #         print(word,"not ins S2words vocab")
        #         s2words.remove(word)
        # return wordmodel.n_similarity(s1words, s2words)

        # for word in s1: #remove sentence words not found in the vocab
        #     if (word not in vocab):
        #         # print(word,"not in S1words vocab")
        #         s1.remove(word)
        # for word in s2: #idem
        #     try:
        #         if (word not in vocab):
        #             print(word,"not in S2words vocab")
        #             s2.remove(word)
        #     except KeyError:
        #         print("error")


        s1 = [w for w in s1 if w in vocab]
        s2 = [w for w in s2 if w in vocab]  

        return wordmodel.n_similarity(s1, s2)






path_to_model = "C:/Kafil/Lab/Python/FE_SAFE.py/stanford-postagger-2016-10-31/models/english-bidirectional-distsim.tagger"
path_to_jar = "C:/Kafil/Lab/Python/FE_SAFE.py/stanford-postagger-2016-10-31/stanford-postagger.jar"

st_tagger = StanfordPOSTagger(path_to_model, path_to_jar)

def penn_to_wn(tag):
    """ Convert between a Penn Treebank tag to a simplified Wordnet tag """
    if tag.startswith('N'):
        return 'n'
 
    if tag.startswith('V'):
        return 'v'
 
    if tag.startswith('J'):
        return 'a'
 
    if tag.startswith('R'):
        return 'r'
 
    return None  #"""NONE creates error for wordnet uknown types"""
    # return 'n'
 
def tagged_to_synset(word, tag):
    wn_tag = penn_to_wn(tag)
    if wn_tag is None:
        return None
    try:
        return word
    except:
        return None
 
def sentence_processing(text):
    """ compute the sentence similarity using Wordnet """
    # Tokenize and tag
    #StanfordPOSTagger gives more accurate POS tag than NLTK pos_tag
    #pos_tag(word_tokenize(sentence1)) gives sometimes incorrect 
    #for example "snap selfies." and "snap selfies"
   #####################################################################

    # sentence1 = pos_tag(word_tokenize(sentence1))

    try:
        text=st_tagger.tag(word_tokenize(text))
    except:
        text = pos_tag(word_tokenize(text))


    # sentence1 = [nltk.WordNetLemmatizer().lemmatize(*tagged_word) for tagged_word in sentence1]

    # print(text)
    
    # sentence2 = pos_tag(word_tokenize(sentence2))
    # sentence2=st_tagger.tag(word_tokenize(sentence2))
    # # sentence2 = [nltk.WordNetLemmatizer().lemmatize(*tagged_word) for tagged_word in sentence2]
    # print(sentence2)
    
    # Get the synsets for the tagged words
    #################################################

    # synsets1=[]
    # synsets2=[]
    # for tagged_word in sentence1:
    #     print(tagged_word)
    #     tagged_word = list(tagged_word)
    #     synsets1.append(tagged_to_synset(tagged_word[0],tagged_word[1]))
    # for tagged_word in sentence2:
    #     print(tagged_word)
    #     tagged_word = list(tagged_word)
    #     print(tagged_word)
    #     synsets2.append(tagged_to_synset(tagged_word[0],tagged_word[1]))

    # The code above is the elaboration of code below
    
    synsets1 = [tagged_to_synset(*tagged_word) for tagged_word in text]
    # synsets2 = [tagged_to_synset(*tagged_word) for tagged_word in sentence2]
 
    # Filter out the Nones in the synonym set
    text = [ss for ss in synsets1 if ss]
    # synsets2 = [ss for ss in synsets2 if ss]
 
    # print(type(text))
    # text = str(text)
    # print(text)
    # print(synsets2)
    

    ##REMOVE STOP WORDS###
    stop_words = set(stopwords.words('english')) 
    text = [w for w in text if not w in stop_words] 
    # text1=str(text1)

    ###REMOVE DUPLICATES
    text = list(dict.fromkeys(text))

    ###REMOVE words in my custom dictionary
    my_custom_dict =["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
    "http",
    "https",
    "inc",
    "etc",
    "able",
    "typical",
    "yet",
    "otherwise",
    "welcome",
    "none",
    "done",
    "ago",
    "recently",
    "still",
    "wait",
    "today",
    "soon",
    "always", 
    "app",
    "also", 
    "even",
    "ever",
    "available", 
    "please",
    "much",
    "almost",
    "many"]
    
    text = [w for w in text if not w in my_custom_dict] 
    print(text)
    return text
    

""" Writing a file by using writer object"""
def fileopener(filename_):

    csvfile=open(filename_,'a',newline='')
    fieldnames = ['AppID','Functional_similarity', 'Rating', 'Downloads']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    return writer   

if __name__ == '__main__':
    #+++++++Working Model-1+++++++++++
    #+++++++++++++++++++++++++++++++++++++++++++
    # wordmodelfile="C:/Users/mdkafiluddin/Downloads/GoogleNews-vectors-negative300.bin.gz"
    # wordmodel=word2vec.KeyedVectors.load_word2vec_format(wordmodelfile, binary=True, limit=500000)
    
    #+++++++Working Model-2+++++++++++
    #+++++++++++++++++++++++++++++++++++++++++++
    wordmodelfile="C:/Users/mdkafiluddin/Downloads/wiki.en.vec"
    wordmodel=word2vec.KeyedVectors.load_word2vec_format(wordmodelfile, binary=False, limit=500000)
    
    #+++++++Working Model-3+++++++++++
    #+++++++++++++++++++++++++++++++++++++++++++    
    # wordmodelfile="C:/Users/mdkafiluddin/Downloads/cc.en.300.vec.gz"
    # wordmodel=word2vec.KeyedVectors.load_word2vec_format(wordmodelfile, binary=False, limit=500000)

    #+++++++ERROR: Working Model-4+++++++++++
    # wordmodelfile="C:/Users/mdkafiluddin/Downyloads/fastText.cc.en.300.bin.gz"
    # wordmodel=word2vec.KeyedVectors.load_word2vec_format(wordmodelfile, binary=True, limit=500000)

    dir_name='C:\\Users\\mdkafiluddin\\Desktop\\Research\\Dataset\\GooglePlay2020\\Communication\\comm_top_free'
    with open('C:\\Users\\mdkafiluddin\\Desktop\\Research\\Dataset\\GooglePlay2020\\Communication\\comm_top_free\\app_desc_competitors.csv', encoding='utf-8',errors='ignore') as f_a:
        f_csv_a = csv.DictReader(f_a)
        for line_a in f_csv_a:
            app_id=line_a['AppID']
            print("+++",app_id)
            filename= dir_name+'\\'+'target_'+line_a['AppID']+'.csv'
            csv_writer=fileopener(filename)
            app_desc_x=line_a['Description']
            app_desc_x=text_cleaning(app_desc_x)
            app_desc_x=sentence_processing(app_desc_x.lower())
            with open('C:\\Users\\mdkafiluddin\\Desktop\\Research\\Dataset\\GooglePlay2020\\Communication\\comm_top_free\\app_desc.csv', encoding='utf-8',errors='ignore') as f_b:
                f_csv_b = csv.DictReader(f_b)
                for line_b in f_csv_b:
                    app_id_b=line_b['AppID']
                    print(app_id_b)
                    app_desc_y=line_b['Description']
                    app_desc_y=text_cleaning(app_desc_y)
                    app_desc_y=sentence_processing(app_desc_y.lower())
                    app_simi_score=w2v(app_desc_x,app_desc_y,wordmodel)
                    print("sim(description_1,description_2) = ", app_simi_score,"/1.")
                    csv_writer.writerow({'AppID':line_b['AppID'],'Functional_similarity':app_simi_score,'Rating':line_b['AppRating'], 'Downloads':line_b['MinInstalls']})

    
    # f_csv = csv.DictReader(open('C:\\Users\\mdkafiluddin\\Desktop\\Research\\[1]DATASET_v1\\Category\\BOOK_AND_REF\\book_and_ref_competitors.csv', encoding="utf-8"))
    # f_csv_weather = csv.DictReader(open('C:\\Users\\mdkafiluddin\\Desktop\\Research\\[1]DATASET_v1\\Category\\BOOK_AND_REF\\book_and_ref.csv',encoding="utf-8"))
    

    # for line in f_csv:
    #     # count_=0
    #     # print("++++++++++++++++++++++++++++")
    #     # print(line['App_id'],"\n",line['Description'])
        
    #     app_id=line['App_id']
    #     # app_desc_x=line['Description']
    #     # app_desc_x=text_cleaning(app_desc_x)
    #     # app_desc_x=sentence_processing(app_desc_x.lower())
    #     # print(app_id,"\n",app_desc)
    #     print("+++",app_id)
    #     count=0;
    #     # f_csv_y.seek(0)
    #     for line_y in islice(f_csv_weather, count, None):
    #     # for line_y in f_csv_weather:
    #         # print("++++++++++++++++++++++++++++")
    #         # print(line['App_id'],"\n",line['Description'])
            
    #         app_id=line_y['App_id']
    #         # app_desc_y=line_y['Description']
    #         # app_desc_y=text_cleaning(app_desc_y)
    #         # print(app_id,"\n",app_desc)

    #         print(app_id)
        # f_csv_weather.seek(0)    
            # app_desc_y=sentence_processing(app_desc_y.lower())
            # print("sim(description_1,description_2) = ", w2v(app_desc_x,app_desc_y,wordmodel),"/1.")
            # count_=count_+1
            # if count_==6:
            #     break;

        # f_csv_y=f_csv
        # count=count+1
        # if count==1:
        #     break;

    # text1=desc_f1.read();
    
    # text1=re.sub(r'([--:\w?@%&+~#=]*\.[a-z]{2,4}\/{0,2})((?:[?&](?:\w+)=(?:\w+))+|[--:\w?@%&+~#=]+)?', '', text1, flags=re.MULTILINE)
    # text1=re.sub(r'[^\w]',' ',text1)
    # print(text1)

    # text2=desc_f2.read();
    # text2=re.sub(r'([--:\w?@%&+~#=]*\.[a-z]{2,4}\/{0,2})((?:[?&](?:\w+)=(?:\w+))+|[--:\w?@%&+~#=]+)?', '', text2, flags=re.MULTILINE)
    # text2=re.sub(r'[^\w]',' ',text2)
    # print(text2)

    # text1=sentence_processing(text1.lower())
    # text2=sentence_processing(text2.lower())

    # stop_words = set(stopwords.words('english')) 
    # word_tokens = word_tokenize(text1) 
    # text1 = [w for w in word_tokens if not w in stop_words] 
    # text1=str(text1)
    # print(text1)
    
    # word_tokens = word_tokenize(text2) 
    # text2 = [w for w in word_tokens if not w in stop_words]
    # text2=str(text2)
    # print(text2)

    # print("sim(description_1,description_2) = ", w2v("Instantly just reach the people in your life for free","Say just hello to friends and family with an instant message",wordmodel),"/1.")
    # print("sim(description_1,description_2) = ", w2v(text1,text2,wordmodel),"/1.")


