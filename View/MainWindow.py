# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created: Tue Jun 25 18:17:26 2013
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
    def __init__(self,controller):
        Qt.QMainWindow.__init__(self)
        
        self.controller = controller
        
        self.setObjectName(_fromUtf8("MainWindow"))
        self.resize(391, 569)
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
        self.resultToolBox = QtGui.QToolBox(self.centralwidget)
        self.resultToolBox.setObjectName(_fromUtf8("resultToolBox"))
        self.nomesPage = QtGui.QWidget()
        self.nomesPage.setGeometry(QtCore.QRect(0, 0, 373, 233))
        self.nomesPage.setObjectName(_fromUtf8("nomesPage"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.nomesPage)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.nomesTableView = QtGui.QTableView(self.nomesPage)
        self.nomesTableView.setObjectName(_fromUtf8("nomesTableView"))
        self.verticalLayout_2.addWidget(self.nomesTableView)
        self.resultToolBox.addItem(self.nomesPage, _fromUtf8(""))
        self.fabricantesPage = QtGui.QWidget()
        self.fabricantesPage.setGeometry(QtCore.QRect(0, 0, 373, 233))
        self.fabricantesPage.setObjectName(_fromUtf8("fabricantesPage"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.fabricantesPage)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.fabricantesTableView = QtGui.QTableView(self.fabricantesPage)
        self.fabricantesTableView.setObjectName(_fromUtf8("fabricantesTableView"))
        self.verticalLayout_3.addWidget(self.fabricantesTableView)
        self.resultToolBox.addItem(self.fabricantesPage, _fromUtf8(""))
        self.mdiasPage = QtGui.QWidget()
        self.mdiasPage.setObjectName(_fromUtf8("mdiasPage"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.mdiasPage)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.midiasTableView = QtGui.QTableView(self.mdiasPage)
        self.midiasTableView.setObjectName(_fromUtf8("midiasTableView"))
        self.verticalLayout_4.addWidget(self.midiasTableView)
        self.resultToolBox.addItem(self.mdiasPage, _fromUtf8(""))
        self.consolesPage = QtGui.QWidget()
        self.consolesPage.setObjectName(_fromUtf8("consolesPage"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.consolesPage)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.consolesTableView = QtGui.QTableView(self.consolesPage)
        self.consolesTableView.setObjectName(_fromUtf8("consolesTableView"))
        self.verticalLayout_5.addWidget(self.consolesTableView)
        self.resultToolBox.addItem(self.consolesPage, _fromUtf8(""))
        self.verticalLayout.addWidget(self.resultToolBox)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 391, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMenu = QtGui.QMenu(self.menubar)
        self.menuMenu.setObjectName(_fromUtf8("menuMenu"))
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

        self.retranslateUi(self)
        self.resultToolBox.setCurrentIndex(3)
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
        self.resultToolBox.setItemText(self.resultToolBox.indexOf(self.nomesPage), _translate("MainWindow", "Nome", None))
        self.resultToolBox.setItemText(self.resultToolBox.indexOf(self.fabricantesPage), _translate("MainWindow", "Fabricantes", None))
        self.resultToolBox.setItemText(self.resultToolBox.indexOf(self.mdiasPage), _translate("MainWindow", "Mídia", None))
        self.resultToolBox.setItemText(self.resultToolBox.indexOf(self.consolesPage), _translate("MainWindow", "Consoles", None))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu", None))
        self.actionSobre.setText(_translate("MainWindow", "Sobre", None))
        self.actionSair.setText(_translate("MainWindow", "Sair", None))
        
    
    def update_table(self):
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

