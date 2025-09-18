# # --- Imports ---
# import string
# import pandas as pd
# from sklearn.metrics import accuracy_score
# from collections import Counter
# from nltk.tokenize import sent_tokenize, word_tokenize
# from nltk.corpus import stopwords
# from nltk.sentiment.vader import SentimentIntensityAnalyzer
# import matplotlib.pyplot as plt
# import nltk



# # --- Step 1: Preprocess Text (read.txt) ---
# text = open(r"C:\Users\drunk\OneDrive\Desktop\projects python\emotion.txt",'r', encoding='utf-8').read()
# lower_case = text.lower()
# cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

# # Tokenize into words (for emotion extraction)
# tokenized_words = word_tokenize(cleaned_text, "english")
# final_words = [word for word in tokenized_words if word not in stopwords.words('english')]

# # --- Step 2: Emotion Extraction (emotion.txt) ---
# emotion_list = []
# with open(r"C:\Users\drunk\OneDrive\Desktop\projects python\emotion.txt", 'r', encoding='utf-8') as file:
#     for line in file:
#         clear_line = line.replace('\n', '').replace(",", '').replace("'", '').strip()
#         if ':' in clear_line:
#             word, emotion = clear_line.split(':')
#             if word in final_words:
#                 emotion_list.append(emotion)

# w = Counter(emotion_list)

# # Plot emotions
# fig, ax1 = plt.subplots()
# ax1.bar(w.keys(), w.values())
# fig.autofmt_xdate()
# plt.savefig('graph.png')
# plt.show()

# # --- Step 3: Sentiment Analysis Function ---
# sia = SentimentIntensityAnalyzer()

# def sentiment_analyse(sentiment_text):
#     score = sia.polarity_scores(sentiment_text)
#     neg, pos = score['neg'], score['pos']
#     if neg > pos:
#         return "negative"
#     elif pos > neg:
#         return "positive"
#     else:
#         return "neutral"

# # --- Step 4: Build Dataset from Sentences ---
# sentences = sent_tokenize(text)

# # Example: Assign true labels manually (just for demo!)
# # You can refine these based on your actual data
# true_labels = [
#     "positive",  # "i was very happy to be in this concert..."
#     "negative",  # "i got very sad when..."
#     "positive",  # "i feel happy and shy..."
#     "neutral"    # part of Steve Jobs speech, more neutral
# ]

# # Build DataFrame
# data = pd.DataFrame({
#     "text": sentences[:len(true_labels)],  # take only same number as labels
#     "label": true_labels
# })

# # Apply sentiment model
# data['predicted'] = data['text'].apply(sentiment_analyse)

# # --- Step 5: Accuracy Calculation ---
# accuracy = accuracy_score(data['label'], data['predicted'])
# print("\nPredictions with True Labels:\n", data[['text','label','predicted']])
# print("\nAccuracy:", accuracy)


#  cleaning text 
import string
import pandas as pd 
from sklearn.metrics import accuracy_score
from collections import Counter
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as pyt
text=open(r"C:\Users\drunk\OneDrive\Desktop\projects python\read.txt",encoding='utf-8').read()
lower_case=text.lower()
cleaned_text=lower_case.translate(str.maketrans('','',string.punctuation))


tokenized_words=word_tokenize(cleaned_text,"english")


final_words=[]
for word in  tokenized_words:
    if word not in stopwords.words('english'):
        final_words.append(word)


emotion_list=[]
with open(r"C:\Users\drunk\OneDrive\Desktop\projects python\emotion.txt",'r')as file:
    for line in file:
        clear_line=line.replace('\n','').replace(",",'').replace("'",'').strip()
        word,emotion=clear_line.split(':')
        if word in final_words:
            emotion_list.append(emotion)

w=Counter(emotion_list)




def sentiment_analyse(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    neg = score['neg']
    pos = score['pos']
    if neg > pos:
        return "negative"
    elif pos > neg:
        return "positive"
    else:
        return "neutral"


 #Step 4: Build Dataset from Sentences

sentences = sent_tokenize(text)  

# You can refine these based on your actual data
true_labels = [
    "positive",  # "i was very happy to be in this concert..."
    "negative",  # "i got very sad when..."
    "positive",  # "i feel happy and shy..."
    "neutral"    # part of Steve Jobs speech, more neutral
]

# Build DataFrame
data = pd.DataFrame({
    "text": sentences[:len(true_labels)],  # take only same number as labels
    "label": true_labels
})


data['predicted'] = data['text'].apply(sentiment_analyse)

# Debug before filtering
print("\nBefore filtering:")
print("True labels:", data["label"].tolist())
print("Predicted labels:", data["predicted"].tolist())

# Keep only valid labels
valid_labels = {"positive", "negative", "neutral"}
data = data[data["label"].isin(valid_labels) & data["predicted"].isin(valid_labels)]

if data.empty:
    print("\nNo valid rows left after filtering! Check labels again.")
else:
    accuracy = accuracy_score(data['label'], data['predicted'])
    print("\nPredictions with True Labels:\n", data[['text','label','predicted']])
    print("\nAccuracy:", accuracy)
