import pandas as pd
import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.stem.porter import *
import numpy as np
np.random.seed(2018)
import nltk
nltk.download('wordnet')
from tokenize import tokenize

def lemmatize_stemming(text):
    return stemmer.stem(WordNetLemmatizer().lemmatize(text, pos='v'))
def preprocess(text):
    result = []
    for token in gensim.utils.simple_preprocess(text):
        if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
            result.append(lemmatize_stemming(token))
    return result



if __name__ == '__main__':

	data = pd.read_csv('H:\\Research\\GooglePlayApps\\Communication\\comm_top_free\\cleanedText.csv', error_bad_lines=False);
	data_text = data[['Functional_Features']]
	# data_text['index'] = data_text.index
	# documents = data_text
	print(type(data_text))
	tokens = tokenize.tokenize(data_text)
	dictionary = gensim.corpora.Dictionary(tokens)
	# count = 0
	# for k, v in dictionary.iteritems():
	#     print(k, v)
	#     count += 1
	#     if count > 10:
	#         break