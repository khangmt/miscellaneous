# import json
# from spacy.lang.en import English
# import spacy

# nlp = English()
# input_file = r"raw.txt"
# output_file = r"data.json"

# with open(input_file, "r", encoding="utf-8") as f:
#     lines = f.readlines()

# final_data = list()
# for l in lines:
#     data = dict()
#     data["sent"] = l
#     doc = nlp(l)
#     tokens = list()
#     annotation = list()
#     data["type"]= 1
#     for token in doc:
#         if token.text == "\n": continue
#         tokens.append(token.text)
#         annotation.append("O")
#     data["token"]= tokens
#     data["annotation"] = annotation
#     final_data.append(data)
# with open(output_file, "w", encoding="utf-8") as f:
#     json.dump(final_data,f,ensure_ascii=False,indent=2)

#%%
import json
from spacy.tokens import Span
import random
import spacy
import codecs
nlp = spacy.load("en_core_web_sm")
text = ""
file_path = r"G:\Other computers\My Laptop\Doctoral program\Lab\NER dataset\myannotations.json"
with codecs.open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)
data = data["annotations"]
annotation_data = list()

for d in data:
    item = dict()
    if d is None:
        continue
    text, annot = d
    item["sentence"]=text
    doc = nlp(text)
    if doc is None:
        continue
    spans = list()
    for start, end, label in annot["entities"]:
        span = doc.char_span(start, end, label=label)
        if span is None:
            # print(start,end, label)
            continue
        spans.append(span)
        # if label == "USER":
        #     print(spans)
    # print(spans)
    doc.set_ents(spans)
    tokens = list()
    labels = list()
    for token in doc:
        tokens.append(token.text)
        if (token.ent_iob_== "O"):
            labels.append("O")
        else:
            new_label = token.ent_iob_+"-"+token.ent_type_
            #     print(token.text, token.ent_iob_, token.ent_type_)
            labels.append(new_label)
        # print(token.text, token.ent_iob_, token.ent_type_)
    item["tokens"]= tokens
    item["labels"]= labels
    # if "users" in item["sentence"]:
    #     print(item["labels"])
    #     print(item["sentence"])
    annotation_data.append(item)

file_save = "Threat_ner_v1.json"
with codecs.open(file_save,"w", encoding="utf-8") as f:
    json.dump(annotation_data, f,indent=4)

#%%
import json
import codecs
import random
import math
file_path = "Threat_ner_v1.json"
with codecs.open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)
random.shuffle(data)
offset1 = math.floor(0.8 * len(data))
offset2 = math.floor(0.9* len(data))
dataset = dict()
dataset["train_data"]= data[0:offset1]
dataset["dev_data"] = data[offset1:offset2]
dataset["test_data"] = data[offset2: len(data)]
save_names = ["train.json", "dev.json", "test.json"]
with codecs.open(save_names[0], "w", encoding= "utf-8") as f:
    json.dump(dataset["train_data"],f, ensure_ascii=False)
with codecs.open(save_names[1], "w", encoding= "utf-8") as f:
    json.dump(dataset["dev_data"],f, ensure_ascii=False)
with codecs.open(save_names[2], "w", encoding= "utf-8") as f:
    json.dump(dataset["test_data"],f, ensure_ascii=False)
# %%
import json
import codecs
import random
import math
import pickle
file_path = "Threat_ner_v1.json"
with codecs.open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)
uniques = list()
for d in data:
    for label in d["labels"]:
        if label not in uniques:
            uniques.append(label)
if "I-ACTOR" not in uniques:
    uniques.append("I-ACTOR")
if "I-USER" not in uniques:
    uniques.append("I-USER")
data_dict = dict()
tag2id = {v:k for k,v in enumerate(uniques)}
id2tag = {k:v for k,v in enumerate(uniques)}
num_tags = len(uniques)
data_dict["tag2id"] = tag2id
data_dict["id2tag"] = id2tag
data_dict["num_tags"] = num_tags
print(data_dict)
# with open("mapper.pickle", "wb") as f:
#     pickle.dump(data_dict,f,protocol= pickle.HIGHEST_PROTOCOL)

# # %%
