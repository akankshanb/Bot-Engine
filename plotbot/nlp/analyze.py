import numpy as np
import random
import string # to process standard python strings
import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
import json
import pickle
import requests
# f=open('chatbot.txt','r',errors = 'ignore')
# raw=f.read()
# raw=raw.lower()# converts to lowercase
# nltk.download('punkt') # first-time use only
# nltk.download('wordnet') # first-time use only
# sent_tokens = nltk.sent_tokenize(raw)# converts to list of sentences 
# word_tokens = nltk.word_tokenize(raw)# converts to list of words

def eventhandle(inp):
    message = inp["text"]
    with open("intents.json",'rb') as f:
        # data = json.dumps(f)
        data = json.load(f)
    # print(data)
    s_words = nltk.word_tokenize(message)
    # s_words1 = [stemmer.stem(word.lower()) for word in s_words]
    print(s_words)
    for tag in data["intents"]:
        if tag['tag'] == inp["trigger_word"]:
            responses = tag['responses']
    response = random.choice(responses)
    # print(response)

def bag_of_words(s,words):
    bag = [0 for _ in range(len(words))]
    s_words = nltk.word_tokenize(s)
    print("before: ",s_words)
    s_words1 = [stemmer.stem(word.lower()) for word in s_words if word!="?"]
    print("final: ", s_words1)

if __name__ == "__main__":
    inpt = {'token': 'nx3mp3xph3yz5ecwkskzi1ntcc', 'team_id': 'wtpx8yiowtbs5nes6adqcdco1e', 'team_domain': 'plotbotteam', 'channel_id': '85i3du788tgadqtz8mao6ctqma', 'channel_name': 'off-topic', 'timestamp': 1572374487583, 'user_id': '69i1gy344tygdychdcmppf658h', 'user_name': 'akankshanb', 'post_id': 'f38grtj7ut8fuqoaw4w6stexdw', 'text': '@plotbot how are?', 'trigger_word': '@plotbot', 'file_ids': ''}

    # data = {}
    # data['people'] = []
    # data['people'].append({
    #     'name': 'Scott',
    #     'website': 'stackabuse.com',
    #     'from': 'Nebraska'
    # })
    # data['people'].append({
    #     'name': 'Larry',
    #     'website': 'google.com',
    #     'from': 'Michigan'
    # })
    # data['people'].append({
    #     'name': 'Tim',
    #     'website': 'apple.com',
    #     'from': 'Alabama'
    # })

    # with open('data.txt', 'w') as outfile:
    #     json.dump(data, outfile)
    eventhandle(inpt)




