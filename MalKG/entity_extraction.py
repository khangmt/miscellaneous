import os
import pickle
dir = r"G:\Other computers\My Laptop\Doctoral program\Lab\NER dataset\MalKG-1-main\Entity2id"
file_path = r"G:\Other computers\My Laptop\Doctoral program\Lab\NER dataset\MalKG-1-main\Entity2id\entity2id_40k.txt"
save_path = os.path.join(r"C:\Users\Oblivion\Working Space\miscellaneous\MalKG\output",r"malKG2.pickle")
def read_file(file_path):
    collection = list()
    with open(file_path,"r", encoding = "utf-8") as f:
        lines = f.readlines()
    for l in lines:
        split = l.split()
        if len(split)<2:
            continue
        s = split[0]
        split = s.split("_")
        label = split[0]
        word = " ".join(split[1:])
        if (word,label) not in collection:
            collection.append((word, label))
    return collection
def read_file2(file_path):
    collection = list()
    label = "Misc"
    with open(file_path,"r", encoding = "utf-8") as f:
        lines = f.readlines()
    for l in lines:
        split = l.split()
        if len(split)<2:
            continue
        s = split[0]
        split = s.split("_")
        
        word = " ".join(split[1:])
        if (word,label) not in collection:
            collection.append((word, label))
    return collection
data = read_file2(file_path)
print(len(data))
print(data)
with open(save_path, "wb") as f:
      pickle.dump(data,f, protocol= pickle.HIGHEST_PROTOCOL)