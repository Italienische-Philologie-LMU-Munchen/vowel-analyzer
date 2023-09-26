import sys
import getopt
import os
from teiParser import TeiParser
from vowelCalculator import VowelCalculator
from tableExporter import TableExporter
from chartExporter import ChartExporter


def main():
    # Get command line arguments
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:o:p", [
                                   "help", "input=", "output=", "percentage"])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # print "option -a not recognized" or something similar
        sys.exit(2)

    # Handle console line options and store them in appropriate variables
    inputFile = ''
    outputDirectory = ''
    percentage = False

    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile> -o <outputfile> -p')
            sys.exit()
        elif opt == "-i":
            inputFile = arg
        elif opt == "-o":
            outputDirectory = arg
        elif opt == "-p":
            percentage = True

    # Only proceed if we have an input file
    if inputFile != '' and outputDirectory != '':
        # Create Tei Parser to read given file
        teiParserObject = TeiParser(inputFile)

        # Calculate vowel results considering percentage mode
        vowelCalcObject = VowelCalculator(teiParserObject.parse())
        if (percentage):
            vowelResult = vowelCalcObject.calcpercentage()
        else:
            vowelResult = vowelCalcObject.calc()

        # Save results into chart (svg file)
        chartExporterObject = ChartExporter(
            vowelResult[0], vowelResult[1], inputFile, os.path.splitext(os.path.basename(outputDirectory))[0])
        if (percentage):
            chartExporterObject.exportPercentage()
        else:
            chartExporterObject.export()

    else:
        print("Error: No input file provided")


if __name__ == "__main__":
    main()
