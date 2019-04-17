We currently use two evaluation metrics for this project, Accuracy and BLEU score. These metrics are explained below:

**Accuracy**: We check the prediction of next lyric given the first lyric. If the predicted lyric matches exactly to the correct lyric, accuracy is 1 else it is 0. We compute the average accuracy over all the lyrics pairs in the ground truth and prediction files. Higher accuracy score is better.

**BLEU score**: We also use the BLEU score as a measure of how closely the predicted lyric matches the correct lyric. The BLEU score is obtained by comparing the *n*-gram overlap of candidate text with reference text(s). A thorough discussion on BLEU score can be found in the paper *Papineni et al, 2002, "BLEU: a Method for Automatic Evaluation of Machine Translation"*, URL - https://www.aclweb.org/anthology/P02-1040.pdf . This metric is commonly is used to assess the quality of machine translation but we believe that it suits well for our task as well. We use NLTK's implementation for calculating BLEU score. We assign equal weigths for unigram, bigram and trigram features and assign zero weight for 4-gram ones. Similar to accuracy, higher BLEU score is better.

The score calculation for given ground truth and predicted lyrics is implemented in the Python script 'scoring.py'. It takes as inputs the gound truth lyric pairs (in 'goldfile') and the first and next predicted lyric (in 'predfile'). We can use the script as below:

*python scoring.py --goldfile goldfile --predfile predfile*

Running this evaluation script with the ground truth and prediction files as inputs, we get an Accuracy of 0.11 and a BLEU score of 0.11.