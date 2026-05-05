# Nivel 3 — Relación

## Pregunta-eje del nivel

Cuando dos variables hablan entre sí dentro del mismo sistema, ¿qué tipo de relación las une?

## Lugar en la columna vertebral

N1 describió un sistema, N2 comparó dos. N3 mira DENTRO de un sistema y pregunta cómo se conectan sus partes. La estadística empieza a parecerse a un microscopio del sistema, no solo a un termómetro.

## Módulos

### 3.1 — Co-variación

**Pregunta-eje**: ¿dos variables se mueven juntas? ¿Hacia dónde?

**Sistema-anchor candidato**: temperatura y consumo de helado durante un año. Cuando una sube, la otra sube. Pero también: temperatura y ahogamientos. ¿Significa que el helado causa ahogamientos?

**Conceptos**: co-variación, dirección, intensidad. Asociación ≠ causalidad (anuncio temprano).

**Conecta con**: 1.2 (dispersión es co-variación de una variable consigo misma desplazada). Abre 3.4 (¿cuándo la relación es causal?).

### 3.2 — Correlación

**Pregunta-eje**: ¿cómo medir la fuerza de la relación?

**Sistema-anchor candidato**: scatterplots con distintas formas — lineal fuerte, lineal débil, no lineal, sin relación. La correlación responde solo a la primera.

**Conceptos**: coeficiente de correlación (Pearson, Spearman), límites de la correlación, casos donde correlación alta esconde no linealidad.

**Conecta con**: 3.1 (cuantifica lo que 3.1 describe cualitativamente). Limita en 3.3 (correlación no es predicción).

### 3.3 — Regresión

**Pregunta-eje**: si conozco una variable, ¿qué puedo decir de la otra?

**Sistema-anchor candidato**: estatura → peso. Conocer la estatura me da una estimación del peso, con error. La regresión es un resumen lineal de la co-variación.

**Conceptos**: línea de regresión, residuos, R², predicción puntual vs. predicción con incertidumbre.

**Conecta con**: 3.2 (la regresión usa la correlación pero agrega dirección y predicción). Abre N4 (¿cómo cuantificar la incertidumbre de una predicción?).

### 3.4 — Causalidad vs. asociación

**Pregunta-eje**: cuándo una asociación es causalidad y cuándo es engaño.

**Sistema-anchor candidato**: tres patrones de DAG mínimos:
- Confusión: Z → X y Z → Y. Helado y ahogamientos confundidos por verano.
- Mediación: X → M → Y. Tratamiento → bajada de presión → menos infartos.
- Collider: X → C ← Y. Talento y suerte como causas comunes de éxito; condicionar en éxito induce correlación espuria.

**Conceptos**: confusores, mediadores, colliders, criterios mínimos de inferencia causal.

**Conecta con**: 2.4 (los confusores son la causa de comparaciones inválidas). 3.1 (toda asociación pide preguntarse "¿qué tipo es?").

### 3.5 — Cierre transferencial

**Pregunta-eje**: las mismas herramientas de relación en 4 dominios.

**Estructura**: relación entre dos variables en clima (humedad ↔ temperatura), clínica (dosis ↔ respuesta), finanzas (tasa ↔ inversión), redes (tiempo de uso ↔ engagement).

## Salida del nivel

La pregunta que abre N4: "Todo lo que vimos hasta acá asume que tengo TODO el sistema. ¿Qué pasa cuando solo tengo una muestra?".
