
import argparse

def main(args):
    gold = {}
    with open(args.goldfile) as file:
        for line in file:
            line1, line2 = line.strip().split('\t')
            gold[line1] = line2

    pred = {}
    with open(args.predfile) as file:
        for line in file:
            line1, line2 = line.strip().split('\t')
            pred[line1] = line2

    assert len(gold) == len(pred)

    num_correct, num_total = 0, 0
    for line1 in gold:
        assert line1 in pred
        if gold[line1] == pred[line1]:
            num_correct += 1
        num_total += 1

    accuracy = num_correct / num_total
    print(f'Accuracy: {accuracy:.2f}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--goldfile', type=str, required=True)
    parser.add_argument('--predfile', type=str, required=True)

    args = parser.parse_args()
    main(args)