import argparse
from deconstructor import Deconstructor
import ast

parser = argparse.ArgumentParser(description="Readable username generator.")
parser.add_argument("-d", "--deconstruct", type=str, help="Path to the file to deconstruct into transition table")
parser.add_argument("-t", "--train", type=str, help="If flag is present it will train the Markov model based on the transition table")
args = parser.parse_args()

deconstruct = Deconstructor(lang="en")

if args.deconstruct:
    with open("syllabels_table.txt", "w") as file:
        for k, v in deconstruct.syllabyze(args.deconstruct).items():
            file.write(k + "->" + str(v) + "\n")

if args.train:
    deconstruct.train(args.train)