import numpy
import random
import string
import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
import json
import pickle
import requests
import re
def train(inp):
    with open("intents.json") as file:
        data = json.load(file)
    try:
        with open("data.pickle", "rb") as f:
            words, labels, training, output = pickle.load(f)
    except:
        words = []
        labels = []
        docs_x = []
        docs_y = []

        for intent in data["intents"]:
            for pattern in intent["patterns"]:
                wrds = nltk.word_tokenize(pattern)
                words.extend(wrds)
                docs_x.append(wrds)
                docs_y.append(intent["tag"])

            if intent["tag"] not in labels:
                labels.append(intent["tag"])

        words = [stemmer.stem(w.lower()) for w in words if w != "?"]
        words = sorted(list(set(words)))

        labels = sorted(labels)

        training = []
        output = []

        out_empty = [0 for _ in range(len(labels))]

        for x, doc in enumerate(docs_x):
            bag = []

            wrds = [stemmer.stem(w.lower()) for w in doc]

            for w in words:
                if w in wrds:
                    bag.append(1)
                else:
                    bag.append(0)

            output_row = out_empty[:]
            output_row[labels.index(docs_y[x])] = 1

            training.append(bag)
            output.append(output_row)


        training = numpy.array(training)
        output = numpy.array(output)
        with open("data.pickle", "wb") as f:
            pickle.dump((words, labels, training, output), f)

def eventhandle(inp):
    message = inp["text"]
    with open("intents.json",'rb') as f:
        data = json.load(f)
    for items in data["intents"]:
        regex = ''
        maxi = 0
        response_item = None
        for b in items["patterns"]:
            match = get_jaccard_sim(b,message)
            print(match)
            if(match > maxi):
                maxi = match
                response_item = items
    if(response_item is None):
        print("Sorry I do not understand")
    responses = response_item['responses']
    print("That is my anser: ", random.choice(responses))

from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
def get_cosine_sim(*strs): 
    vectors = [t for t in get_vectors(*strs)]
    return cosine_similarity(vectors)
    
def get_vectors(*strs):
    text = [t for t in strs]
    print(text)
    vectorizer = CountVectorizer(text)
    print(vectorizer)
    vectorizer.fit(text)
    return vectorizer.transform(text).toarray()



import nltk.corpus
import nltk.tokenize.punkt
import string
# nltk.download('punkt') 
# nltk.download('stopwords')
# nltk.download('wordnet')
# Get default English stopwords and extend with punctuation
stopwords = nltk.corpus.stopwords.words('english')
stopwords.extend(string.punctuation)
stopwords.append('')

# Create tokenizer
tokenizer = nltk.tokenize.WordPunctTokenizer()
def get_jaccard_sim(str1, str2): 
    a = set(str1.split()) 
    b = set(str2.split())
    c = a.intersection(b)
    return float(len(c)) / (len(a) + len(b) - len(c))

def is_ci_token_stopword_match(a, b):
    """Check if a and b are matches."""
    tokens_a = [token.lower().strip(string.punctuation) for token in tokenizer.tokenize(a) \
                    if token.lower().strip(string.punctuation) not in stopwords]
    print("sentence1: ", tokens_a)
    tokens_b = [token.lower().strip(string.punctuation) for token in tokenizer.tokenize(b) \
                    if token.lower().strip(string.punctuation) not in stopwords]
    print("sentence2: ", tokens_b)
    return (tokens_a == tokens_b)

def bag_of_words(s,words):
    bag = [0 for _ in range(len(words))]
    s_words = nltk.word_tokenize(s)
    print("before: ",s_words)
    s_words1 = [stemmer.stem(word.lower()) for word in s_words if word!="?"]
    print("final: ", s_words1)

if __name__ == "__main__":
    inpt = {'token': 'nx3mp3xph3yz5ecwkskzi1ntcc', 'team_id': 'wtpx8yiowtbs5nes6adqcdco1e', 'team_domain': 'plotbotteam', 'channel_id': '85i3du788tgadqtz8mao6ctqma', 'channel_name': 'off-topic', 'timestamp': 1572374487583, 'user_id': '69i1gy344tygdychdcmppf658h', 'user_name': 'akankshanb', 'post_id': 'f38grtj7ut8fuqoaw4w6stexdw', 'text': '@plotbot I need to retrieve my plots from this to that', 'trigger_word': 'plot', 'file_ids': ''}
    eventhandle(inpt)


