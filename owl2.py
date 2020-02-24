#!/usr/bin/env python3
"""query africa"""
import requests


def main():
    """test query"""
    url = 'https://protege.stanford.edu/ontologies/pizza/pizza.owl'
    query = """
        PREFIX pizza: <https://protege.stanford.edu/ontologies/pizza/pizza.owl>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
SELECT ?pizza
WHERE {
?pizza rdfs:subClassOf pz:NamedPizza .
}
    """
    response = requests.get(url, params={'format': 'json', 'query': query})
    data = response.json()
    print(data)


if __name__ == "__main__":
    main()
