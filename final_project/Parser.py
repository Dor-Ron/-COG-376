'''
Author: Dor Rondel
File: Parse.py
Program: Naive Bayes Classifier for E-mail Spam Detection
Course: Computational Models of Language Models (COG-376)
Instructor: Prof. Daniel Schlegel
Institution: SUNY Oswego
'''

# must download nltk stopwords prior to running script
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

class Parser(object):
    ''' Class to handle parsing Enron test/training spam datasets '''

    def __init__(self, _file):
        ''' constructor for parsing object '''
        self.subject_tokens = set()
        self.body_tokens = set()
        self.tokens = self.tokenize(_file)

    def tokenize(self, _file, stop_words = stopwords.words('english')):
        ''' returns all unique tokens in email body '''
        subj = set()
        body = set()
        with open(_file, encoding='utf-8', errors='ignore') as fil:
            for line in fil.readlines():
                if line[:8].lower() == "subject:":
                    subj = set(word_tokenize(line[9:]))
                else:
                    tmp = word_tokenize(line)
                    tmp2 = set()
                    for token in tmp:
                        if token not in stop_words:
                            tmp2.add(token)
                    body = set(list(body) + list(tmp2))
        self.subject_tokens = subj
        self.body_tokens = body
        
    def get_subject_and_body(self):
        ''' 
        returns tuple of token sets
        index 0 == subject tokens
        index 1 == body tokens
        index 2 == union of index 0 and 1
        '''
        return (self.subject_tokens, self.body_tokens, set(
                list(self.subject_tokens) + list(self.body_tokens)
            )
        )

    def set_body(self, payload):
        ''' setter for body tokens '''
        self.body_tokens = payload

    def set_subject(self, payload):
        ''' setter for subject tokens '''
        self.subject_tokens = payload