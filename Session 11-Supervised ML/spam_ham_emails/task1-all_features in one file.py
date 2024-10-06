# Task 1-seperate
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Load your CSV file
data = pd.read_csv("spam_ham_dataset_processed.csv")

# Use the 'text' column from the dataset
text_data = data['text'].astype(str)

def bag_of_words():
    vectorizer = CountVectorizer()
    matrix = vectorizer.fit_transform(text_data)
    
    df_bow = pd.DataFrame(matrix.toarray(), columns=[f"bow_{word}" for word in vectorizer.get_feature_names_out()])
    df_bow.head(50).to_csv('bag_of_words_features.csv', index=False)
# bag_of_words()

def tfidf():
    vectorizer = TfidfVectorizer()
    matrix = vectorizer.fit_transform(text_data)

    df_tfidf = pd.DataFrame(matrix.toarray(), columns=[f"tfidf_{word}" for word in vectorizer.get_feature_names_out()])
    df_tfidf.head(50).to_csv('tfidf_features.csv', index=False)
# tfidf()

def char_level_features():
    vectorizer = CountVectorizer(analyzer='char')
    matrix = vectorizer.fit_transform(text_data)

    df_char = pd.DataFrame(matrix.toarray(), columns=[f"char_{char}" for char in vectorizer.get_feature_names_out()])
    df_char.head(50).to_csv('char_level_features.csv', index=False)
# char_level_features()

def pos_tagging():
    def extract_pos_features(text):
        tokens = word_tokenize(text)
        pos_tags = pos_tag(tokens)
        return ' '.join([tag for word, tag in pos_tags])
    
    pos_features = [extract_pos_features(text) for text in text_data]
    vectorizer = CountVectorizer()
    matrix = vectorizer.fit_transform(pos_features)

    df_pos = pd.DataFrame(matrix.toarray(), columns=[f"pos_{tag}" for tag in vectorizer.get_feature_names_out()])
    df_pos.head(50).to_csv('pos_tagging_features.csv', index=False)
# pos_tagging()

def lexical_features():
    def extract_lexical_features(text):
        words = word_tokenize(text)
        common_words = ["free", "buy", "click", "now"]
        return ' '.join([word for word in words if word in common_words])
    
    lexical_features = [extract_lexical_features(text) for text in text_data]
    vectorizer = CountVectorizer()
    matrix = vectorizer.fit_transform(lexical_features)

    df_lexical = pd.DataFrame(matrix.toarray(), columns=[f"lex_{word}" for word in vectorizer.get_feature_names_out()])
    df_lexical.head(50).to_csv('lexical_features.csv', index=False)
# lexical_features()

def sentiment_analysis():
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = [sia.polarity_scores(text) for text in text_data]
    sentiment_features = pd.DataFrame(sentiment_scores)

    sentiment_features.head(50).to_csv('sentiment_analysis_features.csv', index=False)
# sentiment_analysis()

# Uncomment any of the functions below to save their results to CSV
bag_of_words()
tfidf()
char_level_features()
pos_tagging()
lexical_features()
sentiment_analysis()
