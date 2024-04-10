class Macchina:
  def __init__(self, marca, modello, cilindrata, carburante, colore):
    self.marca = marca
    self.modello = modello
    self.cilindrata = cilindrata
    self.carburante = carburante
    self.colore = colore
    self.velocita = 50

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

  def accelera(self):
    if self.velocita >= self.calcola_velocita_massima():
      print("Velocità massima raggiunta.")
    elif self.velocita >= 140:
      print("Hai superato la velocità massima consentita. Rallenta!")
      self.velocita += 10
    else:
      self.velocita += 10

  def frena(self):
    if self.velocita < 0:
      self.velocita = 0
    else:
      self.velocita -= 5

  def stampa_blocco(self):
    self.stampa_macchina("\n")
    print("velocita massiam:", self.calcola_velocita_massima())
    print("\nvelocita attuale: ", self.velocita)

def main():
  menu = 0
  a1 = Macchina("Mercedes", "AMG", 1700, "Benzina", "Nera Opaca")

  while menu != 9:
    print("\nScegli un'azione:")
    print("1 - Accelera")
    print("2 - Frena")
    print("9 - Chiudi Programma")
    menu = int(input())

    if menu == 1:
      a1.accelera()
    elif menu == 2:
      a1.frena()
    elif menu == 9:
      print("Programma terminato.")
    else:
      print("Scelta non valida.")

    a1.stampa_blocco()
    


if __name__ == "__main__":
  main()
