We implement a very simple baseline for Milestone 2. We first randomly select 100 pairs of lyric sequences. For each of the first lyric, we also select 9 other random lyrics. The ground truth therefore contains 100 pairs of true lyric sequences. The prediction involves selecting the second lyric randomly from the 10 available lyrics for each of the 100 first lyrics. 

The ground truth sequences are stored in a file named 'goldfile', while the prediction sequences are stored in a file named 'predfile'. The baseline is implemented in the Python script 'simple-baseline.py'. It takes as an input the training/validation/test file in CSV format, depending on what we are trying to evaluate. We can use the script as below:

*python simple-baseline.py --datafile data/<operation_type>_rock.csv*<br>

For the test data ('test_rock.csv'), we get the 'goldfile' and 'predfile' files. A few sample predictions are shown below. The first column is the first lyric, the second column is the true next lyric and the last column is the predicted next lyric:

| First_Lyric                   | Second_Lyric_True                           | Second_Lyric_Predicted              |
|-------------------------------|---------------------------------------------|-------------------------------------|
| Been screamin' out your name, | I wake up in a sweat,                       | In fact I think I wish you would    |
| Make my dad pay the bill      | Yeah man, that's heaven to me               | I deserve this!                     |
| Now I'm the invisible man     | My head is spinning round faster and faster | 'Cause I got voices down inside me, |

Running the evaluation script 'scoring.py' with these ground truth and prediction files as inputs, we get an Accuracy of 0.11 and a BLEU score of 0.11.