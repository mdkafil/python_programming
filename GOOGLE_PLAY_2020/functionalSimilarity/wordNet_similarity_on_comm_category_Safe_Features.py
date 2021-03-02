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
 
    return 'n'
 
def tagged_to_synset(word, tag):
    wn_tag = penn_to_wn(tag)
    if wn_tag is None:
        return None
    try:
        return wn.synsets(word, wn_tag)[0]
    except:
        return None
 
def wordNet_similarity(sentence1, sentence2):
    """ compute the sentence similarity using Wordnet """
    # Tokenize and tag
    
    # sentence1 = pos_tag(word_tokenize(sentence1))
    sentence1=st_tagger.tag(word_tokenize(sentence1))
    
    # sentence2 = pos_tag(word_tokenize(sentence2))
    sentence2=st_tagger.tag(word_tokenize(sentence2))

    
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
    synsets1 = [tagged_to_synset(*tagged_word) for tagged_word in sentence1]
    synsets2 = [tagged_to_synset(*tagged_word) for tagged_word in sentence2]
 
    # Filter out the Nones in the synonym set
    synsets1 = [ss for ss in synsets1 if ss]
    synsets2 = [ss for ss in synsets2 if ss]
 
    score, count = 0.0, 0
 
###########################################################################
    # for syn1 in synsets1:
    #     arr_simi_score = []
    #     print('=========================================')
    #     print(syn1)
    #     print('----------------')
    # for syn2 in synsets2:
    #     print(syn2)
    #     simi_score = syn1.path_similarity(syn2)
    #     print(simi_score)
    #     if simi_score is not None:
    #         arr_simi_score.append(simi_score)
    #         print('----------------')
    #         print(arr_simi_score)
    #     if(len(arr_simi_score) > 0):
    #         best = max(arr_simi_score)
    #         print(best)
    #         score += best
    #         count += 1
    #         # Average the values
    #         print('score: ', score)
    #         print('count: ', count)
    #         score /= count

###########################################################################

    for syn1 in synsets1:
        arr_simi_score = []
        # print('=========================================')
        print("Each word from Synonym se1",syn1)
        # print('----------------')
        for syn2 in synsets2:
            print("Each word from Synonym se2",syn2)
            # simi_score = syn1.path_similarity(syn2)
            simi_score = syn1.wup_similarity(syn2)
            print("word to word path_similarity score",simi_score)
            if simi_score is not None:
                arr_simi_score.append(simi_score)
                print('----------------')
                print(arr_simi_score)
        if(len(arr_simi_score) > 0):
            best = max(arr_simi_score)
            print("best score so far", best)
            score += best
            count += 1
    # Average the values
    print('score: ', score)
    print('count: ', count)
    if count!=0:
        score /= count
    else:
        score=0.0
    return score



def text_cleaning(app_desc):
    app_desc = str(app_desc)
    app_desc=app_desc.replace('\\n','')  # Cool Cleaning stuff use of '\\'
    app_desc=re.sub(r'([--:\w?@%&+~#=]*\.[a-z]{2,4}\/{0,2})((?:[?&](?:\w+)=(?:\w+))+|[--:\w?@%&+~#=]+)?', '', app_desc, flags=re.MULTILINE)
    app_desc = re.sub(r'<.*?>', ' ', app_desc)
    app_desc=re.sub(r'[^[a-zA-z ]+]*', ' ',app_desc)
    app_desc=re.sub(r'[^\w]', ' ',app_desc)
    app_desc = re.sub(r'\s+', ' ', app_desc).strip()
    return app_desc


 
"""STOP WORD removal"""
def stop_word_removal(text):
    stop_words = set(stopwords.words('english')) 
    # word_tokens = word_tokenize(text) 
    text = [w for w in text if not w in stop_words] 
    # text=str(text)
    print(text)
    return text 




