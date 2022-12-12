import argparse

parser = argparse.ArgumentParser()

parser.add_argument('source', help='File choosing')
parser.add_argument('-m', '-medals', help='Medals', nargs=2)
parser.add_argument('-o', '-output', help='Output in file')
parser.add_argument('-t', '-total', help='Total statistics')

arguments = parser.parse_args()


