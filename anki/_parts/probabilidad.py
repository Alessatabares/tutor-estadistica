# -*- coding: utf-8 -*-
NAME = "Probabilidad"

# EJE CLINICO: del PROBLEMA (en voz clinica/de investigacion) al concepto.
EJES = [
  ("Algo es incierto, ¿cómo le pongo número a qué tan probable es?", [
    ("Listar todos los resultados posibles de un experimento",
     "Espacio muestral"),
    ("Quedarme con el subconjunto de resultados que me interesa",
     "Evento"),
    ("Asignar un número entre 0 y 1 a qué tan probable es",
     "Probabilidad (proporción / frecuencia a largo plazo)"),
    ("Dos resultados que no pueden ocurrir a la vez",
     "Eventos mutuamente excluyentes"),
  ]),
  ("¿Cómo combino la probabilidad de varios eventos?", [
    ("Que un evento no cambie la probabilidad del otro",
     "Independencia"),
    ("La probabilidad de A dado que ya sé que ocurrió B",
     "Probabilidad condicional P(A|B)"),
    ("Probabilidad de que ocurra A o B",
     "Regla de la suma"),
    ("Probabilidad de que ocurran A y B juntos",
     "Regla del producto"),
  ]),
  ("Un paciente da positivo en una prueba, ¿de verdad está enfermo?", [
    ("Actualizar mi creencia con la evidencia de la prueba",
     "Teorema de Bayes"),
    ("Qué tan bien la prueba detecta enfermos / descarta sanos",
     "Sensibilidad / Especificidad"),
    ("Si dio positivo, la probabilidad de estar realmente enfermo",
     "Valor predictivo positivo (VPP)"),
    ("Lo que sabía antes de la prueba (qué tan común es la enfermedad)",
     "Probabilidad previa (prior) / prevalencia"),
  ]),
  ("Quiero modelar una variable que toma valores al azar", [
    ("Una variable cuyo valor es el resultado de un experimento aleatorio",
     "Variable aleatoria"),
    ("Contar éxitos en un número fijo de intentos sí/no",
     "Distribución binomial"),
    ("Contar eventos raros en un intervalo de tiempo o espacio",
     "Distribución de Poisson"),
    ("Una variable continua simétrica en forma de campana",
     "Distribución normal"),
    ("El valor promedio que esperaría a la larga",
     "Valor esperado E[X]"),
    ("Cuánto se dispersan los valores alrededor del promedio",
     "Varianza (herramienta: scipy.stats)"),
  ]),
  ("¿Por qué tantísimas cosas terminan viéndose como campana?", [
    ("Los promedios de muestras se vuelven normales aunque los datos no lo sean",
     "Teorema del Límite Central (TLC)"),
    ("Cuántas desviaciones estándar está un valor de la media",
     "z-score (estandarización)"),
  ]),
]

