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
           SELECT ?subject
           WHERE {
                ?subject  ?supportsTechnique  pankos:NeutronDiffraction;
                          ?inFacility pankos:ESS .
           }""")
    i = 0
    for row in qres:
        i = i + 1
        # .split('#')[-1])
        print(i, row.subject.split('#')[-1])


if __name__ == "__main__":
    main()
