from PyQt4 import QtGui, QtCore
import analyzer
import dataset

class MainWindow (QtGui.QWidget):
    def __init__ (self, parent=None):
        super (QtGui.QWidget, self).__init__ (parent)

        # create analyzer
        self.analyzer = analyzer.Analyzer("../datasets.json")

        self.mainGrid = QtGui.QVBoxLayout ()
        
        self.commonTopPanel = QtGui.QVBoxLayout()
        self.basicAnalysisBox = QtGui.QVBoxLayout()
        self.advancedAnalysisBox = QtGui.QVBoxLayout()

        font = QtGui.QFont()
        font.setPointSize (16)
        
        """
        Basic tab
        """
        # first line : select country,city comboboxes and searchButton
        # combobox country
        self.standardSelectCountry = QtGui.QComboBox()
        self.standardSelectCountry.addItems (dataset.Dataset.getCountries (self.analyzer.datasets))
        self.standardSelectCountry.currentIndexChanged.connect (self.countryIndexChanged)
        self.standardSelectCountry.setFont (font)
        self.standardSelectCountry.setMaxVisibleItems (6)
        # combobox city
        self.standardSelectCity = QtGui.QComboBox()
        self.standardSelectCity.setEnabled (False)
        self.standardSelectCity.setFont (font)
        self.standardSelectCity.setMaxVisibleItems (6)
        # search button
        searchButton = QtGui.QPushButton ("Search")
        searchButton.clicked.connect (self.searchButtonClicked)
        searchButton.setFont (font)

        # create layout for first line
        userInputPanel = QtGui.QHBoxLayout()
        logoLbl = QtGui.QLabel()
        logoLbl.setPixmap (QtGui.QPixmap ("../presolar_logo.png"))
        logoLbl.setScaledContents (True)
        logoLbl.setFixedSize (30, 30)

        userInputPanel.addWidget (logoLbl)
        userInputPanel.addWidget (self.standardSelectCountry)
        userInputPanel.addWidget (self.standardSelectCity)
        userInputPanel.addWidget (searchButton)

        self.basicResultBox = QtGui.QTextEdit()
        self.basicResultBox.setReadOnly (True)
        self.basicResultBox.setFont (font)
        basicLayout = QtGui.QHBoxLayout()
        basicLayout.addWidget (self.basicResultBox)

        self.commonTopPanel.addLayout (userInputPanel)
        self.basicAnalysisBox.addLayout (basicLayout)

        """
        Advanced tab
        """
        # Advanced cost of panel textedit and label
        self.advancedCostOfPanelEdit = QtGui.QLineEdit()
        advancedCostOfPanelLbl = QtGui.QLabel ("&Cost of panel:")
        advancedCostOfPanelLbl.setBuddy (self.advancedCostOfPanelEdit)
        # Advanced power of panel and label
        self.advancedPowerOfPanelEdit = QtGui.QLineEdit()
        advancedPowerOfPanelLbl = QtGui.QLabel ("&Power of panel:")
        advancedPowerOfPanelLbl.setBuddy (self.advancedPowerOfPanelEdit)
        # Advanced count of panel textedit and label
        self.advancedCountOfPanelsEdit = QtGui.QLineEdit()
        advancedCountOfPanelsLbl = QtGui.QLabel ("&Quantity of panels:")
        advancedCountOfPanelsLbl.setBuddy (self.advancedCountOfPanelsEdit)
        
        # Create layout for advanced tab
        advancedCostLayout = QtGui.QVBoxLayout()
        advancedCostLayout.addWidget (advancedCostOfPanelLbl)
        advancedCostLayout.addWidget (self.advancedCostOfPanelEdit)
        advancedPowerLayout = QtGui.QVBoxLayout()
        advancedPowerLayout.addWidget (advancedPowerOfPanelLbl)
        advancedPowerLayout.addWidget (self.advancedPowerOfPanelEdit)
        advancedCountLayout = QtGui.QVBoxLayout()
        advancedCountLayout.addWidget (advancedCountOfPanelsLbl)
        advancedCountLayout.addWidget (self.advancedCountOfPanelsEdit)

        advancedTabInputLayout = QtGui.QHBoxLayout()
        advancedTabInputLayout.addLayout (advancedCostLayout)
        advancedTabInputLayout.addLayout (advancedPowerLayout)
        advancedTabInputLayout.addLayout (advancedCountLayout)
        self.advancedResultBox = QtGui.QTextEdit()
        self.advancedResultBox.setReadOnly (True)
        self.advancedResultBox.setFont (font)
        self.advancedAnalysisBox = QtGui.QVBoxLayout()
        self.advancedAnalysisBox.addLayout (advancedTabInputLayout)
        self.advancedAnalysisBox.addWidget (self.advancedResultBox)


        """
        Tab widget
        """
        # add tab widget layout
        self.tabWidget = QtGui.QTabWidget()
        basicWidget = QtGui.QWidget()
        basicWidget.setLayout (self.basicAnalysisBox)
        advancedWidget = QtGui.QWidget()
        advancedWidget.setLayout (self.advancedAnalysisBox)
        self.tabWidget.addTab (basicWidget, "Basic")
        self.tabWidget.addTab (advancedWidget, "Advanced")

        self.mainGrid.addLayout (self.commonTopPanel)
        self.mainGrid.addWidget (self.tabWidget)
        
        self.setWindowTitle ("Presolar")
        self.setFixedSize (800, 600)
        icon = QtGui.QIcon ("../presolar_logo.png")
        self.setWindowIcon (icon)
        self.setLayout (self.mainGrid)


    def searchButtonClicked (self, e):
        if (self.standardSelectCountry.currentIndex() < 0 or
            self.standardSelectCity.currentIndex() < 0):
                return

        if self.tabWidget.currentIndex() == 0:
            self.basicTabCalculations()
        else:
            self.advancedTabCalculations()


    def basicTabCalculations (self):
        country = self.standardSelectCountry.currentText() 
        city = self.standardSelectCity.currentText()

        energyPerHour, paybackTermMonths = self.analyzer.predict (country, city)
        resultStr = "Energy per hour by panel (kW/h): " + str ("{:.2f}".format (energyPerHour)) + \
                "\nPayback term: " + str (paybackTermMonths) + " months."
        self.basicResultBox.setPlainText (resultStr)
        self.advancedResultBox.clear()


    def advancedTabCalculations (self):
        country = self.standardSelectCountry.currentText() 
        city = self.standardSelectCity.currentText()

        costOfPanel = int (self.advancedCostOfPanelEdit.text())
        powerOfPanel = int (self.advancedPowerOfPanelEdit.text())
        countOfPanels = int (self.advancedCountOfPanelsEdit.text())
        areaOfPanel = 1

        energyPerHour, paybackTermMonths = self.analyzer.predict (country, city, powerOfPanel,
                areaOfPanel, costOfPanel, countOfPanels)
        
        resultStr = "Energy per hour by panel (kW/h): " + str ("{:.2f}".format (energyPerHour)) + \
                "\nPayback term: " + str (paybackTermMonths) + " months."
        self.advancedResultBox.setPlainText (resultStr)
        self.basicResultBox.clear()


    def keyPressEvent (self, e):
        if e.key() == QtCore.Qt.Key_Return or e.key() == QtCore.Qt.Key_Enter:
                self.searchButtonClicked (None)


    def countryIndexChanged (self, index):
        if (index < 1):
            self.standardSelectCity.clear()
            self.standardSelectCity.setEnabled (False)
            return

        country = self.standardSelectCountry.currentText()
        
        cities = dataset.Dataset.getCitiesByCountry (self.analyzer.datasets, country)
        self.standardSelectCity.clear()
        self.standardSelectCity.addItems (cities)
        self.standardSelectCity.setEnabled (True)

