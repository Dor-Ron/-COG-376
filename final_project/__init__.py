'''
Author: Dor Rondel
File: __init__.py
Program: Naive Bayes Classifier for E-mail Spam Detection
Course: Computational Models of Language Models (COG-376)
Instructor: Prof. Daniel Schlegel
Institution: SUNY Oswego
'''

from Classifier import Classifier

if __name__ == "__main__":
    print("Building model")
    print("Training model on emails under ./train/*")
    bayes = Classifier()
    print("Testing model on emails under ./test/*")
    print(bayes.test_model())