""" Writing a file by using writer object"""
def fileopener(filename_):
    csvfile=open(filename_,'a',newline='')
    fieldnames = ['AppID','Functional_similarity']
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
    # wordmodelfile="C:/Users/mdkafiluddin/Downloads/wiki.en.vec"
    # wordmodel=word2vec.KeyedVectors.load_word2vec_format(wordmodelfile, binary=False, encoding='utf8', limit=500000)
    
    #+++++++Working Model-3+++++++++++
    #+++++++++++++++++++++++++++++++++++++++++++    
    # wordmodelfile="C:/Users/mdkafiluddin/Downloads/cc.en.300.vec.gz"
    # wordmodel=word2vec.KeyedVectors.load_word2vec_format(wordmodelfile, binary=False, limit=500000)

    #+++++++ERROR: Working Model-4+++++++++++
    # wordmodelfile="C:/Users/mdkafiluddin/Downyloads/fastText.cc.en.300.bin.gz"
    # wordmodel=word2vec.KeyedVectors.load_word2vec_format(wordmodelfile, binary=True, limit=500000)

##############FACEBOOK Feature Classification##########################################

    # file_name='C:\\Users\\mdkafiluddin\\Desktop\\Research\\Experiments\\RQ2\\facebook\\feature_classification\\popular_features_scores1.csv'
    # csv_writer=fileopener(file_name)
    # count=0
    # # f_reviews= csv.DictReader(open('C:\\Users\\mdkafiluddin\\Desktop\\Research\\Experiments\\RQ2\\facebook\\feature_classification\\popular_features.csv', encoding="utf-8", errors="ignore"))
    # f_whatsnew= open('C:\\Users\\mdkafiluddin\\Desktop\\Research\\Experiments\\RQ2\\facebook\\facebook_whatsnew_features.txt', encoding="utf-8", errors="ignore")
    
    # similarity_threshold =0.6
    

    # whatsnew_text = f_whatsnew.readlines()
    # for _feature in whatsnew_text:
    #     count=count+1
    #     whatsnew_feature=text_cleaning(_feature)
    #     print(count,": whatsnew_feature")
    #     with open('C:\\Users\\mdkafiluddin\\Desktop\\Research\\Experiments\\RQ2\\facebook\\feature_classification\\popular_features.csv', encoding="utf-8", errors="ignore") as file:
    #         f_reviews=csv.DictReader(file)
    #         for line in f_reviews:
    #             feature_set = line["Features"].split(",")
    #             for feature in feature_set:
    #                 rev_feature=text_cleaning(feature)
    #                 print(rev_feature)
    #                 simi_score=sentence_similarity(whatsnew_feature,rev_feature)
    #                 if simi_score>=similarity_threshold:
    #                     csv_writer.writerow({'WN_Feature_No':count,'WN_Feature':whatsnew_feature,'Rev_Feature':rev_feature,'Rev_Sentiment':line["Pos_Sen"], 'Similarity_Score':simi_score})


    dir_name='C:\\Users\\mdkafiluddin\\Desktop\\Research\\Dataset\\GooglePlay2020\\Communication\\comm_top_free'
    with open('C:\\Users\\mdkafiluddin\\Desktop\\Research\\Dataset\\GooglePlay2020\\Communication\\comm_top_free\\cleanedText_competitors.csv', encoding='utf-8',errors='ignore') as f_a:
        f_csv_a = csv.DictReader(f_a)
        for line_a in f_csv_a:
            app_id=line_a['AppID']
            print("+++",app_id)
            filename= dir_name+'\\'+'target_'+line_a['AppID']+'_wordNet_cleanedText.csv'
            csv_writer=fileopener(filename)
            app_desc_x=line_a['Functional_Features']
            app_desc_x=text_cleaning(app_desc_x)
            # app_desc_x=sentence_processing(app_desc_x.lower())
            with open('C:\\Users\\mdkafiluddin\\Desktop\\Research\\Dataset\\GooglePlay2020\\Communication\\comm_top_free\\cleanedText.csv', encoding='utf-8',errors='ignore') as f_b:
                f_csv_b = csv.DictReader(f_b)
                for line_b in f_csv_b:
                    app_id_b=line_b['AppID']
                    print(app_id_b)
                    app_desc_y=line_b['Functional_Features']
                    app_desc_y=text_cleaning(app_desc_y)
                    # app_desc_y=sentence_processing(app_desc_y.lower())
                    app_simi_score=wordNet_similarity(app_desc_x,app_desc_y)
                    print("sim(description_1,description_2) = ", app_simi_score,"/1.")
                    csv_writer.writerow({'AppID':line_b['AppID'],'Functional_similarity':app_simi_score})




















            
                    
    #                 highest_score=app_simi_score
    #                 print("Score/feature: ",highest_score)

    #         # print("sim(description_1,description_2) = ", app_simi_score,"/1.")
    #         print("+++Highest Score/review: ",highest_score)
    #         


