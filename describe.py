#!/usr/bin/env python3
"""test query"""
from SPARQLWrapper import SPARQLWrapper, N3
from rdflib import Graph


def main():
    """main"""
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setQuery("""
        DESCRIBE <http://dbpedia.org/resource/Asturias>
    """)

    sparql.setReturnFormat(N3)
    results = sparql.query().convert()
    g = Graph()
    g.parse(data=results, format="n3")
    print(g.serialize(format='n3'))


if __name__ == "__main__":
    main()
