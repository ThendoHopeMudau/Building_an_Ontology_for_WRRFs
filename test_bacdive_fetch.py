import bacdive
import pandas as pd

client = bacdive.BacdiveClient()

metabolites = set()

metabolite_fields = [
    "metabolite_util",
    "metabolite_prod",
    "metabolite_test",
    "metabolite_antib"
]


def extract_metabolites(obj):
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key in metabolite_fields:
                if isinstance(value, list):
                    for item in value:
                        metabolites.add(str(item).strip())
                else:
                    metabolites.add(str(value).strip())

            extract_metabolites(value)

    elif isinstance(obj, list):
        for item in obj:
            extract_metabolites(item)


# Broad search through BacDive
client.search(taxonomy="Bacteria", search_type="contains")

for strain in client.retrieve():
    extract_metabolites(strain)


df = pd.DataFrame(sorted(metabolites), columns=["Metabolite"])

df.to_excel("bacdive_metabolites_only.xlsx", index=False)

print("Done.")
print(f"Saved {len(df)} unique metabolites.")
print("Excel file created: bacdive_metabolites_only.xlsx")