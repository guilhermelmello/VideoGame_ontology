#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys

def main(args):
	import Bootstrap as app
	global app
	app = app.Bootstrap(args)
	app.exec_()

if __name__ == "__main__":
	main(sys.argv)














#import mainWindow, sys
#from PyQt4 import *

#if __name__ == "__main__":
    #app = QtGui.QApplication(sys.argv)
    #MainWindow = QtGui.QMainWindow()
    #ui = mainWindow.Ui_MainWindow()
    #ui.setupUi(MainWindow)
    #MainWindow.show()
    
    ##Insert = QtGui.QWidget()
    ##ins = inserir.Ui_Form()
    ##ins.setupUi(Insert)
    ##Insert.show()	
    
    #sys.exit(app.exec_())
    
    #------------------------------------#
	
	#import rdflib
	
	#rdflib.plugin.register('sparql', rdflib.query.Processor, 'rdfextras.sparql.processor', 'Processor')
	#rdflib.plugin.register('sparql', rdflib.query.Result, 'rdfextras.sparql.query', 'SPARQLQueryResult')
	
	#graph = rdflib.Graph()
	
	#graph.load("ontologia.rdf")
	
	#q = graph.query("""PREFIX a:<http://ontokem.egc.ufsc.br/ontologia#>
							  #SELECT DISTINCT ?f ?c
							  #WHERE {
								  #?f rdf:type a:Fabricantes.
								  #?c rdf:type a:Consoles.
								  #?c a:ehDeFabricantes ?f
							  #}""")
	
	#for row in q.result:
		#s = ''
		#for item in row:
			#s += item.split('#')[1] + " "
		#print s







