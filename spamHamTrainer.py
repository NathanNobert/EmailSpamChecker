import os
import sys
import glob
import fnmatch
import math

spamGroup = {}
hamGroup = {}
spamWordCount = 0
hamWordCount = 0

for filename in glob.glob('./Train/train_Lemmatized/*.txt'):
    if(fnmatch.fnmatch(filename, '*spm*.txt')):
       with open(filename, 'r') as fd:
            fileContents = fd.read().split()
            for word in fileContents:
                count = spamGroup.get(word, 0)
                spamGroup[word] = count + 1
                spamWordCount = spamWordCount + 1
            spamWordList = spamGroup.keys()
    else:
        with open(filename, 'r') as fd:
            fileContents = fd.read().split()
            for word in fileContents:
                count = hamGroup.get(word, 0)
                hamGroup[word] = count + 1
                hamWordCount = hamWordCount + 1
            hamWordList = hamGroup.keys()

spamProbFile = open('probability_spam_words.txt', 'a+')
hamProbFile = open('probability_ham_words.txt', 'a+')

with spamProbFile as spamOut:
    spamOut.write('SPAM WORDS PROBABILITY \n')
    spamOut.write('Left word is the word, to the right is the count, then probability after LOG. \n')
    for i in sorted(spamWordList):
        spamOut.write("{0:<15s}".format(str(i)) + ' == count: ' +  "{0:<5s}".format(str(spamGroup[i]))
                      + ' == Probability: ' +  '%.15s' %str(math.log(spamGroup[i]/spamWordCount)) + '\n')
spamProbFile.close()

with hamProbFile as hamOut:
    hamOut.write('HAM WORDS PROBABILITY \n')
    hamOut.write('Left word is the word, to the right is the count, then probability after LOG. \n')
    for i in sorted(hamWordList):
        hamOut.write("{0:<15s}".format(str(i)) + ' == count: ' +  "{0:<5s}".format(str(hamGroup[i]))
                      + ' == Probability: ' +  '%.15s' %str(math.log(hamGroup[i]/hamWordCount)) + '\n')
hamProbFile.close()
