class Macchina:
  def __init__(self, marca, modello, cilindrata, carburante, colore):
    self.marca = marca
    self.modello = modello
    self.cilindrata = cilindrata
    self.carburante = carburante
    self.colore = colore

  def calcola_velocita_massima(self):
    bonus = 0
    if self.carburante == "Benzina":
      bonus += 30
    elif self.carburante == "Diesel":
      bonus += 20
    elif self.carburante == "GPL":
      bonus -= 10
    elif self.carburante == "Metano":
      bonus -= 30

    return (self.cilindrata / 10) + bonus

  def stampa_macchina(self, separatore):
    print(f"\nMarca: {self.marca}{separatore}")
    print(f"Modello: {self.modello}{separatore}")
    print(f"Cilindrata: {self.cilindrata}{separatore}")
    print(f"Carburante: {self.carburante}{separatore}")
    print(f"Colore: {self.colore}{separatore}")


def main():
  a1 = Macchina("Mercedes", "AMG", 250, "Benzina", "Nera Opaca")
  a2 = Macchina("Audi", "A3", 2500, "Diesel", "Verde")
  a3 = Macchina("Fiat", "Punto", 130, "GPL", "Grigia Spilberga")
  a4 = Macchina("Ferrari", "PuroSangue", 700, "Metano", "Rosso Sangue")

  a1.stampa_macchina("\n")
  print(f"Velocita massima: {a1.calcola_velocita_massima()} km/h\n")

  a2.stampa_macchina("\n")
  print(f"Velocita massima: {a2.calcola_velocita_massima()} km/h\n")

  a3.stampa_macchina("\n")
  print(f"Velocita massima: {a3.calcola_velocita_massima()} km/h\n")

  a4.stampa_macchina("\n")
  print(f"Velocita massima: {a4.calcola_velocita_massima()} km/h\n")


if __name__ == "__main__":
  main()
