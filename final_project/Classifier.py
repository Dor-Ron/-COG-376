'''
Author: Dor Rondel
File: Classifier.py
Program: Naive Bayes Classifier for E-mail Spam Detection
Course: Computational Models of Language Models (COG-376)
Instructor: Prof. Daniel Schlegel
Institution: SUNY Oswego
'''

import os

from Email import Email
from Parser import *

class Classifier(object):
    ''' class for naive bayes classifier for email spam detection '''

    CLASSES = ["spam", "ham"]

    def __init__(self):
        ''' constructor for naive bayes email spam classifier '''
        self.training_spam_bag_of_words = {}
        self.training_ham_bag_of_words = {}
        self.training_spam_subject_bag = {}
        self.training_ham_subject_bag = {}
        self.training_spam_body_bag = {}
        self.training_ham_body_bag = {}
        self.training_ham_count = 0
        self.training_spam_count = 0
        self.train_model()

    def train_model(self):
        ''' trains naive bayesian model '''
        for _class in self.CLASSES: 
            for fil in os.listdir("./train/" + _class + "/"):
                if fil.endswith(".txt"):
                    parser = Parser("./train/" + _class + "/" + fil)
                    tup = parser.get_subject_and_body()

                    if _class == "ham":
                        self.training_ham_count += 1
                        
                        # populate subject bag of words
                        for word in tup[0]:
                            if word in self.training_ham_subject_bag:
                                self.training_ham_subject_bag[word] += 1
                            else:
                                self.training_ham_subject_bag[word] = 1

                        # populate body bag of words
                        for word in tup[1]:
                            if word in self.training_ham_body_bag:
                                self.training_ham_body_bag[word] += 1
                            else:
                                self.training_ham_body_bag[word] = 1

                        # populate combined bag of words
                        for word in tup[2]:
                            if word in self.training_ham_bag_of_words:
                                self.training_ham_bag_of_words[word] += 1
                            else:
                                self.training_ham_bag_of_words[word] = 1

                    elif fil.endswith(".txt") and _class == "spam":
                        self.training_spam_count += 1

                        # populate subject bag of words
                        for word in tup[0]:
                            if word in self.training_spam_subject_bag:
                                self.training_spam_subject_bag[word] += 1
                            else:
                                self.training_spam_subject_bag[word] = 1

                        # populate body bag of words
                        for word in tup[1]:
                            if word in self.training_spam_body_bag:
                                self.training_spam_body_bag[word] += 1
                            else:
                                self.training_spam_body_bag[word] = 1
                    else:  # ignore file
                        continue

        # populate combined bag of words
        #NEEDS TO BE DONE
    
                

c = Classifier()
print(c.training_ham_bag_of_words)