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

**Estado**: abierto
**Módulo**: 1.1
**Nivel**: 1
**Fecha de apertura**: pendiente — primera sesión.

**Sistema-anchor que funcionó**: a definir en sesión.
**Síntesis verbal**: a construir.
**Forma matemática**: a alcanzar al cerrar la fase 4 del concepto.

**Conexiones salientes**: a articular en sesión.

**Conexiones salientes anticipadas** (sembradas en sesión 2026-05-05, sin desarrollar):

- → **dispersión** (módulo 1.2) : *complementa*. Surgió cuando Alessa, al inventar la mediana, agregó "y con un rango de variabilidad". Lectura: el centro solo no alcanza para describir el conjunto; necesita un compañero que diga cuán lejos del centro vive la mayoría de los datos. Nodo destino aún no abierto.
- → **criterio de modelado / función de pérdida** (módulos 4-5) : *ilumina*. Surgió cuando Alessa, frente al outlier de 200, dijo "o pierde el jefe o pierde el conductor, de eso depende la decisión". Lectura: cada centro minimiza una pérdida específica (la media minimiza errores cuadrados, la mediana minimiza errores absolutos, la moda minimiza errores 0/1). La decisión de qué centro usar depende del costo asimétrico del error. Nodo destino aún no abierto.

**Conexiones entrantes**: vacío — es el primer nodo del temario.

**Preguntas abiertas**: ¿qué número representa a un grupo de números variables?

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

(Ninguno todavía.)

## Ramas poco desarrolladas

Toda la red. Estado inicial: solo el nodo raíz "tendencia central" está abierto.

## Conexiones esperadas y aún no establecidas

- tendencia central → dispersión (sembrada 2026-05-05; pendiente de abrir nodo de dispersión).
- tendencia central → criterio de modelado / función de pérdida (sembrada 2026-05-05; pendiente de abrir nodos en niveles 4-5).

## Microespacios — política

Cuando Alessa siembra una intuición que toca otro módulo, se registra como conexión saliente anticipada en el nodo actual (no como nodo abierto del módulo destino). Eso preserva la traza sin saturar el módulo en curso. Si la misma intuición vuelve a aparecer en sesiones posteriores, se promueve a nodo abierto. Detalle de la política en la memoria del proyecto (`feedback_microespacios-hilos-paralelos.md`).