# INTEGRADOR: de las SENALES concretas al concepto + tip verbalizable.
ESTACIONES = [
  ("CONDICIONAL Y BAYES", [
    ("La probabilidad cambia porque ya sé que ocurrió otro evento",
     "Se escribe P(A|B)",
     "Es la base del razonamiento diagnóstico",
     "Probabilidad condicional",
     "P(A|B) es 'la probabilidad de A en el mundo donde B ya ocurrió'"),
    ("Una prueba muy sensible da muchos falsos positivos si la enfermedad es rara",
     "El VPP depende de la prevalencia, no solo de la prueba",
     "Actualizo el prior con la evidencia",
     "Teorema de Bayes",
     "con enfermedad rara, hasta una buena prueba da positivos casi siempre falsos: el prior manda"),
    ("Detecta bien a los enfermos (pocos falsos negativos)",
     "Si sale NEGATIVA, descarta la enfermedad (SnNOut)",
     "Es fija: no depende de la prevalencia",
     "Sensibilidad",
     "alta sensibilidad: una negativa me deja descartar"),
    ("Identifica bien a los sanos (pocos falsos positivos)",
     "Si sale POSITIVA, confirma la enfermedad (SpPIn)",
     "También es fija: no depende de la prevalencia",
     "Especificidad",
     "alta especificidad: una positiva me deja confirmar"),
  ]),
  ("DISTRIBUCIONES", [
    ("Cuenta éxitos en un número fijo de intentos sí/no",
     "Cada intento independiente con la misma probabilidad",
     "Ej: cuántos de 20 pacientes responden al fármaco",
     "Distribución binomial",
     "binomial = contar éxitos en n monedas"),
    ("Cuenta eventos raros en un intervalo fijo",
     "Ej: número de ingresos a urgencias por hora",
     "Su media es igual a su varianza",
     "Distribución de Poisson",
     "Poisson = contar eventos raros por unidad de tiempo"),
    ("Continua, simétrica, en forma de campana",
     "Queda definida por su media y su desviación estándar",
     "El 95% cae a ±2 desviaciones de la media",
     "Distribución normal",
     "la normal: la media manda el centro, la SD manda el ancho"),
  ]),
  ("EL PUENTE: TLC Y VARIANZA", [
    ("Los PROMEDIOS de muestras se vuelven normales",
     "Aunque los datos originales no sean normales",
     "Funciona cuando n es suficientemente grande",
     "Teorema del Límite Central",
     "el TLC es la bisagra: vuelve campana a los promedios de CUALQUIER dato; de ahí sale toda la inferencia"),
    ("Mide a cuántas desviaciones estándar está un valor de la media",
     "Permite comparar valores de escalas distintas",
     "z = (x − media) / SD",
     "z-score",
     "el z-score traduce cualquier valor a 'cuántas SD me alejo del centro'"),
    ("Cuánto se dispersan los valores de una variable",
     "Reaparece como dispersión, error estándar y peso del meta-análisis",
     "Es el mismo número viajando por todas las capas",
     "Varianza",
     "la varianza es el hilo que cose probabilidad, descriptiva e inferencia"),
  ]),
]

# CAPA 2 - CONTRASTE: discriminar conceptos cercanos + supuestos/fallos.
# (tema, planteamiento, resolucion)
CONTRASTES = [
  ("Sensibilidad vs Especificidad",
   "¿Cuál te sirve para DESCARTAR, cuál para CONFIRMAR, y de qué NO dependen?",
   "Sensibilidad: detecta enfermos; si es alta y sale NEGATIVA, descartas (SnNOut). "
   "Especificidad: identifica sanos; si es alta y sale POSITIVA, confirmas (SpPIn). "
   "Las dos son propiedades fijas de la prueba: NO dependen de la prevalencia (eso es el VPP/VPN)."),
  ("Sensibilidad/Especificidad vs VPP/VPN",
   "Las cuatro describen una prueba diagnóstica. ¿Cuáles cambian con la prevalencia y cuáles no?",
   "Sensibilidad y especificidad son intrínsecas a la prueba: no cambian con la prevalencia. "
   "VPP y VPN sí dependen de la prevalencia: en enfermedad rara el VPP cae aunque la prueba sea buena. "
   "Por eso un positivo en tamiz poblacional suele ser falso."),
  ("Binomial vs Poisson",
   "Las dos cuentan eventos. ¿Cuándo cada una?",
   "Binomial: número FIJO de intentos sí/no con la misma p (cuántos de 20 pacientes responden). "
   "Poisson: eventos raros por intervalo de tiempo/espacio, sin tope fijo (ingresos por hora). "
   "Pista: ¿hay un n claro de intentos? Binomial. ¿Cuentas ocurrencias por unidad de tiempo? Poisson."),
  ("Independientes vs Mutuamente excluyentes (la trampa)",
   "Dos eventos que no pueden ocurrir juntos, ¿son independientes?",
   "NO. Si son mutuamente excluyentes y ambos posibles, son DEPENDIENTES: saber que ocurrió A te dice "
   "que B no ocurrió (cambia su probabilidad a cero). Excluyente = no coexisten; independiente = no se informan. "
   "Es uno de los errores más comunes."),
  ("Prior vs Posterior",
   "En Bayes, ¿qué distingue al prior del posterior?",
   "Prior: lo que creías ANTES de la prueba (la prevalencia, tu creencia base). "
   "Posterior: lo que crees DESPUÉS de incorporar la evidencia (el VPP es un posterior). "
   "Bayes es la máquina que convierte prior + evidencia en posterior."),
]
