import os
from pprint import pprint

dir = "data/"
files = []
files2 = os.listdir(dir)
for file in files2:
    file = dir+file
    files.append(file)

counts = []
for file in files:
    with open(file, encoding='utf-8') as f:
        file = file.split("/")[1]
        data = f.readlines()
        ff = []
        for item in data:
            item = item.strip().strip("\n")
            ff.append(item)
        count = len(ff)
    counts.append({'count':len(ff), 'file':file, 'lines':ff})
data_files = sorted(counts, key=lambda x:x['count'])

finish_file_name = 'finish.txt'

with open(finish_file_name, 'w') as f:
    for data in data_files:
        f.write(data['file']+'\n')
        f.write(str(data['count'])+'\n')
        lines = data['lines']
        for line in lines:
            f.write(line+'\n')