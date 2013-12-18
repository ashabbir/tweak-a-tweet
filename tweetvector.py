import re
import csv
import shutil
import os
import string
from gensim import corpora, models, similarities

dictionary = corpora.dictionary.Dictionary.load('/Projects/tweets.dict')
##bad_chars = '()[]'
withid = open('/Projects/VisualClustering/tweets/tweets-labeled/tweets-013.txt')

lines = f.readlines()

noid = open('/Projects/VisualClustering/textOnly-tweet-013.txt','w')
for line in lines:
    index = line.find(',')
    tweettext = line[index+1:len(line)]
    w.write(tweettext)

noid.close()
withid.close()

class MyCorpus(object):
    def __iter__(self):
        for line in open('/Projects/VisualClustering/textOnly-tweet-013.txt'):
            # assume there's one document per line, tokens separated by whitespace
            yield dictionary.doc2bow(line.lower().split())

w = open('/Projects/VisualClustering/VectorOnly-tweet-013.txt','wb')           

corpus_memory_friendly = MyCorpus()
print corpus_memory_friendly
for vector in corpus_memory_friendly:
##    print str(vector).strip('(').strip(')')
    line = re.sub('[\[(\ )\]]', '', str(vector))
    print line
    w.write(line+'\n')

w.close()

##b = open('v11.csv', 'w')
##a = csv.writer(b)
##for count in range(0,30):
##    a.writerow([0 for col in range(0,856)])
##b.close()
##    

shutil.copy('/Projects/VisualClustering/VectorOnly-tweet-011.txt','/Projects/VisualClustering/Copied13.txt')
os.rename('/Projects/VisualClustering/Copied11.txt','/Projects/VisualClustering/Copied13.csv')
