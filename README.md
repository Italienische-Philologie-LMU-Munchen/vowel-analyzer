# Vowel Analyzer

**Vowel Analyzer** is a small software to analyze vowel distribution in (old) Italian verse texts in TEI XML format. It can be used as console application or as a GUI application. The software has been developped mainlay on Windows machines, so you might get the ,ost reliable functionality using the application on a Windows machine.

## Background

The software is the result of an introductory seminar to Python programming for philology students in summer 2023 at the institute for Italian philology at LMU Munich. At the end of this seminar, the idea of applying the new knowledge arose and the Enrico Fantini, post doc researcher and participant of the seminar, and Sascha Resch, doctoral candidate and tutor of the Python seminar, decided to create a small application that aims to demonstrate what can be done after one semester of Python training. While Sascha Resch worked mainly on the GUI, the installer and the repository logic, Enrico Fantini developped the main logic of the application.

## Installation/Prerequisities

In order to merely run **Vowel Analyzer** you have to install [Python 3.9.7](https://www.python.org/downloads/) on your machine (other versions might work but haven't been tested yet). This way you should be able to use the pre-built application files from the current release (exe-files for Windows 64-bit machines).

If you want (or need) to build your own version of **Vowel Analyzer**, you have to perform the following steps:

- Download/Clone the source code
- Install all needed Python packages with `pip install -r requirements.txt`
- Run `build.py` to create a [single-file application](https://github.com/s-resch/vowel-analyzer#building-your-own-bundled-executable) or just start `vowelAnalyzer.py` or `vowelAnalyzerGui.py`

## Special prerequisities for Mac M1 architecture

The Mac M1 architecture (released in 2020) requires special actions in order to make Vowel Analyzer work.
- In our test case it was necessary to install the needed libraries manually (so `pip install -r requirements.txt` didn't work)
- We had to install PyQt5 separately - this requires several actions using M1 architecture
  - Consider the following hints to install PyQt5 (Qt5 respectively) on your Mac: https://stackoverflow.com/a/76114212
  - You need to enable an Intel terminal using Rosetta (see the instructions here: https://stackoverflow.com/a/74531940), make sure you have Rosetta installed
  - Now you can open a terminal and type `intel`, to get an Intel terminal
  - In this Intel terminal you can install PyQt5 libraries using `pip`: `pip install PyQt5` and `pip install PyQtWebEngine`


## Usage

Using the application in GUI mode, you will see the following graphical interface:
![GUI interface of Vowel Analyzer](/src/assets/vowel_analyzer.jpg)

- Click `Select file` to choose the TEI XML-file to be analyzed
- Click `Run analysis` to perform the vowel calculation for the chosen TEI XML-file
- Activate `Calculate percentages` to get results as percentages, if not activated the absolute number of vowels will be displayed
- Click `Export SVG` to save the chart with results (displayed in the main view on the right side of the application) to any directory of your machine
- Click `Legal notice` to view information about the application and legal notices for libraries used

## Building your own bundled executable

In order to build your own bundled executable, you have to run `build.py`. The building process can take several minutes. In the end you should find an executable file in a newly created folder `dist`.

You can change the type of application to be built using the `.env` file by changing the `APP_MODE` value:
`APP_MODE=gui`
or
`APP_MODE=console`

Be aware that the building process has been tested with on a Windows 11 64-bit machine. For other systems you might need to change the code of `build.py` and the PyInstaller configuration.

## Roadmap

The following features are to be implemented in further versions of the software

- Improved support for Mac
- Support for Linux systems
- Error handling for malformed TEI-XML documents
- Error handling for other documents than TEI-XML documents
- Logging of errors and warnings
- Accept other texts than verse texts
- Accept texts in other languages with specific vowel settings (diacritics)
- Offer more types of charts to display the results
- Compare the results with standard distribution of vowels in a certain language
- Try to reduce file size for bundled executable by PyInstaller
- Improve startup performance of bundled executable by PyInstaller
- Maybe switch to another deployment/installer than PyInstaller (e.g., copying files into system directory (such as "Program Files" on Windows) and using .bat/.sh-file to start application)
- Upgrade to Python 3.11 or higher
- ...
