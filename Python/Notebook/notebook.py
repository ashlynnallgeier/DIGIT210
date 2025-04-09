import nltk
import matplotlib.pyplot as plt
import tkinter as tk
from nltk import FreqDist
from nltk.tokenize import word_tokenize

# Download necessary resources (only once)
nltk.download('punkt')

# Load your own Disney text file
with open("grimm.txt", "r", encoding="utf-8") as file:
    grimm_raw = file.read()

# Tokenize the text
grimm_tokens = word_tokenize(grimm_raw.lower())

# Filter out punctuation
words = [word for word in grimm_tokens if word.isalpha()]

# Show lexical diversity
lexical_diversity = len(set(words)) / len(words)
print(f"Lexical diversity of grimm.txt: {lexical_diversity:.3f}")

# Frequency distribution
fdist = FreqDist(words)

# Show the 20 most common words
print("Most common words:", fdist.most_common(20))

# Plot frequency distribution
fdist.plot(20, title="Top 20 Word Frequencies in Grimm")

# Try dispersion-like effect (only works if you convert to Text class)
grimm_text = nltk.Text(words)
grimm_text.dispersion_plot(["princess", "magic", "castle", "witch"])
