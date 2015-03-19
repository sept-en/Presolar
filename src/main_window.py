from PyQt4 import QtGui, QtCore
import analyzer


class MainWindow (QtGui.QWidget):
    def __init__ (self, parent=None):
        super (QtGui.QWidget, self).__init__ (parent)

        # create analyzer
        self.analyzer = analyzer.Analyzer("../datasets.json")

        self.mainGrid = QtGui.QGridLayout ()
        #self.mainGrid.resize (800, 600)
        
        self.basicAnalysisBox = QtGui.QVBoxLayout()
        
        # first line : userInput and searchButton
        userFirstLine = QtGui.QHBoxLayout()
        self.userInputLine = QtGui.QLineEdit()
        self.userInputLine.resize (200, 50)
        searchButton = QtGui.QPushButton ("Search")
        searchButton.clicked.connect (self.searchButtonClicked)

        userFirstLine.addWidget (self.userInputLine)
        userFirstLine.addWidget (searchButton)

        # second line : box with the result of analysis
        userSecondLine = QtGui.QHBoxLayout()
        self.userResultBox = QtGui.QTextEdit()
        self.userResultBox.setReadOnly (True)
        userSecondLine.addWidget (self.userResultBox)

        self.basicAnalysisBox.addLayout (userFirstLine)
        self.basicAnalysisBox.addLayout (userSecondLine)
        
        self.setWindowTitle ("Presolar")
        self.resize (800, 600)
        self.setLayout (self.basicAnalysisBox)


    def searchButtonClicked (self, e):
        userInputText = self.userInputLine.text()
        
        if userInputText == "":
            self.userResultBox.setText ("Invalid input.")
            return

        userInputText = str (userInputText).split (' ')
        country = userInputText[0]
        city = userInputText[1]

        energyPerHour, paybackTermMonths = self.analyzer.predict (country, city)
        resultStr = "Energy per hour by panel: " + str (energyPerHour) + \
                "\nPayback term: " + str (paybackTermMonths) + " months."
        self.userResultBox.setPlainText (resultStr)

    def keyPressEvent (self, e):
        if e.key() == QtCore.Qt.Key_Return or e.key() == QtCore.Qt.Key_Enter:
                self.searchButtonClicked (None)
        
