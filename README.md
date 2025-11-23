 Medical Lab Management – Python, OOP & NumPy

This project is a small console-based application that simulates the workflow of a medical analysis center.  
It was built as a practical exercise for learning:

- Python fundamentals
- Object-Oriented Programming (OOP)
- Basic numerical analysis with NumPy
- Integration between OOP and numerical computation

---

 Project overview

A medical analysis center needs to partially digitalize the management of patients, doctors and lab test results.

The project is organized in 5 parts:

 1. Variables & Data Types

- Define basic variables to represent:
  - Patient first name, last name and tax code (strings)
  - Age and weight (integers and floats)
  - List of performed analyses (list of strings)
- Example patients are defined (at least three), just using simple variables.

 2. Classes & OOP

Three main classes are implemented:

 `Analisi`
Represents a single lab test.

- Attributes:
  - `tipo` (type of analysis, e.g. "glicemia", "colesterolo")
  - `valore` (numeric result)
- Method:
  - `valuta()` → returns a string indicating whether the value is in a normal range  
    (the ranges are invented for educational purposes).

 `Paziente`
Represents a patient of the medical center.

- Attributes:
  - `nome`, `cognome`, `codice_fiscale`
  - `eta`, `peso`
  - `analisi_effettuate` (list of `Analisi` objects)
  - `risultati_analisi` (NumPy array with numeric values of the analyses)
- Methods:
  - `scheda_personale()` → returns a formatted string with patient details
  - `statistiche_analisi()` → uses NumPy to compute:
    - mean
    - minimum
    - maximum
    - standard deviation of the analysis results

 `Medico`
Represents a doctor.

- Attributes:
  - `nome`, `cognome`, `specializzazione`
- Methods:
  - `visita_paziente(paziente)` → prints which doctor is visiting which patient.

---

 3. NumPy Usage (standalone example)

The function `esempio_numpy_esame_unico()` simulates collecting the results of one exam (e.g., blood glucose) for 10 patients.  
It stores the values in a NumPy array and prints:

- mean
- minimum
- maximum
- standard deviation

---

 4. OOP + NumPy Integration

The `Paziente` class integrates NumPy by storing analysis results in a NumPy array (`risultati_analisi`) and providing the method `statistiche_analisi()` to compute statistics using NumPy operations.

---

 5. Main Application

The `main()` function:

1. Calls the standalone NumPy example.
2. Creates at least 3 doctors and 5 patients.
3. Each patient has at least 3 analysis results.
4. Prints the personal sheet of each patient.
5. Shows which doctor is visiting which patient.
6. Prints the evaluation of each analysis (normal / out of range).
7. Prints the statistics (mean, min, max, std dev) for each patient using NumPy.

---

How to run

1. Make sure you have **Python 3.10+** installed.
2. Install NumPy if needed.

 
