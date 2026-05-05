# tutor-estadistica

Tutor socrático personal de destilación conceptual de estadística, construido sobre Claude Code.

## Idea

No es un tutor que enseña estadística. Es un sistema que destila el esqueleto conceptual: cada concepto entra como imagen mental de un SISTEMA con partes relacionadas, se modifica para ver qué se propaga, y la fórmula matemática emerge solo al final como descripción de las invariantes.

La meta: ver estadística en todo. Reconocer la estructura de preguntas estadísticas tanto en clima como en clínica, en finanzas como en redes sociales.

## Método

Cada concepto se aprende en 5 fases:

1. **Anchor** — un sistema-imagen concreto que genera la pregunta.
2. **Contraste** — modificar el sistema, ver qué cambia.
3. **Variaciones** — qué se conserva bajo transformación.
4. **Formalización** — síntesis verbal y cierre matemático.
5. **Ubicación en la red** — cómo conecta con todo lo demás.

Detalles del método en `metodologia/`.

## Estructura

- `CLAUDE.md` — instrucciones operativas para el tutor.
- `metodologia/` — los 9 principios, la mecánica de 5 fases, el perfil cognitivo, el glosario de imágenes y la vara de calidad.
- `temario/` — 5 niveles, de "describir un grupo variable" hasta "criterio de modelado".
- `modulos/` — un archivo por módulo trabajado (se llena conforme avanzamos).
- `progreso/` — memoria viva: estado actual, red conceptual, intuiciones consolidadas y débiles, bitácora.
- `.claude/agents/` — subagents (tutor, evaluador, drill-master, cartógrafo).
- `.claude/commands/` — slash commands.

## Cómo arrancar una sesión

```bash
cd tutor-estadistica
claude
```

Dentro de Claude Code, escribí `/sesion`. El sistema lee la memoria viva y propone qué trabajar.

## Comandos

| Comando | Para qué |
|---|---|
| `/sesion` | Arrancar. Lee memoria, propone tema. |
| `/sintesis` | Síntesis tipo "10 puntos" del concepto trabajado. |
| `/cierre` | Cerrar la sesión y actualizar la memoria. |
| `/drill` | Modo discriminación entre conceptos cercanos. |
| `/estado` | Mapa de lo consolidado y lo débil. |
| `/anchor` | Forzar exploración de un escenario nuevo. |
| `/imagen` | Reactivar la exploración visual del concepto actual. |
| `/red` | Mostrar la red conceptual viva. |

## Estado

En construcción. Diseñado por y para Alessa.
