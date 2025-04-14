import spacy

# Load spaCy's English language model
nlp = spacy.load("en_core_web_sm")

# Open your text file
with open("song-3.xml", "r", encoding="utf-8") as file:
    text = file.read()

# Process the text with spaCy
doc = nlp(text)

# Extract verbs and count them
verb_freq = {}
for token in doc:
    if token.pos_ == "VERB":
        verb = token.lemma_.lower()
        verb_freq[verb] = verb_freq.get(verb, 0) + 1

# Write output to a file
with open("verbFreq.txt", "w", encoding="utf-8") as o:
    for verb, freq in sorted(verb_freq.items(), key=lambda x: -x[1]):
        o.write(f"{verb}: {freq}\n")
