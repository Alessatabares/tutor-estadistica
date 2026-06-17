"""Metadatos compartidos para los decks de Estadistica (Probabilidad / Descriptiva / Inferencial).

Replica la metodologia de los ejes diagnosticos de examen-ecoe-anki:
cada AREA genera DOS decks con la misma logica que los ejes ECOE:
  - Eje Clinico  (del PROBLEMA al concepto que lo resuelve)
  - Integrador   (de las SENALES al concepto + tip verbalizable)

Cada _parts/<slug>.py define: NAME (str), EJES (list), ESTACIONES (list).

Esquema de deck_id: 1600_AA_C
  AA = indice del area (01-03)
  C  = 1 (Eje Clinico) | 2 (Integrador)
Rango valido [1<<30, 1<<31); sin colision con examen-ecoe-anki (12xx/13xx)
ni con python-learning/basicos (15xx).
"""

MODEL_QA_ID = 1607392322  # qa_estadistica (propio de este repo)
PADRE = "Estadistica"

# (nombre_en_data, nombre_corto_para_deck, slug_archivo, tag, idx)
AREAS = [
    ("Probabilidad",             "Probabilidad",  "Probabilidad",  "probabilidad",  1),
    ("Estadistica Descriptiva",  "Descriptiva",   "Descriptiva",   "descriptiva",   2),
    ("Estadistica Inferencial",  "Inferencial",   "Inferencial",   "inferencial",   3),
]


def deck_id(idx, fmt):
    """fmt: 1 = Eje Clinico, 2 = Integrador."""
    return 1600000000 + idx * 1000 + fmt
