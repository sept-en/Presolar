import sys
from PyQt4 import QtCore, QtGui
from main_window import *


if __name__=='__main__':
    app = QtGui.QApplication (sys.argv)
    window = MainWindow()
    window.show()
    sys.exit (app.exec_())
