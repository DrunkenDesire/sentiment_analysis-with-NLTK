#  cleaning text 
import string
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as pyt
text=open('read.txt',encoding='utf-8').read()
lower_case=text.lower()
cleaned_text=lower_case.translate(str.maketrans('','',string.punctuation))


tokenized_words=word_tokenize(cleaned_text,"english")


final_words=[]
for word in  tokenized_words:
    if word not in stopwords.words('english'):
        final_words.append(word)


emotion_list=[]
with open('emotion.txt','r')as file:
    for line in file:
        clear_line=line.replace('\n','').replace(",",'').replace("'",'').strip()
        word,emotion=clear_line.split(':')
        if word in final_words:
            emotion_list.append(emotion)

w=Counter(emotion_list)

fig,ax1=pyt.subplots()
ax1.bar(w.keys(),w.values())
fig.autofmt_xdate()
pyt.savefig('graph.png')
pyt.show()


def sentiment_analyse(sentiment_text):
  score=SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
  print(score)
  neg=score['neg']
  pos=score['pos']
  if neg>pos:
      print("Negative text")
  elif pos>neg:
      print("Positive text")
  else:
      print("Neutral text ")
  
sentiment_analyse(cleaned_text)
