#!/usr/bin/env python3
"""test"""
from SPARQLWrapper import SPARQLWrapper, JSON


def main():
    """test"""
    sparql = SPARQLWrapper("https://protege.stanford.edu/ontologies/pizza/pizza.owl")
    sparql.setQuery("""
    PREFIX pizza: <https://protege.stanford.edu/ontologies/pizza/pizza.owl>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
SELECT ?pizza
WHERE {
?pizza rdfs:subClassOf pz:NamedPizza .
}
    """)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    print(results)
    # for result in results["results"]["bindings"]:
    #    print(result["label"]["value"])


if __name__ == "__main__":
    main()
