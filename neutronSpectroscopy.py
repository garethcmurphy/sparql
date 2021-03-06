#!/usr/bin/env python3
""" Query using graph.query """

import rdflib


def main():
    """ main"""
    graph = rdflib.Graph()
    graph.load("ess.rdf")
    pankos_url = "https://raw.githubusercontent.com/ral-facilities/pankos/master/PanKOS/Version_1.0/pankos.rdf"
    # graph.load(pankos_url)

    qres = graph.query(
        """
           SELECT DISTINCT ?subject ?predicate ?object
           WHERE {
                ?subject ?inFacility pankos:ESS ;
                         ?supportsTechnique pankos:NeutronReflectometry .
           }
           ORDER BY ?subject
           """)
    i = 0
    for row in qres:
        i = i + 1
        # .split('#')[-1])
        print(i, row.subject.split('#')[-1])
        #print(i, row)


if __name__ == "__main__":
    main()
