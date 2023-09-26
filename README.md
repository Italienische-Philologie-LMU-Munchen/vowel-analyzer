# Vowel Analyzer

**Vowel Analyzer** is a small software to analyze vowel distribution in (old) Italian verse texts in TEI XML format. It can be used as console application or as a GUI application. The software has been developped mainlay on Windows machines, so you might get the ,ost reliable functionality using the application on a Windows machine.

## Installation/Prerequisities

In order to merely run **Vowel Analyzer** you have to install Python 3.9 on your machine. This way you should be able to use the pre-built application files from the current release.

If you want (or need) to build your own version of **Vowel Analyzer**, you have to perform the following steps:

- Download/Clone the source code
- Install all needed Python packages with `pip install -r requirements.txt`
- Run `build.py` to create a single-file application or just start `vowelAnalyzer.py` or `vowelAnalyzerGui.py`

## Usage

Using the application in GUI mode, you will see the following graphical interface:
![GUI interface of Vowel Analyzer](/src/assets/vowel_analyzer.jpg)

- Click `Select file` to choose the TEI XML-file to be analyzed
- Click `Run analysis` to perform the vowel calculation for the chosen TEI XML-file
- Activate `Calculate percentages` to get results as percentages, if not activated the absolute number of vowels will be displayed
- Click `Export SVG` to save the chart with results (displayed in the main view on the right side of the application) to any directory of your machine
- Click `Legal notice` to view information about the application and legal notices for libraries used

## Roadmap

The following features are to be implemented in further versions of the software

- Improved support for Mac
- Support for Linux systems
- Error handling for malformed TEI-XML documents
- Error handling for other documents than TEI-XML documents
- Accept other texts than verse texts
- Accept texts in other languages with specific vowel settings (diacritics)
- Offer more types of charts to display the results
- Compare the results with standard distribution of vowels in a certain language
- ...
