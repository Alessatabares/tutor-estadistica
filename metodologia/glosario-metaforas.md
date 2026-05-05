# Glosario de imágenes-de-sistema (patrones)

Catálogo de TIPOS de imágenes-de-sistema que han funcionado para Alessa. Esto NO es un catálogo de instancias específicas (eso vive en `progreso/imagenes-canon.md`). Esto es la galería de PATRONES reusables.

# Estructura de entrada

```
## [Nombre del patrón]

**Estructura del sistema**: [qué elementos y qué relaciones]
**Para qué tipo de concepto funciona**: [...]
**Por qué funciona para Alessa**: [...]
**Instancia(s) específica(s) en uso**: [referencias a imagenes-canon.md o al módulo]
```

# Cómo se canoniza un patrón

Un sistema-anchor pasa de instancia (`imagenes-canon.md`) a patrón (este archivo) cuando:

1. Funcionó con éxito en al menos un módulo.
2. La estructura del sistema (tipo de elementos + tipo de relaciones) es reusable para otros conceptos del mismo tipo.
3. El cartógrafo identifica que la abstracción es legítima — no que dos sistemas comparten "una palabra" sino que comparten ESTRUCTURA.

---

# Patrones canonizados

---

## "Tres lentes sobre el mismo dato"

**Estructura del sistema**: Una misma realidad (un conjunto de números) observada desde tres preguntas distintas que producen tres respuestas distintas. Las respuestas no se contradicen: cada una es correcta para su pregunta. El encuadre define el resultado.
**Para qué tipo de concepto funciona**: Conceptos donde la elección del estimador o el modelo depende de quién pregunta y qué quiere saber. Especialmente útil cuando hay múltiples formas "correctas" de resumir algo.
**Por qué funciona para Alessa**: Alessa piensa en relaciones, no en piezas. Ver que tres números distintos emergen de la misma planilla, según quién la abra, activa inmediatamente la pregunta "¿de qué depende cuál usar?" — que es exactamente la pregunta que genera criterio de modelado.
**Instancia(s) específica(s) en uso**: El bus A-B-A, módulo 1.1 — gerente vs. conductor vs. pasajero hacen preguntas distintas sobre la misma planilla de duraciones. Ver `progreso/imagenes-canon.md`.

---

# Patrones candidatos (anticipados, no canonizados todavía)

Estos son patrones que probablemente aparezcan, pero no se agregan formalmente hasta que cumplan los criterios de canonización.

- **"Reparto bajo restricción"**: pastel finito, N personas, conservación del total. Útil para promedios, varianzas, cualquier concepto que opere sobre un total que se distribuye.
- **"Señal en ruido"**: emisión clara + interferencia variable. Útil para conceptos de inferencia, error de medición, detección.
- **"Ecosistema con feedback"**: presa-depredador, flujos cíclicos. Útil para conceptos que requieren ver retroalimentación.
- **"Sistema bajo transformación"**: aplicar una operación al sistema y ver qué se conserva. Útil para invariantes, escala, robustez.
- **"Objetos con peso"**: los datos no son puntos abstractos sino objetos con masa/peso. Introducido por Alessa en módulo 1.1 ("cada recorrido como una masa de pura magnitud"). Potencialmente reusable para varianza, ponderación, distribuciones de probabilidad. Canonizar cuando aparezca en un segundo módulo.
