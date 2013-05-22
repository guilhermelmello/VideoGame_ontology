import sys
import mainWindow, inserir
from PyQt4 import QtCore, QtGui
from PyQt4.Qt import *

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = mainWindow.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    
    Insert = QtGui.QWidget()
    ins = inserir.Ui_Form()
    ins.setupUi(Insert)
    Insert.show()	
    
    sys.exit(app.exec_())