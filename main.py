import argparse
from deconstructor import Deconstructor

parser = argparse.ArgumentParser(description="Readable username generator.")
parser.add_argument("-d", "--deconstruct", type=str, help="Path to the file to deconstruct into transition table")
parser.add_argument("-t", "--train", action="store_true", help="If flag is present it will train the Markov model based on the transition table")
args = parser.parse_args()

deconstrct = Deconstructor()

if args.deconstruct:
    deconstrct.deconstruct(args.deconstruct)