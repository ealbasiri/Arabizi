#!/usr/bin/env python
from typing import Iterable, List, Optional, Tuple
#from itertools import izip
from jiwer import wer
import argparse


def main(args: argparse.Namespace) -> None:

    target_list = []
    hypothesis_list = []
    correct = 0
    incorrect = 0
    with open(args.output, "r") as f1, open(args.target) as f2:
        for line in f1:
            lines = line.rstrip()
            words = lines.split() 
            target_list.append(words)
        for line in f2:  
            lines = line.rstrip()
            words = lines.split() 
            hypothesis_list.append(words)
    

        for t, h in zip(target_list, hypothesis_list):
            for w1, w2 in zip(t, h):
                error = wer(w1, w2)
                print(w1, w2, error)
                if error == 0.0:
                    correct += 1
                else:
                    incorrect += 1

    my_WER = incorrect / (correct + incorrect)
    print(f"WER:\t{my_WER * 100:.2f}")
    print(correct)
    print(incorrect)
    #len(target_list)
    #len(hypothesis_list)
    #print(target_list)
    #print(hypothesis_list)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "output",
        help="path to output file",
    )
    parser.add_argument(
        "target",  help="path to target file"
    )
    main(parser.parse_args())
