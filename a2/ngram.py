# ngram_observations.py
# An set of functions for examining characteristics of ngrams.
# Author: Daniel R. Schlegel
# Modified: 2/27/19
 
'''
How to use this program:
 
First, if you are using Thonny and haven't yet installed nltk, from the Tools menu choose Manage Packages. In the window that appears type
nltk and hit the Search button. Then once it is found, click the Install button. You may now close that window. Then, in the console at the bottom of Thonny, type: 
 
import nltk
nltk.download('punkt') 
 
and hit enter. It will take a minute to download some required files.
 
Then:
 
1) At the bottom of this file, change the file location to the location of the input file you want to use.
2) Load the program into Python. It will take a few seconds to build unigrams through 5-grams.
3) Run commands like the following:
 
print_ngram_freq_list(unigrams, top=100, pattern=None)
 
This will get the top 100 unigrams along with their counts from the corpus.
 
You can:
- Change unigrams to bigrams, trigrams, quadrigrams, or pentagrams to look at the top results for those.
- Change top=100 to a different value (top=10, top=50, ...) to get a different number of results.
- Add a regular expression pattern to only get ngrams which match that pattern. 
 
More example usages:
 
print_ngram_freq_list(bigrams, top=5, pattern='ing')
 
This gets the top 5 bigrams that contain 'ing'.
 
print_ngram_freq_list(trigrams, top=5, pattern='^w+ings')
 
This gets the top 5 bigrams where the first word contains 'ings'
 
More advanced usage:
- You can create ngrams of any length by following the form used at the bottom of the file to create the unigrams etc. 
'''
 
import random
import nltk
import re
import collections
from nltk import word_tokenize
 
def tokenize_file(fname):
    file = open(fname, errors='ignore')
    return nltk.word_tokenize(file.read())
 
# This function gets the raw ngrams, without figuring out counts, duplicates, etc.
# Optionally takes a regular expression pattern as an argument, then only returns
# ngrams which match that pattern.
def get_ngrams(all_tokens, length, pattern = None):
    ngrams = []
    p = None
    if(pattern):
        p = re.compile(pattern)
    for x in range(0, len(all_tokens)-length+1):
        if p:
            if p.search(' '.join(all_tokens[x:x+length])):
                ngrams.append(all_tokens[x:x+length])
        else:
            ngrams.append(all_tokens[x:x+length])
    return ngrams
 
def print_ngram_freq_list(ngrams, top=None, pattern=None):
    length = len(ngrams[0])
    ngram_strs = [' '.join(x) for x in ngrams]
    freqs = collections.Counter(ngram_strs)
    if(pattern):
        p = re.compile(pattern)
        outcounts = {k: v for k, v in freqs.items() if p.search(k)}
    else:
        outcounts = freqs
    sorted_outcounts = [(k, outcounts[k]) for k in sorted(outcounts, key=outcounts.get, reverse=True)]
    if top == None:
        top = len(sorted_outcounts)
    for i in range(min(top,len(sorted_outcounts))):
        (k, v) = sorted_outcounts[i]
        print(v, k)
    if len(sorted_outcounts) == 0:
        print("No Matches.")
    return None
 

corporas = [
    "ccae_fiction.txt",
    "ccae_news.txt",
    "sbcsae.txt"
]

# Be sure to use forward slashes in your file path!
tokens = tokenize_file(corporas[2])
unigrams = get_ngrams(tokens, 1)
bigrams = get_ngrams(tokens, 2)
trigrams = get_ngrams(tokens, 3)
quadrigrams = get_ngrams(tokens, 4)
pentagrams = get_ngrams(tokens, 5)



# print(unigrams)
#print(bigrams)
# print(len(trigrams))
# print(len(quadrigrams))
# print(len(pentagrams))
print_ngram_freq_list(pentagrams, top=25, pattern=None)
