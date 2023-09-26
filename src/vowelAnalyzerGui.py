import os
import tempfile
import platform
import ctypes
from shutil import copyfile
from pathlib import Path
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QCheckBox
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtGui import QIcon
from teiParser import TeiParser
from vowelCalculator import VowelCalculator
from chartExporter import ChartExporter
from legalNoticeGui import LegalNoticeGui


class VowelAnalyzerGui(QMainWindow):
    def __init__(self):
        super().__init__()

        # Variable to check whether we have already run analysis
        self.analysisRun = False

        # Icon handling
        self.current_directory = os.path.dirname(__file__)
        self.window_icon = str(Path(self.current_directory) /
                               'assets' / 'magnifying-glass-chart-solid.svg')
        self.legal_icon = str(Path(self.current_directory) /
                              'assets' / 'scale-balanced-solid.svg')
        self.setWindowIcon(QIcon(self.window_icon))

        # Title of application window
        self.setWindowTitle("Vowel Analyzer")

        # Fixed geometry for startup of application
        self.setGeometry(0, 0, 600, 600)
        self.setMinimumSize(600, 600)

        # Subwindow for legal notice
        self.legalWindow = LegalNoticeGui()

        # Select file button
        self.btFileSelect = QPushButton("Select file", self)
        self.btFileSelect.clicked.connect(self.selectFile)
        # Analysis button
        self.btAnalysis = QPushButton("Run analysis", self)
        self.btAnalysis.clicked.connect(self.runAnalysis)
        # Output button
        self.btOutputDir = QPushButton("Export SVG", self)
        self.btOutputDir.clicked.connect(self.export)
        # Percentage toggle
        self.cbPercentage = QCheckBox("Calculate\r\npercentages", self)
        self.cbPercentage.stateChanged.connect(self.changePercentView)
        # Legal notice
        self.btLegalNotice = QPushButton("Legal Notice", self)
        self.btLegalNotice.clicked.connect(self.legal)
        self.btLegalNotice.setIcon(QIcon(self.legal_icon))

        # Geometry of buttons
        self.btFileSelect.setGeometry(10, 10, 100, 40)
        self.btAnalysis.setGeometry(10, 55, 100, 40)
        self.btOutputDir.setGeometry(10, 100, 100, 40)
        self.cbPercentage.setGeometry(10, 145, 100, 40)
        self.btLegalNotice.setGeometry(10, 190, 100, 40)

        # Webview to display result SVG
        self.wvResult = QWebEngineView(self)
        self.wvResult.setGeometry(
            120, 10, self.width() - 150, self.height() - 50)

        # Storage attributes for file handling
        self.filepath = ''
        self.filename = ''
        self.output = ''

        # Create temp folder if not existing
        self.temppath = Path(tempfile.gettempdir()) / "VowelAnalyzer"
        self.temppath.mkdir(parents=True, exist_ok=True)

    # Method to select file to be analyzed via dialog box
    def selectFile(self):
        # Set base directory as default
        baseDirectory = str(Path.home() / 'Desktop')
        # Get filepath from dialog
        self.filepath, filter = QFileDialog.getOpenFileName(self, 'Open file',
                                                            baseDirectory, "XML files (*.xml)")
        # Get filename
        self.filename = os.path.splitext(os.path.basename(self.filepath))[0]

    # Method to export analysis results into SVG file using dialog box
    def export(self):
        # Get path where to store file
        self.output = Path(str(QFileDialog.getExistingDirectory(
            self, "Select Directory")))
        # Copy file from internal temp storage to selected storage
        copyfile(str(self.temppath / (self.filename + '.svg')),
                 str(self.output / (self.filename + '.svg')))

    # Method to run analysis
    def runAnalysis(self):
        # Only proceed if we have a file defined
        if self.filepath != '':
            # Use TeiParser to read file
            teiParserObject = TeiParser(self.filepath)

            # Get results of vowel calculation considering percentage mode
            vowelCalcObject = VowelCalculator(teiParserObject.parse())
            if (self.cbPercentage.isChecked()):
                vowelResult = vowelCalcObject.calcpercentage()
            else:
                vowelResult = vowelCalcObject.calc()

            # Handle saving of results into chart considering percentage mode
            chartExporterObject = ChartExporter(
                vowelResult[0], vowelResult[1], self.filename, str(self.temppath / (self.filename + '.svg')))
            if (self.cbPercentage.isChecked()):
                chartExporterObject.exportPercentage()
            else:
                chartExporterObject.export()

            # Load saved chart results into web view to display them
            self.wvResult.load(
                QUrl("file:"+(self.temppath / (self.filename + '.svg')).as_posix()))

            # Set value to indicate that we have performed first analysis
            self.analysisRun = True

    # Method to handle change of percentage mode
    def changePercentView(self, event):
        # If we have performed first analysis, we want to display percentage mode change directly in our window
        # So we rerun analysis
        if (self.analysisRun):
            self.analysisRun(self)

    # Method to show legal notice window
    def legal(self):
        self.legalWindow.show()

    # Method to handle resizing of window, so our widgets don't get distorted
    def resizeEvent(self, event):
        self.wvResult.setGeometry(
            120, 10, self.width() - 150, self.height() - 50)
        QMainWindow.resizeEvent(self, event)


def main():
    # Start application and load main window
    app = QApplication([])
    window = VowelAnalyzerGui()
    # Set taskbar icon depending on OS
    if (platform.system() == 'Windows'):
        myappid = 'lmu.italianphilology.vowelanalyzer.0'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    if (platform.system() == 'Darwin'):
        app.setWindowIcon(QIcon(window.window_icon))
    # Show window and execute application
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
