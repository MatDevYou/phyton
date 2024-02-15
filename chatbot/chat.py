# Importiamo la libreria per l'analisi del linguaggio naturale
import nltk

# Definiamo le frasi di saluto
saluti = ["Ciao", "Buongiorno", "Buonasera"]

# Definiamo le frasi di congedo
congedi = ["Arrivederci", "A presto", "Ciao ciao"]

# Funzione per la risposta del chatbot
def chatbot(domanda):
  # Preprocessiamo la domanda
  domanda = domanda.lower()
  domanda = nltk.word_tokenize(domanda)

  # Controlliamo se la domanda è un saluto
  if any(saluto in domanda for saluto in saluti):
    return "Piacere di conoscerti!"

  # Controlliamo se la domanda è un congedo
  if any(congedo in domanda for congedo in congedi):
    return "Grazie per aver chattato con me!"

  # Risposta generica
  return "Non sono sicuro di cosa intendi. Puoi riformulare la tua domanda?"

# Ciclo principale
while True:
  # Chiediamo all'utente una domanda
  domanda = input("Cosa vuoi chiedere? ")

  # Generiamo la risposta del chatbot
  risposta = chatbot(domanda)

  # Stampo la risposta
  print(risposta)
