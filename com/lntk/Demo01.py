# coding=utf-8
import nltk;
import jieba;

porter = nltk.PorterStemmer()
print(porter.stem('lying')) #'lie'

lema=nltk.WordNetLemmatizer()
print (lema.lemmatize('women'))   #'woman'



