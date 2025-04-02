import nltk
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from urllib.request import urlopen

# Ensure NLTK resources are downloaded
nltk.download('punkt')
nltk.download('stopwords')

# Function to read a text file (local or online)
def read_text(file_path_or_url):
    try:
        if file_path_or_url.startswith('http'):  # If source is a URL
            with urlopen(file_path_or_url) as f:
                text = f.read().decode('utf-8')
        else:  # Local file
            with open(file_path_or_url, 'r', encoding='utf-8') as f:
                text = f.read()
        return text
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

# Function to tokenize text while removing stopwords
def preprocess_text(text):
    tokens = word_tokenize(text.lower())  # Tokenize and lowercase
    stop_words = set(stopwords.words('english'))  # Use NLTK stopwords
    filtered_tokens = [word for word in tokens if word.isalnum() and word not in stop_words]
    return filtered_tokens

# Function to calculate lexical diversity
def lexical_diversity(tokens):
    return len(set(tokens)) / len(tokens) if tokens else 0

# Analyze Disney text file
def analyze_text(file):
    # Read and preprocess text
    text = read_text(file)
    if text is None:
        return

    tokens = preprocess_text(text)

    # Lexical diversity
    diversity = lexical_diversity(tokens)
    print(f"Lexical diversity: {diversity:.4f}")

    # Most common words
    freq = FreqDist(tokens)
    print("\nMost common words:")
    print(freq.most_common(10))

# Change this to your Disney text file (local path or URL)
disney_text_file = "/Users/ash/GitHub/DIGIT/DIGIT210/Python/disneySongLyrics.txt"
grimm_text_file = "/Users/ash/GitHub/DIGIT/DIGIT210/Python/grimm.txt"

print("\n--- Analyzing Disney Song Lyrics ---")
analyze_text(disney_text_file)

print("\n--- Analyzing Grimm Text ---")
analyze_text(grimm_text_file)
