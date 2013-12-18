import re
import csv
import shutil
import os
import string
from gensim import corpora, models, similarities

path = "/Projects/VisualClustering/tweets/twirank-selected/"
dirs = os.listdir( path )
dictionary = corpora.dictionary.Dictionary.load('/Projects/tweets.dict')
##bad_chars = '()[]'

for cat in dirs:
    if not cat.startswith('.') and os.path.isfile(os.path.join(path, cat)):
        filename = os.path.splitext(cat)[0]
        withid = open('/Projects/VisualClustering/tweets/twirank-selected/'+filename+'.txt')

        lines = withid.readlines()

        noid = open('/Projects/VisualClustering/text/twirank/textOnly-'+filename+'.txt','w')
        for line in lines:
            index = line.find(',')
            tweettext = line[index+1:len(line)]
            noid.write(tweettext)

        noid.close()
        withid.close()

        class MyCorpus(object):
            def __iter__(self):
                for line in open('/Projects/VisualClustering/text/twirank/textOnly-'+filename+'.txt'):
                    # assume there's one document per line, tokens separated by whitespace
                    yield dictionary.doc2bow(line.lower().split())

        w = open('/Projects/VisualClustering/vectors/twirank/VectorOnly-'+filename+'.txt','wb')           

        corpus_memory_friendly = MyCorpus()
        print corpus_memory_friendly
        for vector in corpus_memory_friendly:
        ##    print str(vector).strip('(').strip(')')
            line = re.sub('[\[(\ )\]]', '', str(vector))
            w.write(line+'\n')

        w.close()

        shutil.copy('/Projects/VisualClustering/vectors/twirank/VectorOnly-'+filename+'.txt','/Projects/VisualClustering/vectors/twirank/Copied-'+filename+'.txt')
        os.rename('/Projects/VisualClustering/vectors/twirank/Copied-'+filename+'.txt','/Projects/VisualClustering/vectors/twirank/Copied-'+filename+'.csv')

        arr = [0 for col in range(0,8839)]
        arr[0] = filename

        in_file = open("/Projects/VisualClustering/vectors/twirank/Copied-"+filename+".csv", "rb")
        reader = csv.reader(in_file)
        out_file = open("master-twirank.csv", "a")
        writer = csv.writer(out_file)
        for row in reader:
            arr = [0 for col in range(0,8839)]
            for j in range(0,len(row)):
                if j%2==0:
                    arr[int(row[j])] = int(row[j+1])
            arr[0] = filename
            print arr[0]
            writer.writerow(arr)
        in_file.close()    
        out_file.close()
