import json

with open("/Applications/phyton/ripasso/dati.json", "r") as f:
    data = json.load(f)
print(f"nome: {data['nome']}")