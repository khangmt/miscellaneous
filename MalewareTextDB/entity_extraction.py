import os
import pickle
dir_path = r"G:\Other computers\My Laptop\Doctoral program\Lab\NER dataset\MalewareTextDB\dataset\tokenized"
file_path = r"G:\Other computers\My Laptop\Doctoral program\Lab\NER dataset\MalewareTextDB\dataset\tokenized\Aided_Frame_Aided_Direction.tokens"
save_file = os.path.join(r"C:\Users\Oblivion\Working Space\miscellaneous\MalewareTextDB\output", r"MalewareTextDB.pickle")

def read_file(file_name):
    collection = list()
    with open(file_name, "r", encoding="utf-8") as f:
        lines = f.readlines()
    prev = "O"
    word = ""
    label = "O"
    for l in lines:
        split = l.split()
        if len(split)<3:
            if len(split) == 2:
                print (l)
                print(file_name)
            continue
        if split[2].startswith("B-"): # B is always start of new word, save the old word
                if label!="O":
                    collection.append((word,label))
                word= split[0]
                prev= split[2]
                label = split[2][2:]
                          
        if split[2].startswith("I-") and split[2][2:]== label:
                    word +=" " + split[0]
                    prev= split[2]
        if split[2].startswith("O"):
            if prev.startswith("B-") or prev.startswith("I-"):
                if label!="O":
                    collection.append((word,label))
            word= ""
            prev= "O"
            label= "O"
    return collection 



def reaf_dir(dir_path):
    collections = list()
    files = os.listdir(dir_path)
    for f in files:
        collection = read_file(os.path.join(dir_path,f))
        collections.extend(collection)
    return collections

data = reaf_dir(dir_path)
with open(save_file, "wb") as f:
     pickle.dump(data,f, protocol= pickle.HIGHEST_PROTOCOL)