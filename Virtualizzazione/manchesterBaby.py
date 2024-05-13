class Simulatore:
    def __init__(self):
        self.registri = [0, 0]  # Inizializzazione dei registri
        self.indiceIstruzione = 0  # Indice dell'istruzione corrente

    def eseguiIstruzione(self, istruzione):
        comando, argomento = self.decodeInstruction(istruzione)
        if comando == "LDN":
            self.registri[0] = int(argomento)
        elif comando == "CMP":
            if self.registri[0] == self.registri[1]:
                self.registri[0] = 0
            elif self.registri[0] < self.registri[1]:
                self.registri[0] = -1
            else:
                self.registri[0] = 1
        elif comando == "STO":
            self.registri[1] = self.registri[0]
        elif comando == "STP":
            print("Fine del programma")
            return False  # Segnala la fine del programma
        print("Registri:", self.registri)  # Stampa lo stato dei registri dopo ogni istruzione
        return True

    def decodeInstruction(self, istruzione):
        comando = istruzione[9:12]
        argomento = istruzione[12:]
        return comando, argomento

    def eseguiProgramma(self, programma):
        while self.indiceIstruzione < len(programma):
            istruzione = programma[self.indiceIstruzione]
            continua = self.eseguiIstruzione(istruzione)
            if not continua:
                break
            self.indiceIstruzione += 1


# Programma di esempio
programma = [
    "00000000000000000000000000000000",
    "00101000000000100000000000000000",  # LDN 20
    "00000000000000110000000000000000",  # CMP
    "00101000000001100000000000000000",  # STO 20
    "00000000000001110000000000000000",  # STP
    # Altre istruzioni...
]

simulatore = Simulatore()
simulatore.eseguiProgramma(programma)
