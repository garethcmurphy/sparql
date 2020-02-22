#!/usr/bin/env python3
from SPARQLWrapper import SPARQLWrapper, N3
from rdflib import Graph

sparql = SPARQLWrapper("http://dbpedia.org/sparql")
sparql.setQuery("""
    DESCRIBE <http://dbpedia.org/resource/Asturias>
""")

sparql.setReturnFormat(N3)
results = sparql.query().convert()
g = Graph()
g.parse(data=results, format="n3")
print(g.serialize(format='n3'))