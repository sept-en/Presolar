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
        
        # first line : select country,city comboboxes and searchButton
        userFirstLine = QtGui.QHBoxLayout()
        self.standardSelectCountry = QtGui.QComboBox()
        self.standardSelectCity = QtGui.QComboBox()
        #self.standardSelectCountry.setLineEdit ("Select country")
        #self.standardSelectCity.setLineEdit ("Select city")
        self.standardSelectCity.setEnabled (False)
        searchButton = QtGui.QPushButton ("Search")
        searchButton.clicked.connect (self.searchButtonClicked)

        userFirstLine.addWidget (self.standardSelectCountry)
        userFirstLine.addWidget (self.standardSelectCity)
        userFirstLine.addWidget (searchButton)

        # second line : box with the result of analysis
        userSecondLine = QtGui.QHBoxLayout()
        self.userResultBox = QtGui.QTextEdit()
        self.userResultBox.setReadOnly (True)
        userSecondLine.addWidget (self.userResultBox)

        self.basicAnalysisBox.addLayout (userFirstLine)
        self.basicAnalysisBox.addLayout (userSecondLine)
        
        self.setWindowTitle ("Presolar")
        self.setFixedSize (800, 600)
        self.setLayout (self.basicAnalysisBox)


    def searchButtonClicked (self, e):
        return
        userInputText = self.userInputLine.text()
        
        energyPerHour, paybackTermMonths = self.analyzer.predict (country, city)
        resultStr = "Energy per hour by panel: " + str (energyPerHour) + \
                "\nPayback term: " + str (paybackTermMonths) + " months."
        self.userResultBox.setPlainText (resultStr)

    def keyPressEvent (self, e):
        if e.key() == QtCore.Qt.Key_Return or e.key() == QtCore.Qt.Key_Enter:
                self.searchButtonClicked (None)
        
