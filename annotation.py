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
item = dict()
for d in data:
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
            print(start,end, label)
            continue
        spans.append(span)
    print(text)
    # print(spans)
    doc.set_ents(spans)
    tokens = list()
    labels = list()
    for token in doc:
        tokens.append(token.text)
        if (token.ent_type_== "O"):
            labels.append("O")
        else:
            labels.append(token.ent_iob_+"-"+token.ent_type_)
    item["tokens"]= tokens
    item["labels"]= labels
    # print(item)
    annotation_data.append(item)

file_save = "Threat_ner_v1.json"
with codecs.open(file_save,"w", encoding="utf-8") as f:
    json.dump(annotation_data, f)

# %%
