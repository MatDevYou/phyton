def segreteria(studenti):
    for studente in studenti:
        media_voti = sum(studente["voti"]) / float(len(studente["voti"]))
        studente["media"] = media_voti
    return studenti

studenti = [
    {"nome": "Mario", "cognome": "Rossi", "classe": "3A", "voti": [6, 10, 8]},
    {"nome": "Luigi", "cognome": "Bianchi", "classe": "3A", "voti": [7, 8, 9]},
    {"nome": "Anna", "cognome": "Verdi", "classe": "3B", "voti": [8, 9, 10]}
]

registro_segreteria = segreteria(studenti)

for studente in registro_segreteria:
    print(studente)
