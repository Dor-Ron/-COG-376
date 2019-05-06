'''
Author: Dor Rondel
File: Classifier.py
Program: Naive Bayes Classifier for E-mail Spam Detection
Course: Computational Models of Language Models (COG-376)
Instructor: Prof. Daniel Schlegel
Institution: SUNY Oswego
'''

from os import listdir

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

        self.prob_spam = self.training_spam_count / (self.training_ham_count + self.training_spam_count)
        self.prob_ham = self.training_ham_count / (self.training_ham_count + self.training_spam_count)


    def train_model(self):
        ''' trains naive bayesian model '''

        for _class in self.CLASSES: 
            for fil in listdir("./train/" + _class + "/"):
                if fil.endswith(".txt"):
                    parser = Parser("./train/" + _class + "/" + fil)
                    tup = parser.get_subject_and_body()

                    if _class == "ham":
                        self.training_ham_count += 1
                        
                        # populate ham subject bag of words
                        for word in tup[0]:
                            if word in self.training_ham_subject_bag:
                                self.training_ham_subject_bag[word] += 1
                            else:
                                self.training_ham_subject_bag[word] = 1

                        # populate ham body bag of words
                        for word in tup[1]:
                            if word in self.training_ham_body_bag:
                                self.training_ham_body_bag[word] += 1
                            else:
                                self.training_ham_body_bag[word] = 1

                    elif _class == "spam":
                        self.training_spam_count += 1

                        # populate spam subject bag of words
                        for word in tup[0]:
                            if word in self.training_spam_subject_bag:
                                self.training_spam_subject_bag[word] += 1
                            else:
                                self.training_spam_subject_bag[word] = 1

                        # populate spam body bag of words
                        for word in tup[1]:
                            if word in self.training_spam_body_bag:
                                self.training_spam_body_bag[word] += 1
                            else:
                                self.training_spam_body_bag[word] = 1
                    else:  # ignore file doesnt adhere with specs
                        continue

        # populate combined bags of words
        for word in self.training_spam_subject_bag:
            self.training_spam_bag_of_words[word] = self.training_spam_subject_bag[word]
        
        for word in self.training_spam_body_bag:
            if word not in self.training_spam_bag_of_words:
                self.training_spam_bag_of_words[word] = self.training_spam_body_bag[word]
            else:
                self.training_spam_bag_of_words[word] += self.training_spam_body_bag[word]

        # now for ham bag
        for word in self.training_ham_subject_bag:
            self.training_ham_bag_of_words[word] = self.training_ham_subject_bag[word]
        
        for word in self.training_ham_body_bag:
            if word not in self.training_ham_bag_of_words:
                self.training_ham_bag_of_words[word] = self.training_ham_body_bag[word]
            else:
                self.training_ham_bag_of_words[word] += self.training_ham_body_bag[word]
    
                
    def test_model(self):
        ''' method to test naive bayes classifier '''

        if self.training_ham_count < 1 or self.training_spam_count < 1:
            print("no training data supplied to classifier, try again\n")
            return None

        # get total amount of tests
        total_tests = 0
        correct = 0
        for _class in self.CLASSES: 
            for fil in listdir("./test/" + _class + "/"):
                if fil.endswith(".txt"):  # proper email file
                    if self.test_email("./test/" + _class + "/" + fil) == _class:
                        correct += 1
                total_tests += 1
        print("Model Accuracy: {}".format(correct / total_tests))
        return None
        

    def find_prob_of_word(self, word, vector):
        ''' finds probability of single word being spammy/hammy '''
        
        # get total count of words in bag        
        total = 0
        for key in vector.keys():
            total += vector[key]

        # get length of vocabulary
        vocab = len(vector)

        if word in vector:
            return (vector[word] + 1) / (total + vocab + 1)
        return 1 / (total + vocab + 1)  #  word not in bag, avoid exceptions

        
    def test_email(self, filepath):
        ''' classifies single email as spam or ham '''
        parser = Parser(filepath)
        tmp_bag = parser.get_subject_and_body()[2]
        spam_odds = self.prob_spam
        ham_odds = self.prob_ham
        for token in tmp_bag:
            spam_odds *= self.find_prob_of_word(token, self.training_spam_bag_of_words)
            ham_odds *= self.find_prob_of_word(token, self.training_ham_bag_of_words)
        return "ham" if ham_odds > spam_odds else "spam"

    
    def test_subject(self, filepath):
        ''' classifies subject words only as spam/ham '''
        parser = Parser(filepath)
        tmp_bag = parser.get_subject_and_body()[0]
        spam_odds = self.prob_spam
        ham_odds = self.prob_ham
        for token in tmp_bag:
            spam_odds *= self.find_prob_of_word(token, self.training_spam_subject_bag)
            ham_odds *= self.find_prob_of_word(token, self.training_ham_subject_bag)
        return "ham" if ham_odds > spam_odds else "spam"


    def test_body(self, filepath):
        ''' classifies email body words only as spam/ham '''
        parser = Parser(filepath)
        tmp_bag = parser.get_subject_and_body()[1]
        spam_odds = self.prob_spam
        ham_odds = self.prob_ham
        for token in tmp_bag:
            spam_odds *= self.find_prob_of_word(token, self.training_spam_body_bag)
            ham_odds *= self.find_prob_of_word(token, self.training_ham_body_bag)
        return "ham" if ham_odds > spam_odds else "spam"