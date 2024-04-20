import nltk
from nltk.corpus import stopwords
from collections import Counter

# Download NLTK stopwords if you haven't already
nltk.download('stopwords')

# Read the file
file_path = "random_paragraphs.txt"
with open(file_path, 'r') as file:
    text = file.read()

# Tokenize the text into words
words = nltk.word_tokenize(text)

# Remove stopwords
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word.lower() not in stop_words]

# Count word frequencies
word_freq = Counter(filtered_words)

# Print the most common words and their frequencies
print("Most common words and their frequencies:")
for word, freq in word_freq.most_common():
    print(f"{word}: {freq}")
