# Task 1- combination
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Load your CSV file
data = pd.read_csv("spam_ham_dataset_processed.csv")

# Use the 'text' column from the dataset
text_data = data['text'].astype(str)

# Initialize an empty DataFrame to store all features
all_features = pd.DataFrame()

def bag_of_words():
    vectorizer = CountVectorizer()
    matrix = vectorizer.fit_transform(text_data)
    # Convert to DataFrame for better structure
    df_bow = pd.DataFrame(matrix.toarray(), columns=[f"bow_{word}" for word in vectorizer.get_feature_names_out()])
    return df_bow

def tfidf():
    vectorizer = TfidfVectorizer()
    matrix = vectorizer.fit_transform(text_data)
    # Convert to DataFrame for better structure
    df_tfidf = pd.DataFrame(matrix.toarray(), columns=[f"tfidf_{word}" for word in vectorizer.get_feature_names_out()])
    return df_tfidf

def char_level_features():
    vectorizer = CountVectorizer(analyzer='char')
    matrix = vectorizer.fit_transform(text_data)
    # Convert to DataFrame for better structure
    df_char = pd.DataFrame(matrix.toarray(), columns=[f"char_{char}" for char in vectorizer.get_feature_names_out()])
    return df_char

def pos_tagging():
    def extract_pos_features(text):
        tokens = word_tokenize(text)
        pos_tags = pos_tag(tokens)
        return ' '.join([tag for word, tag in pos_tags])
    
    pos_features = [extract_pos_features(text) for text in text_data]
    vectorizer = CountVectorizer()
    matrix = vectorizer.fit_transform(pos_features)
    # Convert to DataFrame for better structure
    df_pos = pd.DataFrame(matrix.toarray(), columns=[f"pos_{tag}" for tag in vectorizer.get_feature_names_out()])
    return df_pos

def lexical_features():
    def extract_lexical_features(text):
        words = word_tokenize(text)
        common_words = ["free", "buy", "click", "now"]
        return ' '.join([word for word in words if word in common_words])
    
    lexical_features = [extract_lexical_features(text) for text in text_data]
    vectorizer = CountVectorizer()
    matrix = vectorizer.fit_transform(lexical_features)
    # Convert to DataFrame for better structure
    df_lexical = pd.DataFrame(matrix.toarray(), columns=[f"lex_{word}" for word in vectorizer.get_feature_names_out()])
    return df_lexical

def sentiment_analysis():
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = [sia.polarity_scores(text) for text in text_data]
    sentiment_features = pd.DataFrame(sentiment_scores)
    # Add prefixes for sentiment features
    sentiment_features.columns = [f"sent_{col}" for col in sentiment_features.columns]
    return sentiment_features

# Run all feature extraction functions and concatenate them into one DataFrame
all_features = pd.concat([bag_of_words(), tfidf(), char_level_features(), pos_tagging(), lexical_features(), sentiment_analysis()], axis=1)

# Save only the first 50 rows of the DataFrame to a CSV file
all_features.head(50).to_csv('all_features.csv', index=False)
