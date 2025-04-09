import os
import nltk
from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

# Ensure necessary NLTK packages are downloaded
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('stopwords')

# Setup: get files from the 'hughes-txt' directory
cwd = os.getcwd()
text_dir = os.path.join(cwd, 'hughes-txt')
files = [file for file in os.listdir(text_dir) if file.endswith('.txt')]

# Create output folder
output_dir = os.path.join(cwd, 'output')
os.makedirs(output_dir, exist_ok=True)


# Function to extract verbs from a tokenized, POS-tagged list
def extract_verbs(tokens):
    pos_tags = pos_tag(tokens)
    verb_tags = ['VBD', 'VBN', 'VBZ', 'VB', 'VBP', 'VBG']
    return [word for word, tag in pos_tags if tag in verb_tags]


# Function to analyze word ambiguity with WordNet
def analyze_ambiguity(wordlist):
    results = []
    for word in wordlist:
        lemma = wn.morphy(word) or word
        syns = wn.synsets(lemma)
        results.append((word, lemma, len(syns)))
    return results


# Process each file
for filename in files:
    filepath = os.path.join(text_dir, filename)
    text = open(filepath, 'r', encoding='utf8').read()

    tokens = word_tokenize(text.lower())
    verbs = extract_verbs(tokens)
    unique_verbs = set(verbs)

    # Analyze with WordNet
    ambiguity_data = analyze_ambiguity(unique_verbs)

    # Save results
    output_path = os.path.join(output_dir, f"{filename}_ambiguity.txt")
    with open(output_path, 'w', encoding='utf8') as out:
        for word, lemma, syn_count in ambiguity_data:
            out.write(f"Word: {word}, Lemma: {lemma}, Synset Count: {syn_count}\n")

    print(f"Processed {filename}: {len(unique_verbs)} unique verbs analyzed.")
