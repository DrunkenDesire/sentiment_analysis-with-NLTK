# cleaning text 
import string
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import matplotlib.pyplot as pyt
text=open('read.txt',encoding='utf-8').read()
lower_case=text.lower()
cleaned_txt=lower_case.translate(str.maketrans('','',string.punctuation))


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
