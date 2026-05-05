---
description: Cierra la sesión y actualiza la memoria viva. Invoca al cartógrafo.
---

Fin de sesión. Hay que actualizar la memoria.

# Pasos

1. Confirmale a Alessa que vas a cerrar la sesión.
2. Si todavía no se hizo `/sintesis` en esta sesión, sugerí hacerla primero — el cartógrafo trabaja mejor con la síntesis ya hecha.
3. Invocá al subagent `cartografo` con un resumen explícito de:
   - Qué concepto se trabajó (módulo X.Y).
   - Qué fases se completaron (anchor, contraste, variaciones, formalización, red).
   - Qué intuiciones quedaron sólidas, parciales o confusas (con tipo de fallo, según el evaluador).
   - Qué sistema-anchor se usó.
   - Qué conexiones nuevas en la red aparecieron.
   - Qué quedó abierto para la próxima sesión.

4. El cartógrafo actualiza:
   - `progreso/red-conceptual.md` (artefacto principal)
   - `progreso/estado-actual.md`
   - `progreso/intuiciones-fuertes.md` o `intuiciones-debiles.md`
   - `progreso/imagenes-canon.md` (si aplica)
   - `metodologia/glosario-metaforas.md` (si la imagen es un patrón reusable)
   - `modulos/X-Y-titulo.md` (si el módulo se completó al menos hasta fase 4)
   - `progreso/bitacora.md`

5. Una vez actualizado, mostrale a Alessa un resumen de qué se persistió y qué propuesta queda para la próxima sesión.
