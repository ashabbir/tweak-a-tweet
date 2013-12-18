import re
import csv
import shutil
import os
import string


in_file = open("/Projects/VisualClustering/Latest/readall.csv", "rb")
reader = csv.reader(in_file)
out_file = open("updatedreadall.csv", "a")
writer = csv.writer(out_file)

for row in reader:
        # assume there's one document per line, tokens separated by whitespace
    row[2]='Topic-'+row[2]
    row[3]='Topic-'+row[3]
    row[4]='Topic-'+row[4]
    writer.writerow(row)
in_file.close()
out_file.close()