import argparse
from . import run

print(f"package :: running as a script\n{__file__}")

parser = argparse.ArgumentParser()
parser.add_argument('a', type=int)
parser.add_argument('b', type=str)

run(**vars(parser.parse_args()))
