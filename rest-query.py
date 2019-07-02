import requests, sys

server = "https://rest.ensembl.org"
ext = "/vep/human/id/COSM476?"

r = requests.get(server+ext, headers={ "Content-Type" : "application/json"})

if not r.ok:
  r.raise_for_status()
  sys.exit()

decoded = r.json()
print(repr(decoded))p_id_get('homo sapiens', 'TP53')
