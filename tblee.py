#!/usr/bin/env python3
from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("http://www.w3.org/People/Berners-Lee/card")
sparql.setQuery("""
PREFIX foaf:  <http://xmlns.com/foaf/0.1/>
SELECT ?name
WHERE {
    ?person foaf:name ?name .
}
""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()
print ( results)
#for result in results["results"]["bindings"]:
#    print(result["label"]["value"])