##############SKYPE##########################################

#     file_name='C:\\Users\\mdkafiluddin\\Desktop\\Research\\Experiments\\RQ2\\skype\\skype_relevance_with_review_features_to_all_whatsnew_features_combined.csv'
#     csv_writer=fileopener(file_name)
#     count=1
#     f_whatsnew= open('C:\\Users\\mdkafiluddin\\Desktop\\Research\\Experiments\\RQ2\\skype\\skype_whatsnew_features.txt', encoding="utf-8", errors="ignore")
#     whatsnew_text = f_whatsnew.readlines()
#     app_desc_x=text_cleaning(whatsnew_text)
#     app_desc_x=sentence_processing(app_desc_x.lower())
#     app_desc_x=stop_word_removal(app_desc_x)
#     print(app_desc_x)

#     with open('C:\\Users\\mdkafiluddin\\Desktop\\Research\\Experiments\\RQ2\\skype\\skype_review_features.txt', encoding="utf-8", errors="ignore") as f_reviews:
#         for line in f_reviews:
#             # print("---",line)
#             highest_score =0
#             feature_set = line.split(",")
#             for feature in feature_set:
#                 # print("***",feature)
#                 app_desc_y=text_cleaning(feature)
#                 app_desc_y=sentence_processing(app_desc_y.lower())
#                 app_desc_y=stop_word_removal(app_desc_y)
#                 print(app_desc_y)

#                 app_simi_score=w2v(app_desc_x,app_desc_y,wordmodel)
#                 if app_simi_score>highest_score:
#                     highest_score=app_simi_score
#                     print("Score/feature: ",highest_score)

#             # print("sim(description_1,description_2) = ", app_simi_score,"/1.")
#             print("+++Highest Score/review: ",highest_score)
#             csv_writer.writerow({'Review_No':count,'WN_Similarity_Score':highest_score})
#             count=count+1

# ##############WECHAT##########################################

#     file_name='C:\\Users\\mdkafiluddin\\Desktop\\Research\\Experiments\\RQ2\\wechat\\wechat_relevance_with_review_features_to_all_whatsnew_features_combined.csv'
#     csv_writer=fileopener(file_name)
#     count=1
#     f_whatsnew= open('C:\\Users\\mdkafiluddin\\Desktop\\Research\\Experiments\\RQ2\\wechat\\wechat_whatsnew_features.txt', encoding="utf-8", errors="ignore")
#     whatsnew_text = f_whatsnew.readlines()
#     app_desc_x=text_cleaning(whatsnew_text)
#     app_desc_x=sentence_processing(app_desc_x.lower())
#     app_desc_x=stop_word_removal(app_desc_x)
#     print(app_desc_x)

#     with open('C:\\Users\\mdkafiluddin\\Desktop\\Research\\Experiments\\RQ2\\wechat\\wechat_review_features.txt', encoding="utf-8", errors="ignore") as f_reviews:
#         for line in f_reviews:
#             # print("---",line)
#             highest_score =0
#             feature_set = line.split(",")
#             for feature in feature_set:
#                 # print("***",feature)
#                 app_desc_y=text_cleaning(feature)
#                 app_desc_y=sentence_processing(app_desc_y.lower())
#                 app_desc_y=stop_word_removal(app_desc_y)
#                 print(app_desc_y)

