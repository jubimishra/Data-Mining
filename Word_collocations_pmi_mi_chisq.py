
# coding: utf-8

# ##Question 1 : Word Collocations

# ### Used Tweet Tokenizer in nltk to tokenize the tweets. The strip handler parameter removes the twitter user handles.

# In[135]:

import pandas as pd
import math
import nltk
from nltk.collocations import *
from nltk.tokenize.casual import TweetTokenizer
from collections import Counter
import string
import re
import csv
import math


# In[138]:

tweets=pd.read_csv('tweets.txt', header=None, names='t')
print tweets.head()


# In[144]:

tknzr = TweetTokenizer(strip_handles=True, preserve_case=False)
unigram_freq=Counter()
bigram_freq=Counter()

for tweet in tweets.t:
    tokens= tknzr.tokenize(str(tweet))
    bigram_tuples=list(nltk.bigrams(tokens))
    unigram_freq.update(tokens)
    bigram_freq.update(bigram_tuples)


total_unigram_freq=sum(unigram_freq.values())
unique_unigrams=len(unigram_freq.keys())
total_bigram_freq=sum(bigram_freq.values())
unique_bigrams=len(bigram_freq.keys())
print "Size of the corpus : ", total_unigram_freq
print "Number of unique words : ",unique_unigrams
print "Total number of bigrams : ",total_bigram_freq
print "Number of unique bigrams : ", unique_bigrams


# ###Point wise Mutual Information

# In[145]:

def pmi(unigram_freq, bigram_freq,n):
    pmi_list=[]
    for bigram in bigram_freq:
        prob_word1 = unigram_freq[bigram[0]]
        prob_word2 = unigram_freq[bigram[1]] 
        prob_word1_word2 = bigram_freq[bigram]
        pmi_score= math.log(prob_word1_word2/float(prob_word1*prob_word2)) 
        pmi_list.append([bigram,pmi_score, bigram[0],prob_word1, bigram[1],prob_word2])
    pmi_sorted=sorted(pmi_list, key=lambda key_value: key_value[1], reverse=True)
    return pmi_sorted[0:n]

print pmi(unigram_freq, bigram_freq,100)


# ###Mutual Information

# In[149]:

def mi(unigram_freq, bigram_freq,n):
    mi_list=[]
    NB=float(sum(bigram_freq.values()))
    NU=float(sum(unigram_freq.values()))
    for bigram in bigram_freq:
        XY=bigram_freq[bigram]
        XYB=unigram_freq[bigram[0]]-bigram_freq[bigram]
        XBY=unigram_freq[bigram[1]]-bigram_freq[bigram]
        XBYB= NB-XY-XYB-XBY
        X=unigram_freq[bigram[0]]
        Y=unigram_freq[bigram[1]]
        XB=NU-X
        YB=NU-Y
        try:
            mi1=XY*math.log(XY/float(X*Y))
        except:
            mi1=0.0
        try:
            mi2=XYB*math.log(XYB/float(X*YB))
        except:
            mi2=0.0
        try:
            mi3=XBY*math.log(XBY/float(XB*Y))
        except:
            mi3=0.0
        try:
            mi4=XBYB*math.log(XBYB/float(XB*YB))
        except:
            mi4=0.0
            
        mi_score=mi1+mi2+mi3+mi4  
        mi_list.append([bigram,mi_score, bigram[0],X, bigram[1],Y])
    mi_sorted=sorted(mi_list, key=lambda key_value: key_value[1], reverse=True)
    return mi_sorted[0:n]

print mi(unigram_freq, bigram_freq,100)


# ###Chi Square 

# In[151]:

def chi_sq(unigram_freq, bigram_freq,n):
    chisq=[]
    N=float(sum(bigram_freq.values()))
    for bigram in bigram_freq:
        A=bigram_freq[bigram]
        B=unigram_freq[bigram[0]]-bigram_freq[bigram]
        C=unigram_freq[bigram[1]]-bigram_freq[bigram]
        D= N-A-B-C
        num=(N *pow(((A*D)-(B*C)),2))
        denom=(A+C)*(B+D)*(A+B)*(C+D)
        chi_score= num/denom

        chisq.append([bigram,chi_score, bigram[0],unigram_freq[bigram[0]], bigram[1],unigram_freq[bigram[1]]])
    chi_sorted=sorted(chisq, key=lambda key_value: key_value[1], reverse=True)
    return chi_sorted[0:n]
    

print chi_sq(unigram_freq, bigram_freq,100)


# ###It can be seen that the results from the three measures - pmi, mi and chi square are different.
# ###*Upon compariison of the results from the three measures, it can be seen that the mutual information measure does a better job of finding the top ten word collocations which actually make sense together and are most often used together. Also, their individual frequencies are higher and MI considers the weighted sum of probabilities.
# ###By the definition of Mutual Information, a high value should mean that one feature gives a lot of information about the other and by the definition of Chi Square, a high value of Chi Square means that the two features must be dependent.
# 

