# 5. Cleaning dataset of spam emails dataset
import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from bs4 import BeautifulSoup
import emoji
from spellchecker import SpellChecker

# import nltk
# nltk.download('stopwords')

# Load the text dataset
data = pd.read_csv("spam_ham_dataset.csv")
df = pd.DataFrame(data)

# Preprocessing functions
def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    
    # Remove special characters
    text = re.sub(r'[^\w\s]', '', text)
    
    # Remove HTML
    text = BeautifulSoup(text, "html.parser").get_text()
    
    # Remove emojis
    text = emoji.demojize(re.sub(r'[^\x00-\x7F]+', '', text))
    
    # Remove URLs and emails
    text = re.sub(r'http\S+|www\S+|[\w\.-]+@[\w\.-]+', '', text)
    
    # Tokenize
    tokens = text.split()
    
    # Remove stopwords
    stop_words = set(stopwords.words("english"))
    tokens = [word for word in tokens if word not in stop_words]
    
    # Stemming
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(word) for word in tokens]
    
    # Correct spelling
    spell = SpellChecker()
    tokens = [spell.correction(word) or word for word in tokens]
    
    # Join tokens back into a string
    return ' '.join(tokens)

df['text_preprocessed'] = df['text'].apply(preprocess_text)

# Save the processed DataFrame to a CSV file
df.to_csv('spam_ham_dataset_processed.csv', index=False)

# Print out some results to check
print(df[['text', 'text_preprocessed']].head())
