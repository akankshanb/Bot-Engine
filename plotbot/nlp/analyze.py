import numpy
import random
import string
import nltk
import nltk.corpus
import nltk.tokenize.punkt
import string
from nltk.stem.lancaster import LancasterStemmer
import json
import pickle
import requests
import re
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from framework.constants import log as log

nltk.download('punkt')
nltk.download('stopwords')

# Create tokenizer
stemmer = LancasterStemmer()
stopwords = nltk.corpus.stopwords.words('english')
stopwords.extend(string.punctuation)
stopwords.append('')
tokenizer = nltk.tokenize.WordPunctTokenizer()

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
    message = inp
    with open("nlp/intents.json",'rb') as f:
        data = json.load(f)
    maxi = 0
    response_item = None
    for items in data["intents"]:
        # regex = ''
        for b in items["patterns"]:
            match = get_jaccard_sim(b,message)
            log.debug(str(match))
            # log.info("maxi : ", maxi)
            if(match > maxi):
                maxi = match
                response_item = items
                # log.info("maxi changes : ", maxi)
    if response_item is None:
        return "Sorry I do not understand"
    else: 
        responses = response_item['responses']
        return random.choice(responses)


def get_cosine_sim(*strs): 
    vectors = [t for t in get_vectors(*strs)]
    return cosine_similarity(vectors)


def get_vectors(*strs):
    text = [t for t in strs]
    log.debug(text)
    vectorizer = CountVectorizer(text)
    log.debug(vectorizer)
    vectorizer.fit(text)
    return vectorizer.transform(text).toarray()


def get_jaccard_sim(str1, str2): 
    a = set(str1.lower().split()) 
    # log.debug("intent: ", a)
    b = set(str2.lower().split())
    # log.debug("input :", b)
    c = a.intersection(b)
    return float(len(c)) / (len(a) + len(b) - len(c))

def is_ci_token_stopword_match(a, b):
    """Check if a and b are matches."""
    tokens_a = [token.lower().strip(string.punctuation) for token in tokenizer.tokenize(a) \
                    if token.lower().strip(string.punctuation) not in stopwords]
    log.debug("sentence1: ", tokens_a)
    tokens_b = [token.lower().strip(string.punctuation) for token in tokenizer.tokenize(b) \
                    if token.lower().strip(string.punctuation) not in stopwords]
    log.debug("sentence2: ", tokens_b)
    return (tokens_a == tokens_b)

def bag_of_words(s,words):
    bag = [0 for _ in range(len(words))]
    s_words = nltk.word_tokenize(s)
    log.debug("before: ",s_words)
    s_words1 = [stemmer.stem(word.lower()) for word in s_words if word!="?"]
    log.debug("final: ", s_words1)

