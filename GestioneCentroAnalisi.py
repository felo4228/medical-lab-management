"""
Progetto 2 – Gestione centro analisi mediche
Python + OOP + NumPy
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import List, Dict
import numpy as np



nome1 = "Mario"
cognome1 = "Rossi"
codice_fiscale1 = "MRARSS80A01H501U"
eta1 = 45
peso1 = 78.5
analisi1 = ["emocromo", "glicemia", "colesterolo"]

nome2 = "Lucia"
cognome2 = "Bianchi"
codice_fiscale2 = "LCABNC90B41H501X"
eta2 = 33
peso2 = 62.0
analisi2 = ["glicemia", "trigliceridi", "colesterolo"]

nome3 = "Paolo"
cognome3 = "Verdi"
codice_fiscale3 = "PLVRDI75C15H501Z"
eta3 = 50
peso3 = 85.2
analisi3 = ["emocromo", "pressione", "colesterolo"]




@dataclass
class Analisi:
    """
    Rappresenta una singola analisi di laboratorio.
    """
    tipo: str          
    valore: float      

    def valuta(self) -> str:
        """
        Stabilisce se il valore è nella norma.
        I range sono inventati a scopo didattico.
        """
        range_normali: Dict[str, tuple[float, float]] = {
            "glicemia": (70, 110),
            "colesterolo": (120, 200),
            "trigliceridi": (50, 150),
            "emocromo": (4.0, 6.0),        
            "pressione": (90, 140),        
        }

        if self.tipo not in range_normali:
            return f"Nessun intervallo definito per {self.tipo}"

        minimo, massimo = range_normali[self.tipo]
        if minimo <= self.valore <= massimo:
            return f"{self.tipo}: {self.valore} (nella norma)"
        else:
            return f"{self.tipo}: {self.valore} (FUORI norma!)"


@dataclass
class Paziente:
    """
    Rappresenta un paziente del centro analisi.
    """
    nome: str
    cognome: str
    codice_fiscale: str
    eta: int
    peso: float
    analisi_effettuate: List[Analisi]

   
    def __post_init__(self) -> None:
        """
        Dopo l'inizializzazione, creiamo un array NumPy con i valori numerici
        delle analisi svolte.
        """
        self.risultati_analisi: np.ndarray = np.array(
            [a.valore for a in self.analisi_effettuate],
            dtype=float
        )

    def scheda_personale(self) -> str:
        """
        Restituisce una stringa con i dati principali del paziente.
        """
        return (
            f"Paziente: {self.nome} {self.cognome}\n"
            f"Codice fiscale: {self.codice_fiscale}\n"
            f"Età: {self.eta} anni – Peso: {self.peso} kg\n"
        )

    def statistiche_analisi(self) -> Dict[str, float]:
        """
        Calcola statistiche sui risultati delle analisi usando NumPy:
        - media
        - valore minimo
        - valore massimo
        - deviazione standard
        """
        if self.risultati_analisi.size == 0:
            return {
                "media": float("nan"),
                "minimo": float("nan"),
                "massimo": float("nan"),
                "deviazione_std": float("nan"),
            }

        media = float(self.risultati_analisi.mean())
        minimo = float(self.risultati_analisi.min())
        massimo = float(self.risultati_analisi.max())
        dev_std = float(self.risultati_analisi.std())

        return {
            "media": media,
            "minimo": minimo,
            "massimo": massimo,
            "deviazione_std": dev_std,
        }


@dataclass
class Medico:
    """
    Rappresenta un medico del centro.
    """
    nome: str
    cognome: str
    specializzazione: str

    def visita_paziente(self, paziente: Paziente) -> None:
        """
        Stampa quale medico sta visitando quale paziente.
        """
        print(
            f"Il dott. {self.nome} {self.cognome} "
            f"({self.specializzazione}) sta visitando "
            f"{paziente.nome} {paziente.cognome}."
        )



def esempio_numpy_esame_unico() -> None:
    """
    Esempio: il centro raccoglie i risultati di un certo esame per 10 pazienti.
    Rappresentiamo i valori in un array NumPy e calcoliamo:
    - media
    - massimo
    - minimo
    - deviazione standard
    """
    
    risultati = np.array([88, 92, 110, 76, 101, 95, 120, 85, 99, 105], dtype=float)
    print("=== Parte 3 – Esempio NumPy con 10 pazienti ===")
    print("Risultati esame (glicemia):", risultati)
    print("Media:", np.mean(risultati))
    print("Massimo:", np.max(risultati))
    print("Minimo:", np.min(risultati))
    print("Deviazione standard:", np.std(risultati))
    print()




def main() -> None:
   
    esempio_numpy_esame_unico()

   
    medici: List[Medico] = [
        Medico("Giulia", "Ferrari", "Cardiologia"),
        Medico("Luca", "Conti", "Endocrinologia"),
        Medico("Sara", "Neri", "Medicina generale"),
    ]

    
    pazienti: List[Paziente] = [
        Paziente(
            nome="Mario",
            cognome="Rossi",
            codice_fiscale="MRARSS80A01H501U",
            eta=45,
            peso=78.5,
            analisi_effettuate=[
                Analisi("glicemia", 95),
                Analisi("colesterolo", 210),
                Analisi("pressione", 135),
            ],
        ),
        Paziente(
            nome="Lucia",
            cognome="Bianchi",
            codice_fiscale="LCABNC90B41H501X",
            eta=33,
            peso=62.0,
            analisi_effettuate=[
                Analisi("glicemia", 82),
                Analisi("trigliceridi", 140),
                Analisi("colesterolo", 180),
            ],
        ),
        Paziente(
            nome="Paolo",
            cognome="Verdi",
            codice_fiscale="PLVRDI75C15H501Z",
            eta=50,
            peso=85.2,
            analisi_effettuate=[
                Analisi("emocromo", 4.8),
                Analisi("glicemia", 115),
                Analisi("colesterolo", 190),
            ],
        ),
        Paziente(
            nome="Anna",
            cognome="Russo",
            codice_fiscale="NNARSS88D20H501Y",
            eta=40,
            peso=70.0,
            analisi_effettuate=[
                Analisi("glicemia", 105),
                Analisi("pressione", 145),
                Analisi("colesterolo", 175),
            ],
        ),
        Paziente(
            nome="Diego",
            cognome="Costa",
            codice_fiscale="DGOCST95E11H501Q",
            eta=29,
            peso=80.3,
            analisi_effettuate=[
                Analisi("glicemia", 90),
                Analisi("trigliceridi", 160),
                Analisi("emocromo", 5.2),
            ],
        ),
    ]

   
    print("=== Parte 5 – Applicazione completa ===\n")

    for i, paziente in enumerate(pazienti):
        medico = medici[i % len(medici)]

        
        print(paziente.scheda_personale())

        
        medico.visita_paziente(paziente)
        print()

        
        print("Analisi effettuate:")
        for a in paziente.analisi_effettuate:
            print(" -", a.valuta())
        print()

        stats = paziente.statistiche_analisi()
        print("Statistiche sulle analisi (valori numerici):")
        print(f"  Media: {stats['media']:.2f}")
        print(f"  Minimo: {stats['minimo']:.2f}")
        print(f"  Massimo: {stats['massimo']:.2f}")
        print(f"  Deviazione standard: {stats['deviazione_std']:.2f}")
        print("\n" + "-" * 50 + "\n")


if __name__ == "__main__":
    main()
