'''
Author: Dor Rondel
File: Email.py
Program: Naive Bayes Classifier for E-mail Spam Detection
Course: Computational Models of Language Models (COG-376)
Instructor: Prof. Daniel Schlegel
Institution: SUNY Oswego
'''

class Email(object):
    ''' class to represent emails from Enron training/test datasets '''

    def __init__(self, _subject, _body, _spam = False):
        ''' constructor for Email object '''
        self.subject = _subject
        self.body = _body
        self.is_spam = _spam

    def set_spam(self, _bool):
        ''' void setter for is_spam '''
        self.is_spam = _bool