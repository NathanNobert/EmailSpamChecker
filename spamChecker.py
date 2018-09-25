import os
import sys
import glob
import fnmatch
import math

hamGroup = {}
spamGroup = {}

inputFileHamGroup = {}
sumHam = 0
inputFileSpamGroup = {}
sumSpam = 0

for filename in glob.glob('probability_ham_words.txt'):
    with open(filename, 'r') as fd:
        for line in fd:
            word = line.split(None, 1)[0]
            probability = line[-16:]
            hamGroup[word] = probability


for filename in glob.glob('probability_spam_words.txt'):
    with open(filename, 'r') as fd:
        for line in fd:
            word = line.split(None, 1)[0]
            probability = line[-16:]
            spamGroup[word] = probability


del hamGroup['HAM']
del hamGroup['Left']
del spamGroup['SPAM']
del spamGroup['Left']

hamGroupFloat = dict((k,float(v)) for k,v in hamGroup.items())
spamGroupFloat = dict((k,float(v)) for k,v in spamGroup.items())

inputFile = open('./Test/test_Lemmatized/' + sys.argv[1], 'r')
with inputFile as IF:
    fileContents = IF.read().split()
    for word in fileContents:
        if(word in hamGroup):
            hamCount = inputFileHamGroup.get(word, 0)
            inputFileHamGroup[word] = hamCount + 1
        if(word in spamGroup):
            spamCount = inputFileSpamGroup.get(word, 0)
            inputFileSpamGroup[word] = spamCount + 1
            
    inputHamWordList = inputFileHamGroup.keys()
    inputSpamWordList = inputFileSpamGroup.keys()


outputFile = open(sys.argv[2], 'a+')

with outputFile as out:
    out.write('P(SPAM | all words) \n\n\n')
    for key in inputFileSpamGroup:
        calc = spamGroupFloat[key] * inputFileSpamGroup[key]
        sumSpam = sumSpam + calc
        out.write('P(' + str(key) + '|Spam) = ' + str(round(calc, 4)) + '\n')


    out.write('\nLog Score for SPAM: ' + str(round(sumSpam, 4)) + '\n')

    out.write('\n\n\n------------------------------------------\n')
    out.write('------------------------------------------\n\n\n')

    out.write('P(HAM | all words) \n\n\n')
    for key in inputFileHamGroup:
        calc = hamGroupFloat[key] * inputFileHamGroup[key]
        sumHam = sumHam + calc
        out.write('P(' + str(key) + '|Ham) = ' + str(round(calc, 4)) + '\n')
        
    out.write('\n\nLog Score for HAM: ' + str(round(sumHam, 4)) + '\n')
    out.write('Log Score for SPAM: ' + str(round(sumSpam, 4)) + '\n')


    if(sumHam > sumSpam):
        out.write('\nConclusion: This email is classified as HAM')
    else:
        out.write('\nConclusion: This email is classified as SPAM')    
        

