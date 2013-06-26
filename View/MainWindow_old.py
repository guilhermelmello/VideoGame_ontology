# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created: Mon Jun 24 18:09:34 2013
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(Qt.QMainWindow):
    def __init__(self, controller):
        Qt.QMainWindow.__init__(self)
        
        self.controller = controller
        
        self.setObjectName(_fromUtf8("MainWindow"))
        self.resize(391, 512)
        self.centralwidget = QtGui.QWidget(self)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.centralTitleLabel = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Gill Sans Ultra Bold"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.centralTitleLabel.setFont(font)
        self.centralTitleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.centralTitleLabel.setObjectName(_fromUtf8("centralTitleLabel"))
        self.verticalLayout.addWidget(self.centralTitleLabel)
        self.centralLayout = QtGui.QGridLayout()
        self.centralLayout.setObjectName(_fromUtf8("centralLayout"))
        self.consoleComboBox = QtGui.QComboBox(self.centralwidget)
        self.consoleComboBox.setObjectName(_fromUtf8("consoleComboBox"))
        self.centralLayout.addWidget(self.consoleComboBox, 3, 1, 1, 1)
        self.nameLabel = QtGui.QLabel(self.centralwidget)
        self.nameLabel.setObjectName(_fromUtf8("nameLabel"))
        self.centralLayout.addWidget(self.nameLabel, 0, 0, 1, 1)
        self.midiaLabel = QtGui.QLabel(self.centralwidget)
        self.midiaLabel.setObjectName(_fromUtf8("midiaLabel"))
        self.centralLayout.addWidget(self.midiaLabel, 2, 0, 1, 1)
        self.consoleLabel = QtGui.QLabel(self.centralwidget)
        self.consoleLabel.setObjectName(_fromUtf8("consoleLabel"))
        self.centralLayout.addWidget(self.consoleLabel, 3, 0, 1, 1)
        self.nameLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.nameLineEdit.setObjectName(_fromUtf8("nameLineEdit"))
        self.centralLayout.addWidget(self.nameLineEdit, 0, 1, 1, 1)
        self.fabricanteComboBox = QtGui.QComboBox(self.centralwidget)
        self.fabricanteComboBox.setEditable(False)
        self.fabricanteComboBox.setObjectName(_fromUtf8("fabricanteComboBox"))
        self.centralLayout.addWidget(self.fabricanteComboBox, 1, 1, 1, 1)
        self.midiaComboBox = QtGui.QComboBox(self.centralwidget)
        self.midiaComboBox.setObjectName(_fromUtf8("midiaComboBox"))
        self.centralLayout.addWidget(self.midiaComboBox, 2, 1, 1, 1)
        self.fabricanteLabel = QtGui.QLabel(self.centralwidget)
        self.fabricanteLabel.setObjectName(_fromUtf8("fabricanteLabel"))
        self.centralLayout.addWidget(self.fabricanteLabel, 1, 0, 1, 1)
        self.buttonLayout = QtGui.QHBoxLayout()
        self.buttonLayout.setObjectName(_fromUtf8("buttonLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.buttonLayout.addItem(spacerItem)
        self.searchButton = QtGui.QPushButton(self.centralwidget)
        self.searchButton.setObjectName(_fromUtf8("searchButton"))
        self.buttonLayout.addWidget(self.searchButton)
        self.centralLayout.addLayout(self.buttonLayout, 4, 1, 1, 1)
        self.verticalLayout.addLayout(self.centralLayout)
        self.resultsTableView = QtGui.QTableView(self.centralwidget)
        self.resultsTableView.setObjectName(_fromUtf8("resultsTableView"))
        self.verticalLayout.addWidget(self.resultsTableView)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 391, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMenu = QtGui.QMenu(self.menubar)
        self.menuMenu.setObjectName(_fromUtf8("menuMenu"))
        self.menuInserir = QtGui.QMenu(self.menubar)
        self.menuInserir.setObjectName(_fromUtf8("menuInserir"))
        self.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(self)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        self.setStatusBar(self.statusbar)
        self.actionSobre = QtGui.QAction(self)
        self.actionSobre.setObjectName(_fromUtf8("actionSobre"))
        self.actionSair = QtGui.QAction(self)
        self.actionSair.setObjectName(_fromUtf8("actionSair"))
        self.menuMenu.addAction(self.actionSobre)
        self.menuMenu.addAction(self.actionSair)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuInserir.menuAction())

        self.retranslateUi(self)
        QtCore.QObject.connect(self.searchButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.update_table)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.centralTitleLabel.setText(_translate("MainWindow", "Procurar por Jogos", None))
        self.nameLabel.setText(_translate("MainWindow", "Nome", None))
        self.midiaLabel.setText(_translate("MainWindow", "Mídia", None))
        self.consoleLabel.setText(_translate("MainWindow", "Console", None))
        self.fabricanteLabel.setText(_translate("MainWindow", "Fabricante", None))
        self.searchButton.setText(_translate("MainWindow", "Procurar", None))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu", None))
        self.menuInserir.setTitle(_translate("MainWindow", "Inserir", None))
        self.actionSobre.setText(_translate("MainWindow", "Sobre", None))
        self.actionSair.setText(_translate("MainWindow", "Sair", None))

    def update_table(self):
        if len(self.nameLineEdit.text()) == 0:
            print "Um nome deve ser especificado"
        else:
            dicionario = {}
            dicionario['nome'] = self.nameLineEdit.text()
            dicionario['fabricante'] = self.fabricanteComboBox.currentText()
            dicionario['midia'] = self.midiaComboBox.currentText()
            dicionario['console'] = self.consoleComboBox.currentText()
            self.controller.buscar(dicionario)
        

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

