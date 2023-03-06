
example = {'id': '0',
 'ner_tags': [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 8, 8, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0],
 'tokens': ['admin@33', 'It', "'s", 'the', 'view', 'from', 'where', 'I', "'m", 'living', 'for', 'two', 'weeks', '.', 'Empire', 'State', 'Building', '=', 'ESB', '.', 'Pretty', 'bad', 'storm', 'here', 'last', 'evening', '.']
}
from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")

def tokenize_and_align_labels(examples):
    tokenized_inputs = tokenizer(examples["tokens"], truncation=True, padding=True, max_length= 512, is_split_into_words=True)

    labels = examples[f"ner_tags"]
    word_ids = tokenized_inputs.word_ids()  # Map tokens to their respective word.
    print(word_ids)
    previous_word_idx = None
    label_ids = []
    for word_idx in word_ids:  # Set the special tokens to -100.
            if word_idx is None:
                label_ids.append(-100)
            elif word_idx != previous_word_idx:  # Only label the first token of a given word.
                label_ids.append(labels[word_idx])
            else:
                label_ids.append(-100)
            previous_word_idx = word_idx

    tokenized_inputs["labels"] = label_ids
    return tokenized_inputs

features = tokenize_and_align_labels(examples= example)
tokens = tokenizer.convert_ids_to_tokens(features["input_ids"])
print(tokens)
print(features["labels"])
k = [0  if l == -100 else 1 for l in features["labels"]]
print(k)


