#%%
import spacy
from spacy import displacy
nlp = spacy.load("en_core_web_sm")
#%%
sent = "NBF (known as Network-based firewalls) are positioned between two or more networks, typically between the local area network (LAN) and wide area network (WAN)."
doc = nlp(sent)
displacy.render(doc, style="dep")
# %%
for sent in doc.sents:
    for t in sent:
        if t.text=="NBF":
            for k in t.subtree:
                if k.text!= t.text:
                    print (k.text)
# %%
