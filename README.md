# Sentiment Analysis with NLTK & VADER

This project analyzes text sentiment (Positive, Negative, Neutral) and emotions using **NLTK** and **VADER** sentiment analysis tools.  
It also visualizes emotions in a bar chart and calculates prediction **accuracy** for evaluation.

--------

## 📂 Project Files

sentiment_analysis-with-NLTK/
│
├── Sentiment_analysis.py # Main script for sentiment & emotion analysis
├── read.txt # Sample input text file
├── emotion.txt # Emotion keywords (word:emotion format)
├── graph.png # Bar chart output after analysis
├── requirements.txt # Dependencies list
└── README.md # Project documentation

---------

## ⚡ Features

- **Text Cleaning:** Removes punctuation, converts text to lowercase  
- **Tokenization:** Splits text into individual words  
- **Stopwords Removal:** Filters out common words like "the", "and", etc.  
- **Emotion Detection:** Matches words with emotions in `emotion.txt`  
- **Sentiment Analysis:** Uses **VADER** to classify text as Positive, Negative, or Neutral  
- **Visualization:** Generates bar chart (`graph.png`) for detected emotions  
- **Accuracy Evaluation:** Compares true labels with predicted labels using `accuracy_score`  

---

## 🛠 Requirements

Install dependencies with:

pip install -r requirements.txt

Download NLTK resources
(already included in requirements.txt):

import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')

📖 Usage
Prepare input files

read.txt: Text to analyze

emotion.txt: Words with emotion tags in word:emotion format

python Sentiment_analysis.py
Outputs

* Prints sentiment scores and overall sentiment label

* Generates graph.png with emotion counts

* Prints accuracy score for model evaluation

📊 Example Output
Terminal Output:

{'neg': 0.087, 'neu': 0.751, 'pos': 0.162, 'compound': 0.9996}
Positive text


Graph:

X-axis: Emotion labels (Joy, Sadness, Anger, etc.)

Y-axis: Count of words detected for each emotion

🚀 Future Improvements
* Integrate larger datasets for training & testing

* Add precision, recall, F1-score for detailed evaluation

* Build a web interface for real-time sentiment analysis
