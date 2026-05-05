# La mecánica operativa: 5 fases

Cada concepto pasa por estas 5 fases, en este orden, sin saltos.

## Fase 1 — ANCHOR (imagen ancla del sistema)

Un escenario real, concreto, evocativo VISUALMENTE.

Reglas firmes:
- Es un SISTEMA con partes relacionadas, no un objeto suelto.
- Sin fórmulas, sin definición formal todavía.
- Genera la pregunta que el concepto resuelve.
- El tutor verifica que la imagen "está formada" — incluyendo sus relaciones internas — antes de avanzar.
- El tutor también pregunta dónde encaja este sistema en lo que ya construyeron.

Pregunta de cierre de la fase: ¿Alessa puede describir el sistema con sus partes Y sus relaciones internas? ¿Le quedó clara la pregunta que el sistema plantea?

Checkpoint: invocar `evaluador`.

## Fase 2 — CONTRASTE (modificar el sistema o cambiar la pregunta)

Cuatro modos de contraste:

- **Misma escena, otra pregunta** → otra respuesta.
- **Misma pregunta, sistema modificado** → respuesta cambia.
- **Concepto cercano pero distinto** → discriminación fina, mostrando cómo cambian las relaciones.
- **Caso donde el concepto FALLA** → identificación de los límites del sistema.

Regla firme: la modificación se ve PROPAGAR por el sistema, no se aplica a un elemento aislado. Si el cambio no se propaga, era un objeto suelto disfrazado de sistema.

Pregunta de cierre: ¿Alessa vio la propagación? ¿Identificó dónde el concepto deja de aplicar?

Checkpoint: invocar `evaluador`.

## Fase 3 — VARIACIONES (qué se conserva al transformar)

- Cambiá un parámetro: ¿qué se propaga? ¿qué se conserva?
- Escalá el sistema: ¿la relación principal se mantiene?
- Distorsioná los datos: ¿el sistema resiste? ¿en qué punto colapsa?
- Cambiá el contexto (clima → clínica → finanzas → redes): ¿la estructura de relaciones es la misma?

Regla firme: la matemática emerge AQUÍ. Como descripción de las INVARIANTES bajo transformación. No antes.

Pregunta de cierre: ¿Alessa puede nombrar qué se conserva y qué cambia? ¿La estructura de relaciones cruza dominios?

Checkpoint: invocar `evaluador`.

## Fase 4 — FORMALIZACIÓN (síntesis verbal + cierre matemático)

Dos sub-pasos secuenciales, en este orden:

### 4a. Síntesis verbal

Condensar la intuición en un slogan operacional. Lenguaje no técnico. La síntesis debe poder decirse en voz alta sin recurrir a símbolos.

Ejemplo (calibración): "la moda domina el instante, la mediana mantiene coherencia en el tiempo, la media sostiene la supervivencia del sistema".

### 4b. Cierre matemático

La fórmula como expresión OPERACIONAL de la intuición ya formada, no como definición de partida.

Reglas firmes:
- La fórmula se DERIVA de la intuición, no se da por encima.
- Antes de presentar la fórmula, el tutor pregunta: "¿cómo se traduciría esto en una operación numérica?".
- La fórmula final se muestra como respuesta a la pregunta, no como dictado.

Ejemplos:
- Media = Σx/N → "el reparto que conserva el total y reparte la carga".
- Mediana = valor que parte la masa en dos → "lo que resiste extremos".
- Moda = arg max f(x) → "lo que domina por frecuencia".

Pregunta de cierre: ¿Alessa lee la fórmula como expresión de la intuición o la lee como definición externa que coincide?

Checkpoint: invocar `evaluador`.

## Fase 5 — UBICACIÓN EN LA RED

Antes de cerrar el concepto:

- ¿Cómo se conecta esto con el concepto previo X?
- ¿Qué concepto previo se ilumina con esto?
- ¿Qué pregunta nueva se abre?

Reglas firmes:
- Articular al menos UNA conexión no trivial con un concepto previo.
- "No trivial" significa más que "ambos son medidas de tendencia central". Tiene que decir cómo uno ilumina al otro o cómo uno limita al otro.
- Si no aparece conexión, el concepto queda "huérfano" y se vuelve sobre él.
- Las conexiones nuevas se anotan para que el cartógrafo las registre en `/cierre`.

Checkpoint: invocar `evaluador`.

## Mapa de checkpoints del evaluador

| Fase | Pregunta para el evaluador |
|---|---|
| Anchor | ¿Imagen formada con relaciones internas visibles? |
| Contraste | ¿Discriminación fina o gruesa? ¿Vio la propagación? |
| Variaciones | ¿Captó las invariantes y los límites? |
| Formalización | ¿La fórmula está anclada a la intuición? |
| Red | ¿Concepto conectado o huérfano? |

## Tipos de fallo que el evaluador puede identificar

- Imagen no formada.
- Relaciones internas no visibles.
- Discriminación insuficiente con concepto cercano.
- Invariante no identificada.
- Intuición no anclada a su forma matemática.
- Concepto desconectado de la red.

Cada tipo tiene un drill específico (ver el subagent `drill-master`).
