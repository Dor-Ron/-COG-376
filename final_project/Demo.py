'''
Author: Dor Rondel
File: demo.py
Program: Naive Bayes Classifier for E-mail Spam Detection
Course: Computational Models of Language Models (COG-376)
Instructor: Prof. Daniel Schlegel
Institution: SUNY Oswego
'''

from os import listdir
from time import sleep

from Classifier import Classifier
from Parser import Parser

bayes = Classifier()
parser = None

for _class in ["spam", "ham"]: 
    for fil in listdir("./test/" + _class + "/"):
        if fil.endswith(".txt"):
            filepath = "./test/" + _class + "/" + fil

            subject = ""
            body = ""

            with open(filepath, encoding = 'utf-8', errors = 'ignore') as fil:
                for line in fil.readlines():
                    if line[:8].lower() == "subject:":
                        subject = line
                        continue
                    else:
                        body += line + "\n"

            print(subject)
            print(bayes.test_subject(filepath))
            print()

            print(body)
            print(bayes.test_body(filepath))
            print()

            print("Total Classification {}".format(bayes.test_email(filepath)))
            print()
            print("-------------------------------------------------")
            print()
            sleep(5)
