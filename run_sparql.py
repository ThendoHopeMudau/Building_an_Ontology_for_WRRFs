from rdflib import Graph

g = Graph()
g.parse("WRRFs_Ontology2.owl", format="turtle")

print(f"\nOntology loaded successfully with {len(g)} triples.\n")

query = """
PREFIX : <http://www.semanticweb.org/hope/ontologies/2026/3/WRRFs_Ontology2#>

SELECT DISTINCT ?microorganism ?nitrateSpecies ?oxygenNiche
WHERE {
    ?microorganism :reduces ?nitrateSpecies ;
                   :hasOxygenNiche ?oxygenNiche .

    FILTER(?nitrateSpecies IN (:Nitrate, :Nitrite))
    FILTER(?oxygenNiche = :Anaerobic)
}
ORDER BY ?microorganism ?nitrateSpecies
"""

results = g.query(query)

print("------------------------------------------------------------------------------------------------")
print(f"{'Microorganism':40} {'Nitrate Species Reduced':25} {'Oxygen Niche'}")
print("------------------------------------------------------------------------------------------------")

for row in results:
    microorganism = str(row.microorganism).split("#")[-1]
    nitrate_species = str(row.nitrateSpecies).split("#")[-1]
    oxygen_niche = str(row.oxygenNiche).split("#")[-1]

    print(f"{microorganism:40} {nitrate_species:25} {oxygen_niche}")

print("------------------------------------------------------------------------------------------------")
