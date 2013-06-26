#! coding: utf-8

from PyQt4 import *
from Model.DefaultModel import *
from Model.ListModel import *
from Model.TableModel import *

#import Models.TableModel as c
#import Models.DefaultModel as db

class MainController():
	def __init__(self):		
		import View.MainWindow as mainWindow
		data = None
		self.main = mainWindow.Ui_MainWindow(self)
		
		self.startData()
		self.main.show()
		
		
	def startData(self):
		dm = Default_Model()
		
		fab_model = List_Model(dm.select_fabricantes())
		mid_model = List_Model(dm.select_midias())
		con_model = List_Model(dm.select_consoles())
		
		self.main.fabricanteComboBox.setModel(fab_model)
		self.main.midiaComboBox.setModel(mid_model)
		self.main.consoleComboBox.setModel(con_model)
		
	def buscar(self,dados):
		print "===| Buscar Jogo |==="
		print "Nome:",dados['nome']
		print "Fabricante:",dados['fabricante']
		print "Mídia:",dados['midia']
		print "Console:",dados['console']
		
		dm = Default_Model()
		
		jogos_list = dm.select_propriedades_jogo(dados['nome'])
		self.main.nomesTableView.setModel(table_model)
		self.update_table(resultados)
		
		
	
	def update_table(self,table,dados):
		dados = [[1],[2],[3],[4],[5],[6]]
		headers = ['um']
		table_model = TableModel(dados,headers)
		table.setModel(table_model)
		