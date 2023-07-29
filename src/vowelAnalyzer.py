import sys
import getopt
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
        print(err)  # will print something like "option -a not recognized"
        sys.exit(2)

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
        # assert False, "unhandled option"

    # Only proceed if we have an input file
    if inputFile != '' and outputDirectory != '':
        teiParserObject = TeiParser(inputFile)

        vowelCalcObject = VowelCalculator(teiParserObject.parse())
        if (percentage):
            vowelResult = vowelCalcObject.calcpercentage()
        else:
            vowelResult = vowelCalcObject.calc()

        chartExporterObject = ChartExporter(
            vowelResult[0], vowelResult[1], inputFile, outputDirectory)
        if (percentage):
            chartExporterObject.exportPercentage()
        else:
            chartExporterObject.export()

    else:
        print("Error: No input file provided")


if __name__ == "__main__":
    main()
