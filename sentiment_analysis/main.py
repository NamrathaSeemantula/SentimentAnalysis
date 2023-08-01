import string
from collections import Counter

from nltk.tokenize import word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords

import matplotlib.pyplot as plt

text=open('sample.txt', encoding='utf-8').read()
lower_case=text.lower()
cleaned_text=lower_case.translate(str.maketrans('','',string.punctuation))

tokenized_words=word_tokenize(cleaned_text,"english")
print("Tokenized Words:", tokenized_words)

final_words=[]
for word in tokenized_words:
    if word not in stopwords.words('english'):
        final_words.append(word)
print("Final Words:",final_words)

emotion_list=[]
with open('emotion_lexicon.txt', 'r') as file:
    for line in file:
        clear_line=line.replace('\n','').replace(",",'').replace("'",'').strip()
        word,emotion=clear_line.split(':')


        if word in final_words:
            emotion_list.append(emotion)
print("Emotion list:",emotion_list)

w=Counter(emotion_list)
print(w)

def sentiment_analysis(sentiment_text):
    score=SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    neg=score['neg']
    pos=score['pos']
    if neg>pos:
        print("Negative sentiment")
    elif pos>neg:
        print("Positive sentiment")
    else:
        print("Neutral value")

sentiment_analysis(cleaned_text)
fig,ax1=plt.subplots()
ax1.bar(w.keys(),w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()
