#!/usr/bin/env python3

"""
Query using graph.query
Result is iterable over the result rows
result.vars contains the variables
or result.bindings is a list of dicts of variables bindings
"""

import rdflib


def main():
    """ main"""
    graph = rdflib.Graph()
    graph.load("ess.rdf")

    qres = graph.query(
        """PREFIX supportsTechnique: <http://www.purl.org/pankos#supportsTechnique>
           PREFIX NeutronDiffraction: <http://www.purl.org/pankos#NeutronDiffraction>
           SELECT ?subject ?predicate ?object
           WHERE {
                ?subject  <http://www.purl.org/pankos#supportsTechnique> ?NeutronDiffraction .
           }""")
    for row in qres:
        print(row.subject.split('#')[-1], "supports Technique", row.object)# .split('#')[-1])


if __name__ == "__main__":
    main()
