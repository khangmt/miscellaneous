import json
from spacy.lang.en import English
import spacy

nlp = English()
input_file = r"raw.txt"
output_file = r"data.json"

with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

final_data = list()
for l in lines:
    data = dict()
    data["sent"] = l
    doc = nlp(l)
    tokens = list()
    annotation = list()
    data["type"]= 1
    for token in doc:
        if token.text == "\n": continue
        tokens.append(token.text)
        annotation.append("O")
    data["token"]= tokens
    data["annotation"] = annotation
    final_data.append(data)
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(final_data,f,ensure_ascii=False,indent=2)