#%%
from mitreattack.stix20 import MitreAttackData
import spacy
import re
import codecs
nlp = spacy.load("en_core_web_sm")
import os
file_path = r"G:\Other computers\My Laptop\Doctoral program\Lab\MITRE ATTACK\enterprise-attack.json"
#read mittre_attack corpus
#input file, output list of  description [{id: threadID, description: description}]
def read_corpus(file_path):
    return


# annotate description for each threat
def threat_annotation():
    return

mitre_attack_data = MitreAttackData(file_path)
# technique = mitre_attack_data.get_object_by_attack_id('T1040', 'attack-pattern')
# print(technique["description"])

def annotation_text(text):
    sent = list()
    
    text = re.sub(r'\([^)]*\)', '', text)
    text = text.replace('[','').replace(']','')  
    doc = nlp(text)
    sents = [s for s in doc.sents]
    for s in sents:
        sent.append(s.text.strip() + "\n")
    return sent

# annotation_text(technique["description"])
# technique = mitre_attack_data.get_techniques(include_subtechniques=True)
technique = mitre_attack_data.get_techniques_by_platform("Network")
# print(technique[0])
description = list()
for t in technique:
    for m in  t["external_references"]:
        if m["source_name"]== "mitre-attack":
            id = m["external_id"]
            description.extend(annotation_text(t["description"]))
path = os.path.join(r"C:\Users\Oblivion\Working Space\miscellaneous\causal_effect_annotations\output", "final.txt")
with codecs.open(path,"w",encoding="utf-8") as f:
            f.writelines(description)

#%%
import json
import codecs

dir_path = r"C:\Users\Oblivion\Working Space\temp"
files = os.listdir(dir_path)
annotations = list()
for f in files:
    path = os.path.join(dir_path, f)
    with codecs.open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
        annotations.extend(data["annotations"])
print(annotations)

# %%
print(len(annotations))
# %%
data = dict()
data["classes"]= ["ACTOR","ACTION","EFFECT"]
data["annotations"] = annotations
save_path = os.path.join(dir_path, "out.json")
with codecs.open(save_path,"w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False)
# %%
