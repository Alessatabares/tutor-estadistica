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

(Vacío al inicio.)

---

# Reglas

- Una intuición débil no se "cierra" sin un `sólida` del evaluador.
- Si una intuición lleva más de dos sesiones débil, escalar: revisar el anchor o agregar módulo intermedio.
- Una intuición débil bloquea avance al siguiente módulo solo si es prerrequisito directo. El cartógrafo decide.
