# Intuiciones consolidadas

Intuiciones que Alessa ha consolidado a lo largo del proceso. Cada entrada incluye la síntesis verbal y el sistema-anchor que la produjo.

---

# Estructura de entrada

```
## [Concepto] — [síntesis verbal en una línea]

**Fecha de consolidación**: AAAA-MM-DD
**Módulo**: X.Y
**Sistema-anchor que funcionó**: [...]
**Forma matemática asociada**: [...]
**Conexiones articuladas en la red**: [...]
**Cómo se evaluó**: [diagnóstico del evaluador]
```

---

# Intuiciones

---

## Tendencia central — "El centro depende de la pregunta, no de los datos."

**Fecha de consolidación**: 2026-05-05
**Módulo**: 1.1
**Sistema-anchor que funcionó**: El bus A-B-A. El dueño de la empresa y el conductor piden cosas distintas sobre la misma planilla de duraciones → dos números resumen distintos del mismo conjunto.
**Forma matemática asociada**: Media = Σx/N; Mediana = valor posicional central; Moda = arg max f(x)
**Conexiones articuladas en la red**: tendencia central → criterio de modelado (la pregunta determina el centro)
**Cómo se evaluó**: Evaluador dictaminó sólida en cierre de anchor y contraste.

---

## Tendencia central — "El promedio mezcla las masas y las reparte en partes iguales."

**Fecha de consolidación**: 2026-05-05
**Módulo**: 1.1
**Sistema-anchor que funcionó**: El bus A-B-A. Los recorridos son masas de distinta magnitud; el promedio las junta y las divide en N porciones iguales. Por eso conserva el total y por eso un outlier lo mueve.
**Forma matemática asociada**: Media = Σx/N → el reparto conserva el total
**Conexiones articuladas en la red**: tendencia central → dispersión (el outlier que mueve la media es la semilla de variabilidad)
**Cómo se evaluó**: Producida por Alessa en fase de variaciones. Evaluador dictaminó sólida.

---

## Tendencia central — "La moda lee dónde se concentra la masa por frecuencia."

**Fecha de consolidación**: 2026-05-05
**Módulo**: 1.1
**Sistema-anchor que funcionó**: El bus A-B-A. La duración más repetida es la moda. Ciega al outlier. Ciega también cuando los valores son todos distintos.
**Forma matemática asociada**: Moda = arg max f(x)
**Conexiones articuladas en la red**: (ninguna adicional; conexión al criterio de modelado compartida con la entrada grupal)
**Cómo se evaluó**: Producida por Alessa en fase de variaciones. Evaluador dictaminó sólida.

---

## Tendencia central — "La mediana centra por posición."

**Fecha de consolidación**: 2026-05-05
**Módulo**: 1.1
**Sistema-anchor que funcionó**: El bus A-B-A. Alessa inventó la operación de ordenar y partir antes de recibir el nombre técnico. Resiste extremos porque la posición del valor extremo no cambia aunque su magnitud sea enorme.
**Forma matemática asociada**: Mediana = valor que parte la masa ordenada en dos mitades iguales
**Conexiones articuladas en la red**: tendencia central → dispersión (la mediana y el rango intercuartílico son una pareja natural)
**Cómo se evaluó**: Alessa reinventó la operación. Evaluador dictaminó sólida.

---

## Tendencia central — "La robustez es virtud o defecto según el costo del error."

**Fecha de consolidación**: 2026-05-05
**Módulo**: 1.1
**Sistema-anchor que funcionó**: El bus A-B-A. La misma propiedad (ignorar outliers) puede proteger la decisión del gerente o traicionar la del conductor que planifica por turnos extremos.
**Forma matemática asociada**: (implícita en la elección del estimador según la función de pérdida)
**Conexiones articuladas en la red**: tendencia central → criterio de modelado / función de pérdida (ilumina)
**Cómo se evaluó**: Alessa lo articuló con sus palabras ("o pierde el jefe o pierde el conductor"). Evaluador dictaminó sólida en cierre de variaciones.

---

## Tendencia central — "Cuánto cambia un centro depende del peso del cambio en el conjunto."

**Fecha de consolidación**: 2026-05-05
**Módulo**: 1.1
**Sistema-anchor que funcionó**: El bus A-B-A. Modificar un recorrido extremo mueve la media en proporción a su frecuencia y magnitud relativas en el total. La mediana no se mueve mientras la posición central no cambie.
**Forma matemática asociada**: sensibilidad de la media = Δx/N; sensibilidad de la mediana = 0 si el rango central no se altera
**Conexiones articuladas en la red**: tendencia central → dispersión (la sensibilidad al cambio es la semilla conceptual de la varianza)
**Cómo se evaluó**: Articulada por Alessa en fase de variaciones. Evaluador dictaminó sólida.

---

# Reglas

- Una intuición no se agrega acá sin un `sólida` del evaluador en TODAS las fases (anchor, contraste, variaciones, formalización, red).
- Las intuiciones acá deben tener al menos UNA conexión articulada en la red conceptual.
- Si una intuición se debilita en sesiones posteriores (ej. por confusión con concepto cercano), se mueve a `intuiciones-debiles.md` y se actualiza la red.
