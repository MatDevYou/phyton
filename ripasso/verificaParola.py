import yaml
import os

if os.path.exists("config.yaml"):
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)
    if "nome" in config:
        print(f"nome: {config['nome']}")
    else:
        print("chiave 'nome' non trovata nel file YAML")