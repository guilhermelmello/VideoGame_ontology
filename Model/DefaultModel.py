#! coding: utf-8

import rdflib

class Default_Model():
	def __init__(self):
		rdflib.plugin.register('sparql', rdflib.query.Processor, 'rdfextras.sparql.processor', 'Processor')
		rdflib.plugin.register('sparql', rdflib.query.Result, 'rdfextras.sparql.query', 'SPARQLQueryResult')
		
		self.graph = rdflib.Graph()
		self.graph.load("ontologia.rdf")
		self.prefix = "PREFIX a:<http://ontokem.egc.ufsc.br/ontologia#>"
	
	# retorna todos os fabricantes
	def select_fabricantes(self):
		q = self.graph.query(self.prefix +
			           ("""SELECT DISTINCT ?f
						   WHERE {
						       ?f rdf:type a:Fabricantes.
						   }"""))
		return self.retorno_lista(q)
	
	#retorna todas as midias
	def select_midias(self):
		q = self.graph.query(self.prefix +
			           ("""SELECT DISTINCT ?nome
						   WHERE {
						       ?m rdf:type a:Midias.
						       ?m a:nome ?nome.
						   }"""))
		return self.retorno_lista(q)
	
	# retorna todos os consoles
	def select_consoles(self):
		q = self.graph.query(self.prefix +
			           ("""SELECT DISTINCT ?nome
						   WHERE {
						       ?c rdf:type a:Consoles.
						       ?c a:nome ?nome.
						   }"""))
		return self.retorno_lista(q)
	
	
	# retorna as propriedades encontradas em uma instância de jogo
	def select_propriedades_jogo(self,nome):
		pass
		#q = self.graph.query(self.prefix +
			           #("""SELECT DISTINCT ?j
						   #WHERE {
						       #?j rdf:type a:Jogos.
						   #}"""))
		#return self.retorno_lista(q)
	
	# retorna os jogosd de um console
	def select_jogos_console(self,nome):
		q = self.graph.query(self.prefix +
			           ("""SELECT DISTINCT ?j
						   WHERE {
						       ?c rdf:type a:Consoles.
						       ?j rdf:type a:Jogos.
						       ?c a:nome %s }"""%(nome)))
		return self.retorno_lista(q)
	
	def test_select(self):
		#q = self.graph.query(self.prefix +
		#("""SELECT DISTINCT ?ano
			#WHERE {
				#?c a:nome ?nome.
				#?c a:ano ?ano.
				#FILTER(?nome == "PSOne")
			#}"""))
		s = "PSOne"
		q = self.graph.query(self.prefix +
						("""SELECT DISTINCT ?ano WHERE { 
								?c a:nome ?nome
								?c rdf:type a:Consoles
								?c a:ano ?ano
								FILTER(?nome == 'PSOne')
							}"""))
		for r in q.result:
			print r
		#return self.retorno(q)
	
	def retorno_lista(self,query):
		result = []
		for r in query.result:
			print r
			result.append(r.split('#')[1])
		return result
	
	
	def retorno(self,query):
		result = []
		for i, row in enumerate(query.result):
			result.append([])
			print row
			for item in row:
				result[i].append(item.split('#')[1])
		return result


if __name__ == "__main__":
	dm = Default_Model()
	r = dm.test_select()
	#print r,"\n\n"
	#for l in r:
		#s = ''
		#for c in l:
			#s += '\t'+c
		#print s




# 1 = 
# 2 = how old are you
# 3 = how fast can you type
# 4 = how tall are you
# 5 = how carefully do you write
# 6 = how hard was this exercise