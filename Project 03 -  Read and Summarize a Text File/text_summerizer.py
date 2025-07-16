
# ✅ 3. Read and Summarize a Text File
''' 🧠 Objective: Read a .txt file, summarize the content by showing:

Total lines, words, and characters

Top 5 most frequent words

🔧 Features:
Input: File name

Output: Stats + basic word frequency analysis

💡 Concepts Used:
open() in 'r' mode

String methods: .split(), .lower(), .count()

collections.Counter
'''

import re
from collections import Counter
import heapq

def read_text_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None
    
def preprocess_text(text):
    # Convert to lowercase and split into sentences
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    # Clean text: remove non-alphabetic characters and extra spaces
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text.lower())
    words = cleaned_text.split()
    return sentences, words

def generate_summary(text, num_sentences=3):
    if not text:
        return "No summary generated due to invalid input."
    sentences, words = preprocess_text(text)
    if not sentences or not words:
        return "Text is too short to summarize."
    
    # Calculate word frequencies
    word_freq = Counter(words)
    # Remove common stop words (simplified list for brevity)
    stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by'}
    word_freq = {word: freq for word, freq in word_freq.items() if word not in stop_words}

    # Score sentences based on word frequencies
    sentence_scores = {}
    for sentence in sentences:
       for word, freq in word_freq.items():
           if word in sentence.lower():
              sentence_scores[sentence] = sentence_scores.get(sentence, 0) + freq

    # Select top N sentences
    summary_sentences = heapq.nlargest(num_sentences, sentence_scores, key = sentence_scores.get)
    # Preserve original order of sentences
    summay = [s for s in sentences if s in summary_sentences]
    return " ".join(summay) if summay else "No summary generated."

def main():
    file_path = input("Enter the path to the text file: ")
    text = read_text_file(file_path)
    if text:
        summary = generate_summary(text)
        print("\nSummary: ")
        print(summary)

if __name__ == "__main__":
    main()


    
