# -*- coding: utf-8 -*-
NAME = "Estadistica Descriptiva"

# EJE CLINICO: del PROBLEMA al concepto.
EJES = [
  ("Tengo un montón de datos, ¿cómo los resumo en pocos números?", [
    ("El valor central típico (suma / n)",
     "Media"),
    ("El valor de en medio, robusto a extremos",
     "Mediana"),
    ("El valor más frecuente",
     "Moda"),
    ("Cuánto se dispersan los datos alrededor de la media",
     "Desviación estándar / varianza"),
    ("El rango entre el cuartil 1 y el 3, robusto a outliers",
     "Rango intercuartílico (RIC)"),
    ("Si la distribución se inclina hacia un lado",
     "Asimetría (sesgo) — herramientas: pandas, numpy"),
  ]),
  ("¿Cómo se relacionan dos variables entre sí?", [
    ("Si dos variables varían juntas y en qué dirección",
     "Covarianza"),
    ("Fuerza y dirección de una relación LINEAL, estandarizada",
     "Correlación de Pearson"),
    ("Relación monótona usando rangos (robusta, no-lineal)",
     "Correlación de Spearman"),
    ("El recordatorio de que asociación no implica causa",
     "Correlación ≠ causación"),
    ("Una tercera variable que crea una asociación falsa",
     "Variable confusora"),
  ]),
]

# INTEGRADOR: de las SENALES concretas al concepto + tip verbalizable.
ESTACIONES = [
  ("RESUMIR CENTRO Y DISPERSIÓN", [
    ("Un solo valor atípico la arrastra hacia él",
     "Conviene la mediana si hay outliers o sesgo",
     "Es la suma de todos entre n",
     "Media",
     "la media es sensible a outliers; con datos sesgados, reporta la mediana"),
    ("Es el valor de en medio al ordenar los datos",
     "No la mueve un valor extremo",
     "Mejor resumen cuando la distribución está sesgada",
     "Mediana",
     "la mediana parte los datos a la mitad y aguanta los outliers"),
    ("Mide la dispersión en las MISMAS unidades del dato",
     "Es la raíz de la varianza",
     "Si es normal, el 95% cae a ±2 de la media",
     "Desviación estándar",
     "la SD dice qué tan lejos del centro vive un dato típico"),
  ]),
  ("RELACIÓN ENTRE VARIABLES", [
    ("Mide fuerza y dirección de una relación lineal",
     "Va de −1 a +1",
     "Asume relación lineal y se rompe con outliers fuertes",
     "Correlación de Pearson",
     "Pearson para relaciones lineales entre dos variables continuas"),
    ("Usa los rangos, no los valores crudos",
     "Capta relaciones monótonas aunque no sean lineales",
     "Robusta a outliers y sirve con datos ordinales",
     "Correlación de Spearman",
     "Spearman cuando la relación no es lineal o hay outliers"),
    ("Una correlación alta NO prueba que una cause la otra",
     "Puede haber una tercera variable moviendo a ambas",
     "Ej: helados y ahogamientos suben juntos (por el calor)",
     "Confusión (correlación ≠ causación)",
     "antes de gritar 'causa', busca la confusora que mueve a las dos"),
  ]),
]
