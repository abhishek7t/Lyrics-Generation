We are using two evaluation metrics, BLEU score and accuracy. They are explained below:

Accuracy:   We check the prediction of next sentence given a sentence. 
            If the predicted sentence matches exactly to the correct one accuracy is one else it is zero.
            We compute the average accuracy over all the sentence pairs. 
            Higher score is better.

BLEU score: We use BLUE score as a measure of how closely the predicted sentence matches the correct sentence in the gold set.
            It works by comparing n-gram overlap of candidate with reference.
            A thorough discussion on BLUE can be found on https://www.aclweb.org/anthology/P02-1040.pdf .
            This metric is commonly is used to assess the quality of machine translation but we think that it suits well for 
            our task as well. 
            We are using NLTK's implementation for calculating BLUE score. We have assigned equal weigths for unigram, bigram and trigram
            , and zero weight for four-gram.
            Again, higher score is better.


To Run: python scoring.py --goldfile goldfile --predfile predfile

goldfile: file containig a pair of true sequences of text in each line.
predfile: file containig the first and predicted next sentence in each line.

A sample output is as below:
    Accuracy: 0.17
    BLEU score: 0.15