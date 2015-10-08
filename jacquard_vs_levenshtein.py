#Spelling Correction

# In[161]:

import nltk
from nltk.metrics import *
from nltk.util import ngrams
def jacquard_trigram(query):
    final=[]
    for a in file('enwiktionary.a.list'):
        a=a.rstrip()
        trigram=set(nltk.trigrams(a))
        q_trigram=set(nltk.trigrams(query))
        intersect=q_trigram.intersection(trigram)
        union=q_trigram.union(trigram)
        sim=float(len(intersect))/len(union)
        
        final.append([a,sim])
    final_sorted= sorted(final,key=lambda sim:sim[1], reverse=True)
    print final_sorted[:10]
    
def jacquard_bigram(query):
    final=[]
    for a in file('enwiktionary.a.list'):
        a=a.rstrip()
        bigram=set(nltk.bigrams(a))
        q_bigram=set(nltk.bigrams(query))
        intersect=q_bigram.intersection(bigram)
        union=q_bigram.union(bigram)
        sim=float(len(intersect))/len(union)
        
        final.append([a,sim])
    final_sorted= sorted(final,key=lambda sim:sim[1], reverse=True)
    print final_sorted[:10]
    
def jacquard_fourgram(query):
    final=[]
    n=4
    for a in file('enwiktionary.a.list'):
        a=a.rstrip()
        fourgram=set(nltk.ngrams(a,4))
        q_fourgram=set(nltk.ngrams(query,4))
        intersect=q_fourgram.intersection(fourgram)
        union=q_fourgram.union(fourgram)
        sim=float(len(intersect))/len(union)
        
        final.append([a,sim])
    final_sorted= sorted(final,key=lambda sim:sim[1], reverse=True)
    print final_sorted[:10]
    
def jacquard_fivegram(query):
    final=[]
    n=4
    for a in file('enwiktionary.a.list'):
        a=a.rstrip()
        fivegram=set(nltk.ngrams(a,5))
        q_fivegram=set(nltk.ngrams(query,5))
        intersect=q_fivegram.intersection(fivegram)
        union=q_fivegram.union(fivegram)
        sim=float(len(intersect))/len(union)
        
        final.append([a,sim])
    final_sorted= sorted(final,key=lambda sim:sim[1], reverse=True)
    print final_sorted[:10]

def leven_dist(word):
    leven=[]
    for a in file('enwiktionary.a.list'):
        a=a.rstrip()
        score=edit_distance(word,a)
        leven.append([a,score])
    leven_sorted= sorted(leven,key=lambda score:score[1])
    print leven_sorted[:10]  


# In[162]:

query=["abreviation", "abstrictiveness", "accanthopterigious", "artifitial inteligwnse", "agglumetation"]
for word in query:
    print "The top ten words based on Jacquard similarity(5grams) of "+ word+ " are:\n"
    jacquard_fivegram(word)
    print "\n"
    print "The top ten words based on Jacquard similarity(4grams) of "+ word+ " are:\n"
    jacquard_fourgram(word)
    print "\n"
    print "The top ten words based on Jacquard similarity(trigrams) of "+ word+ " are:\n"
    jacquard_trigram(word)
    print "\n"
    print "The top ten words based on Jacquard similarity(bigrams) of "+ word+ " are:\n"
    jacquard_bigram(word)
    print "\n"
    print "The top ten words based on Levenshtein edit distance of "+ word+ " are:\n"
    leven_dist(word)
    print "\n"


# ### While comparing the jacquard similarities for various n grams it can be observed that bigrams give a better approximation.
