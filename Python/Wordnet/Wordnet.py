import nltk
from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from bs4 import BeautifulSoup

# Download NLTK resources if needed
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

# === Step 1: Read the XML file and pull out lyrics ===
with open("song-3.xml", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "xml")

# Grab all the text inside <mdiv> tags (where the lyrics are)
lyrics = ""
for mdiv in soup.find_all("mdiv"):
    lyrics += mdiv.get_text() + " "

# === Step 2: Tokenize and POS tag the words ===
tokens = word_tokenize(lyrics.lower())  # Make everything lowercase and split into words
tagged_words = pos_tag(tokens)  # Tag each word with its part of speech (noun, verb, etc.)

# === Step 3: Pick some words to explore with WordNet ===
target_words = ['light', 'run', 'fair', 'storm', 'night']

# === Step 4: Check how many meanings (synsets) each word has ===
print("WordNet Synset Counts:\n")
for word in target_words:
    synsets = wn.synsets(word)  # Get all WordNet meanings for this word
    print(f"{word} - Synset count: {len(synsets)}")

    # Optional: Print first few definitions
    for i, syn in enumerate(synsets[:3]):  # Only show up to 3 definitions to keep it short
        print(f"  Definition {i + 1}: {syn.definition()}")
    print()
