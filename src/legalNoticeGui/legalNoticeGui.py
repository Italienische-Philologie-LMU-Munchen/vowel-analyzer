import os
from pathlib import Path
from PyQt5.QtWidgets import QMainWindow, QLabel, QTextEdit
from PyQt5.QtGui import QIcon


class LegalNoticeGui(QMainWindow):
    def __init__(self):
        super().__init__()

        # Save current directory, so we can access it for icons
        self.current_directory = os.path.dirname(__file__)

        # Title of application window and icon
        self.setWindowTitle("Vowel Analyzer - Legal Notice")

        # Icon handling
        self.window_icon = str(Path(self.current_directory).parent.absolute() /
                               'assets' / 'scale-balanced-solid.svg')
        self.setWindowIcon(QIcon(self.window_icon))

        # Fixed geometry for startup of application
        self.setGeometry(0, 0, 450, 450)
        self.setMinimumSize(450, 450)

        # Heading for legal text to be displayed
        self.legalTextHeading = 'Legal Notice'
        self.lbLegalTextHeading = QLabel(self.legalTextHeading, self)

        # Main legal text to be displayed
        self.legalText = '''Vowel Analyzer
Version: 0.1.0.0 

Copyright: ©2023, GNU GPLv3 License 

Enrico Fantini, LMU Munich and Sascha Resch, LMU Munich'''

        self.lbLegalText = QLabel(self.legalText, self)

        # List of libraries and copyright mentions to be displayed (read only mode!)
        self.legalTextLibraries = '''Software to analyze vowel phonetics in (Old) Italian texts 
        <br/><br/>
        The following resources have been used: 
        <br/><br/>
        PyQt5: https://www.riverbankcomputing.com/static/Docs/PyQt5/, GPL v3-License 
        <br/><br/>
        Pygal: https://github.com/Kozea/pygal,  LGPL 3.0-License
        <br/><br/>
        lxml: https://github.com/lxml/lxml, BSD License: Copyright (c) 2004 Infrae. All rights reserved.
        <br/><br/>
        PyInstaller: https://github.com/pyinstaller/pyinstaller, GNU GPL-License
        <br/><br/>
        python-dotenv: https://github.com/theskumar/python-dotenv, BSD License: Copyright (c) 2014, Saurabh Kumar (python-dotenv), 2013, Ted Tieken (django-dotenv-rw), 2013, Jacob Kaplan-Moss (django-dotenv)
        <br/><br/>
        Free Fontawesome icons: https://fontawesome.com/,  SIL OFL 1.1 license
        <br/><br/>
        Pigar: https://github.com/damnever/pigar, BSD License: Copyright (c) 2020, XiaoChao Dong (@damnever) <dxc.wolf@gmail.com> All rights reserved.'''

        self.lbLegalTextLibraries = QTextEdit(self.legalTextLibraries, self)
        self.lbLegalTextLibraries.setReadOnly(True)

        # Set geometry of widgets
        self.lbLegalTextHeading.setGeometry(10, 10, 300, 40)
        self.lbLegalText.setGeometry(10, 60, 420, 120)
        self.lbLegalTextLibraries.setGeometry(
            10, 190, self.width() - 50, self.height() - 200)

    # Method to handle resizing of window, so widgets aren't distorted
    def resizeEvent(self, event):
        self.lbLegalTextLibraries.setGeometry(
            10, 190, self.width() - 50, self.height() - 200)
        QMainWindow.resizeEvent(self, event)
