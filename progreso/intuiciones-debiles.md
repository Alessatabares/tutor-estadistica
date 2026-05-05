# Intuiciones débiles (necesitan refuerzo)

Intuiciones que quedaron parciales o en confusión. Cada entrada identifica el tipo de fallo para que el `drill-master` pueda diseñar el ejercicio correcto.

---

# Estructura de entrada

```
## [Concepto]

**Fecha**: AAAA-MM-DD
**Módulo**: X.Y
**Tipo de fallo**: imagen no formada | relaciones internas no visibles | discriminación insuficiente | invariante no identificada | intuición no anclada a su forma matemática | concepto desconectado de la red
**Sistema-anchor usado (que no fue suficiente)**: [...]
**Diagnóstico del evaluador**: [...]
**Drill recomendado**: [tipo, según el fallo]
**Estado**: pendiente | en refuerzo | resuelto
```

---

# Intuiciones débiles activas

---

## Tendencia central — "Tres tipos de estabilidad"

**Fecha**: 2026-05-05
**Módulo**: 1.1
**Tipo de fallo**: intuición parcial respecto al canon — lectura propia legítima pero falta la dimensión temporal/sistémica
**Sistema-anchor usado (que no fue suficiente)**: El bus A-B-A con variaciones de composición del conjunto.
**Diagnóstico del evaluador**: Alessa leyó los tres centros por sensibilidad a la composición del conjunto (quién se mueve cuando cambian los datos). El canon los lee también por tipo de estabilidad: instante (moda), tiempo (mediana), supervivencia del sistema (media). La lectura de Alessa es coherente y válida; no llega a la dimensión temporal. No es confusión — es una lectura propia que convive con el canon pero no lo cubre.
**Drill recomendado**: Sistema con distribución que cambia en el tiempo (ej. duración de recorridos en hora pico vs. hora valle). Preguntar: "¿qué centro se mantiene estable a lo largo del día? ¿qué centro refleja el momento?" Esto activa la dimensión temporal sin abandonar el anchor del bus.
**Estado**: pendiente

---

## Tendencia central — "Al azar = expectativa = media"

**Fecha**: 2026-05-05
**Módulo**: 1.1
**Tipo de fallo**: intuición no anclada — no apareció en sesión
**Sistema-anchor usado (que no fue suficiente)**: No se llegó a este punto.
**Diagnóstico del evaluador**: No es una confusión sino una ausencia. La conexión entre la media como expectativa matemática y la noción de "valor esperado al azar" no emergió. Requiere módulo de probabilidad como prerequisito; no bloquea avance a 1.2.
**Drill recomendado**: Retomar cuando se trabaje probabilidad. El bus A-B-A sirve: si se elige un recorrido "al azar" de la planilla, ¿qué duración esperarías? La respuesta es la media.
**Estado**: pendiente — no bloquea avance

---

## Tendencia central — "El concepto es previo al modelo"

**Fecha**: 2026-05-05
**Módulo**: 1.1
**Tipo de fallo**: intuición no anclada — no apareció explícita en sesión
**Sistema-anchor usado (que no fue suficiente)**: No se abordó directamente.
**Diagnóstico del evaluador**: No hubo confusión sobre esto, simplemente no se articuló el principio de forma explícita. Alessa demostró el principio al elegir el centro según la pregunta, pero no lo nombró como principio. Aparecerá naturalmente en módulos de modelado.
**Drill recomendado**: Retomar en módulo de modelado (4-5). Basta con preguntar: "antes de calcular algo, ¿qué pregunta estás respondiendo?" y contrastar dos encuadres distintos del mismo conjunto de datos.
**Estado**: pendiente — no bloquea avance

---

# Reglas

- Una intuición débil no se "cierra" sin un `sólida` del evaluador.
- Si una intuición lleva más de dos sesiones débil, escalar: revisar el anchor o agregar módulo intermedio.
- Una intuición débil bloquea avance al siguiente módulo solo si es prerrequisito directo. El cartógrafo decide.
