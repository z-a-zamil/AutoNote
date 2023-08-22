import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

text = """ext is a form of communication that involves using written or printed symbols to convey information, ideas, or thoughts. It's a fundamental means of sharing knowledge, expressing emotions, and communicating messages between individuals or groups. Text can take various forms, such as books, articles, emails, messages, and more. With the advent of digital technology, text has become a crucial part of online communication, social media, websites, and digital documents. It plays a significant role in human culture, education, and information dissemination."""


# def summarizer(rawdocs):
stopwords = list(STOP_WORDS)
# print(stopwords)
nlp = spacy.load('en_core_web_sm')
doc = nlp(text)
# print(doc)
tokens = [token.text for token in doc]
# print(tokens)
word_freq = {}
for word in doc:
    if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
        if word.text not in word_freq.keys():
            word_freq[word.text] = 1
        else:
            word_freq[word.text] +=1
    # print(word_freq)        

max_freq = max(word_freq.values())
# print(max_freq)   

for word in word_freq.keys():
    word_freq[word] = word_freq[word]/max_freq
# print(word_freq)    

sent_tokens = [sent for sent in doc.sents]
# print(sent_tokens)

sent_scores = {}
for sent in sent_tokens:
    for word in sent:
        if word.text in word_freq.keys():
            if sent not in sent_scores.keys():
                sent_scores[sent]= word_freq[word.text]
            else:
                sent_scores[sent] += word_freq[word.text]  
# print(sent_scores)                   

select_len = int(len(sent_tokens) * 0.3)
# print(select_len)
summary = nlargest(select_len, sent_scores, key = sent_scores.get)
# print(summary)
final_summary = [word.text for word in summary]
summary = ' '.join(final_summary)
print(text)
print(summary)
print("length of original text ",len(text.split(' ')))
print("length of summary text ",len(summary.split(' ')))
