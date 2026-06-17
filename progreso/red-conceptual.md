# Red conceptual

Mapa vivo de los conceptos que Alessa ha trabajado y las relaciones articuladas entre ellos.

NO es una lista lineal. NO es un diagrama gráfico. Es texto navegable: cada concepto es un nodo con secciones, las relaciones son enlaces internos descritos.

El cartógrafo es responsable de mantenerla coherente y completa. Todos los demás archivos de progreso se derivan de este.

---

# Estructura de un nodo

```
## Nodo: [nombre del concepto]

**Estado**: abierto | consolidado | débil | huérfano
**Módulo**: X.Y
**Nivel**: 1-5
**Fecha de apertura**: AAAA-MM-DD
**Fecha de consolidación**: AAAA-MM-DD (si aplica)

**Sistema-anchor que funcionó**: [breve]
**Síntesis verbal**: [el slogan]
**Forma matemática**: [fórmula + lectura intuitiva]

**Conexiones salientes**:
- → [otro nodo] : [tipo de relación]

**Conexiones entrantes**:
- ← [otro nodo] : [tipo]

**Preguntas abiertas**: [si hay]
```

# Tipos de relación entre nodos

- **ilumina** — uno hace ver al otro de manera nueva.
- **es un caso de** — uno es instancia particular de otro más general.
- **se opone a** — uno responde a una pregunta donde el otro falla.
- **depende de** — uno requiere el otro como prerrequisito.
- **abre** — uno genera la pregunta que el otro responde.
- **complementa** — los dos se necesitan para una lectura completa.

---

# Nodos por nivel

## Nivel 1 — Variabilidad y resumen

### Nodo: tendencia central

**Estado**: consolidado-parcial (intuición sólida; parcial respecto al canon en dimensión temporal/sistémica)
**Módulo**: 1.1
**Nivel**: 1
**Fecha de apertura**: 2026-05-05
**Fecha de consolidación**: 2026-05-05

**Sistema-anchor que funcionó**: El bus con recorridos cabecera A → cabecera B → cabecera A. Cada vuelta dura distinto por causas internas (peso de pasajeros, ocupación, accidentes, semáforos, posición del estacionamiento). Cada vuelta termina y produce un número. La planilla acumula la lista. El gerente la abre y necesita resumirla.

**Síntesis verbal**: "El promedio reparte. La mediana centra por posición. La moda lee la repetición. Cuál usás depende de qué pregunta hacés y de quién paga el error."

**Forma matemática**:
- Media = Σx/N → "el reparto que conserva el total y distribuye la carga en partes iguales"
- Mediana = valor que parte la masa en dos → "centra por posición; resiste extremos porque la posición del valor extremo no cambia"
- Moda = arg max f(x) → "lee dónde se concentra la masa por frecuencia; ciega al outlier, ciega también cuando todos los valores son distintos"

**Conexiones salientes**:
- → dispersión (módulo 1.2) : complementa — Alessa anticipó "un rango de variabilidad" al inventar la mediana; el centro solo no describe el conjunto
- → criterio de modelado / función de pérdida (módulos 4-5) : ilumina — "o pierde el jefe o pierde el conductor, de eso depende la decisión"; la elección del centro depende de quién paga el error

**Conexiones entrantes**:
- vacío — es el primer nodo del temario

**Preguntas abiertas**:
- "Tres tipos de estabilidad" (instante / tiempo / supervivencia) — Alessa leyó los tres centros por sensibilidad a la composición del conjunto, no por tipo de estabilidad. Lectura propia legítima, pero falta la dimensión temporal/sistémica. Retomar en módulo 1.2 o en revisión de 1.1.
- "Al azar = expectativa = media" — no apareció. Retomar cuando llegue probabilidad.
- "El concepto es previo al modelo" — no apareció explícito. Retomar en módulo de modelado.

---

## Nivel 2 — Comparación

(Sin nodos abiertos todavía.)

## Nivel 3 — Relación

(Sin nodos abiertos todavía.)

## Nivel 4 — Muestreo e incertidumbre

(Sin nodos abiertos todavía.)

## Nivel 5 — Inferencia y modelado

(Sin nodos abiertos todavía.)

---

# Diagnóstico de la red

## Conceptos huérfanos

Ninguno. El nodo "tendencia central" tiene dos conexiones salientes articuladas por Alessa en sesión.

## Ramas poco desarrolladas

- Nivel 1 completo en nodos: solo tendencia central. Dispersión (1.2) aún sin abrir.
- Niveles 2-5: sin nodos abiertos.

## Conexiones esperadas y aún no establecidas

- tendencia central → dispersión (1.2) : conexión sembrada, nodo receptor aún no abierto.
- tendencia central → criterio de modelado / función de pérdida (4-5) : conexión sembrada, nodo receptor aún no abierto.
- tendencia central ← probabilidad/expectativa : no articulada todavía. Aparecerá cuando llegue módulo de probabilidad.

## Microespacios — política

Cuando Alessa siembra una intuición que toca otro módulo, se registra como conexión saliente anticipada en el nodo actual (no como nodo abierto del módulo destino). Eso preserva la traza sin saturar el módulo en curso. Si la misma intuición vuelve a aparecer en sesiones posteriores, se promueve a nodo abierto. Detalle de la política en la memoria del proyecto (`feedback_microespacios-hilos-paralelos.md`).
