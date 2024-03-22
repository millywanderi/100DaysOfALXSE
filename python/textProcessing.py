#!/usr/bin/python3
"""
Module that performs text preprocessing using NLTK
for tokenization and removal of stopwords 
"""

import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer


def preprocess_text(text):
    """Tokenization"""
    tokens = word_tokenize(text.lower()) # Converting the text to lowercase
    # Remove stopwards
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token not in stop_words]
    # Stemming
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(token) for token in filtered_tokens]
    # Return processed text as a single string
    preprocessed_text = ' '.join(stemmed_tokens)
    return preprocessed_text

# Usage
text = "NLP is a subfield of linguistics, computer science."
preprocessed_text = preprocess_text(text)
print("Original text:")
print(text)
print("\nPreprocesses text:")
print(preprocessed_text)
