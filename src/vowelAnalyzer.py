import sys
import getopt
from teiParser import TeiParser
from vowelCalculator import VowelCalculator
from tableExporter import TableExporter
from chartExporter import ChartExporter


def main():
    # Get command line arguments
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:o:", ["help", "output="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        sys.exit(2)

    inputFile = ''
    outputDirectory = ''
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt == "-i":
            inputFile = arg
        elif opt == "-o":
            outputDirectory = arg
        assert False, "unhandled option"

    # Only proceed if we have an input file
    if inputFile != '':
        print()
    else:
        print("Error: No input file provided")


if __name__ == "__main__":
    main()