#                 app_simi_score=w2v(app_desc_x,app_desc_y,wordmodel)
#                 if app_simi_score>highest_score:
#                     highest_score=app_simi_score
#                     print("Score/feature: ",highest_score)

#             # print("sim(description_1,description_2) = ", app_simi_score,"/1.")
#             print("+++Highest Score/review: ",highest_score)
#             csv_writer.writerow({'Review_No':count,'WN_Similarity_Score':highest_score})
#             count=count+1

# ##############WHATSAPP##########################################

#     file_name='C:\\Users\\mdkafiluddin\\Desktop\\Research\\Experiments\\RQ2\\whatsapp\\whatsapp_relevance_with_review_features_to_all_whatsnew_features_combined.csv'
#     csv_writer=fileopener(file_name)
#     count=1
#     f_whatsnew= open('C:\\Users\\mdkafiluddin\\Desktop\\Research\\Experiments\\RQ2\\whatsapp\\whatsapp_whatsnew_features.txt', encoding="utf-8", errors="ignore")
#     whatsnew_text = f_whatsnew.readlines()
#     app_desc_x=text_cleaning(whatsnew_text)
#     app_desc_x=sentence_processing(app_desc_x.lower())
#     app_desc_x=stop_word_removal(app_desc_x)
#     print(app_desc_x)

#     with open('C:\\Users\\mdkafiluddin\\Desktop\\Research\\Experiments\\RQ2\\whatsapp\\whatsapp_review_features.txt', encoding="utf-8", errors="ignore") as f_reviews:
#         for line in f_reviews:
#             # print("---",line)
#             highest_score =0
#             feature_set = line.split(",")
#             for feature in feature_set:
#                 # print("***",feature)
#                 app_desc_y=text_cleaning(feature)
#                 app_desc_y=sentence_processing(app_desc_y.lower())
#                 app_desc_y=stop_word_removal(app_desc_y)
#                 print(app_desc_y)

#                 app_simi_score=w2v(app_desc_x,app_desc_y,wordmodel)
#                 if app_simi_score>highest_score:
#                     highest_score=app_simi_score
#                     print("Score/feature: ",highest_score)

#             # print("sim(description_1,description_2) = ", app_simi_score,"/1.")
#             print("+++Highest Score/review: ",highest_score)
#             csv_writer.writerow({'Review_No':count,'WN_Similarity_Score':highest_score})
#             count=count+1

    # with open('C:\\Users\\mdkafiluddin\\Desktop\\Research\\Experiments\\RQ2\\facebook\\facebook_whatsnew.txt', encoding="utf-8", errors="ignore") as f_whatsnew:
    #     for line in f_whatsnew:
    #         print("+++",line)
    #         app_desc_x=text_cleaning(line)
    #         app_desc_x=sentence_processing(app_desc_x.lower())
    #         app_desc_x=stop_word_removal(app_desc_x)
            # print(app_desc_x)
                
            # with open('C:\\Users\\mdkafiluddin\\Desktop\\Research\\Experiments\\RQ2\\facebook\\facebook_reviews.txt', encoding="utf-8", errors="ignore") as f_reviews:
            #     for line in f_reviews:
            #         print("---",line)
            #         app_desc_y=text_cleaning(line)
            #         app_desc_y=sentence_processing(app_desc_y.lower())
            #         # app_desc_y=stop_word_removal(app_desc_y)

            #         app_simi_score=w2v(app_desc_x,app_desc_y,wordmodel)
            #         print("sim(description_1,description_2) = ", app_simi_score,"/1.")
            #         csv_writer.writerow({'Review_No':count,'WN_Similarity_Score':app_simi_score})
            #         count=count+1

    
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


