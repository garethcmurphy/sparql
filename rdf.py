#!/usr/bin/env python3
import rdflib

g = rdflib.Graph()

# ... add some triples to g somehow ...
g.parse("card.rdf")

qres = g.query(
    """SELECT DISTINCT ?aname ?bname
       WHERE {
          ?a foaf:knows ?b .
          ?a foaf:name ?aname .
          ?b foaf:name ?bname .
       }""")

for row in qres:
    print("%s knows %s" % row)
