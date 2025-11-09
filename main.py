import argparse
from deconstructor import Deconstructor
import ast
from generator import Generator

parser = argparse.ArgumentParser(description="Readable username generator.")
parser.add_argument("-d", "--deconstruct", type=str, help="Path to the file to deconstruct into transition table")
parser.add_argument("-t", "--train", type=str, help="If flag is present it will train the Markov model based on the transition table")
parser.add_argument("-m", "--model", type=str, help="Path of the model file to use for generation")
parser.add_argument("-l", "--length", type=int, help="Length (in syllables) of the username", default=5)
parser.add_argument("-tmp", "--temperature", type=float, help="Temperature to use for username generation", default=0.5)
args = parser.parse_args()

deconstruct = Deconstructor(lang="en")
generator = Generator()

if args.deconstruct:
    with open("syllabels_table.txt", "w") as file:
        for k, v in deconstruct.syllabyze(args.deconstruct).items():
            file.write(k + "->" + str(v) + "\n")

if args.train:
    deconstruct.train(args.train)

if args.model:
    username = generator.generate(length=args.length, modelfile_path=args.model, temperature=args.temperature)
    print(username)