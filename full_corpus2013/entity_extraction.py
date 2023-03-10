import json
import os
import pickle
dir = r""
file_path = r"G:\Other computers\My Laptop\Doctoral program\Lab\NER dataset\full_corpus.json"
save_path = os.path.join(r"C:\Users\Oblivion\Working Space\miscellaneous\full_corpus2013\output",r"2013.pickle")
def read_list(mylist):
    collection = list()
    prev = "O"
    word = ""
    label = "O"
    for l in mylist:
        if len(l)<2:
            continue
        if l[1].startswith("B-"):
            if label!="O":
                collection.append((word,label))
            word= l[0]
            prev= l[1]
            label = l[1][2:]
        if l[1].startswith("I-") and l[1][2:]== label:
            word +=" " + l[0]
            prev= l[1]
        if l[1].startswith("O"):
            if prev.startswith("B-") or prev.startswith("I-"):
                if label!="O":
                    collection.append((word,label))
            word= ""
            prev= "O"
            label= "O"
    return collection

# with open(file_path,"r", encoding="utf-8") as f:
#      data = json.load(f)
#      mylist= data["NVD"]["CVE-2010-0001"]
#      collection = read_list(mylist)
#      print(collection) 

def read_file(file_path):
    collections = list()
    with open(file_path,"r", encoding="utf-8") as f:
        data = json.load(f)
    for k,v in data.items():
        print(k)
        for m,n in v.items():
            collection = read_list(n)
            collections.extend(collection)
    return collections

def cleaning(mycollection):
    temp = list()
    for c in mycollection:
        if c not in temp:
            temp.append(c)
    return temp

data = read_file(file_path=file_path)
print(len(data))
data=cleaning(data)
print(len(data))
print(data)
with open(save_path, "wb") as f:
      pickle.dump(data,f, protocol= pickle.HIGHEST_PROTOCOL)