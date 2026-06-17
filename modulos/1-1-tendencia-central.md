# Módulo 1.1 — Tendencia central

**Estado**: consolidado-parcial
**Fecha de cierre**: 2026-05-05
**Fases completadas**: anchor, contraste, variaciones, formalización (4a + 4b), red (parcial)

---

## Sistema-anchor canónico

El bus haciendo recorridos cabecera A → cabecera B → cabecera A. Cada vuelta dura distinto por causas internas: peso de pasajeros, ocupación, accidentes, semáforos, posición del estacionamiento. Cada vuelta termina y produce un número (su duración). La planilla acumula esa lista. El gerente abre la planilla y necesita resumirla.

El anchor lo eligió Alessa — redirigió desde el escenario clínico propuesto inicialmente (sala de guardia + presión arterial). La redirección fue productiva.

**Por qué este sistema funciona para tendencia central**: genera variabilidad naturalmente con causas visibles y distinguibles; convierte el proceso dinámico en una lista sin que la lista parezca abstracta; permite hacer tres preguntas distintas (gerente, conductor, pasajero) sobre la misma planilla, lo que produce tres centros distintos del mismo conjunto y dispara la pregunta fundamental: ¿de qué depende cuál usar?

---

## Variaciones que produjeron insight

1. **Misma planilla, distintas preguntas**: el gerente quiere el tiempo "promedio" para planificar turnos; el conductor quiere saber cuál es el recorrido más frecuente para prepararse; el pasajero quiere saber qué esperar. Tres números distintos del mismo conjunto. Esto disparó la intuición "el centro depende de la pregunta".

2. **Introducir un recorrido extremo**: un accidente alarga un recorrido a tres veces lo habitual. La media se mueve; la mediana apenas; la moda no. Esto hizo visible la diferencia de robustez.

3. **Todos los recorridos distintos**: la moda desaparece o pierde sentido. Su límite emergió sin necesitar formularlo desde afuera.

4. **Cambiar quién paga el error**: si el gerente subestima el tiempo, el conductor llega tarde y pierde el turno. Si el gerente sobreestima, la empresa pierde plata. La misma robustez puede ser virtud o defecto.

---

## Intuiciones consolidadas

### "El centro depende de la pregunta, no de los datos."
El dueño y el pasajero piden cosas distintas sobre la misma planilla → dos números resumen distintos del mismo conjunto.

### "El promedio mezcla las masas y las reparte en partes iguales."
Por eso conserva el total. Por eso un outlier lo mueve: tiene mucha masa en un extremo, y esa masa entra al reparto.

### "La moda lee dónde se concentra la masa por frecuencia."
Ciega al outlier. Ciega también cuando los valores son todos distintos.

### "La mediana centra por posición."
Alessa inventó la operación antes de recibir el nombre técnico: ordenar los recorridos y tomar el del medio. Resiste extremos porque la posición del valor extremo no cambia aunque su magnitud sea enorme.

### "La robustez es virtud o defecto según el costo del error."
La misma propiedad (ignorar outliers) puede proteger una decisión y traicionar otra. Depende de quién paga el error.

### "Cuánto cambia un centro depende del peso del cambio en el conjunto."
Frecuencia × magnitud relativa. Un recorrido extremo mueve la media en proporción a su peso en el total; no mueve la mediana mientras la posición central no cambie.

---

## Síntesis verbal (slogan operacional)

"El promedio reparte. La mediana centra por posición. La moda lee la repetición. Cuál usás depende de qué pregunta hacés y de quién paga el error."

---

## Formalización matemática

- **Media**: Σx/N — "el reparto que conserva el total y distribuye la carga en partes iguales"
- **Mediana**: valor que parte la masa ordenada en dos mitades — "centra por posición; resiste extremos porque la posición del valor extremo no cambia"
- **Moda**: arg max f(x) — "lee dónde se concentra la masa por frecuencia"

Las fórmulas viven como imágenes PNG en `progreso/imagenes-formulas/` (generadas en sesión; rama feat/formulas-como-imagenes pendiente de merge).

---

## Conexiones a otros módulos

- **→ módulo 1.2 (dispersión)** : complementa — Alessa anticipó "un rango de variabilidad" al inventar la mediana. El centro solo no describe el conjunto; se necesitan los dos.
- **→ módulos 4-5 (criterio de modelado / función de pérdida)** : ilumina — "o pierde el jefe o pierde el conductor, de eso depende la decisión". La elección del centro es un caso de elección de modelo según la función de pérdida.

Detalle ampliado de estas conexiones en rama `feat/microespacios-tendencia-central` (pendiente de merge).

---

## Intuiciones del canon no alcanzadas

Estas no bloquean avance a 1.2, pero se anotan para retomar.

1. **"Tres tipos de estabilidad"** (instante / tiempo / supervivencia): Alessa leyó los tres centros por sensibilidad a la composición del conjunto — lectura propia válida, pero falta la dimensión temporal/sistémica. Retomar con sistema que cambia en el tiempo.
2. **"Al azar = expectativa = media"**: no apareció. Requiere probabilidad como prerequisito.
3. **"El concepto es previo al modelo"**: Alessa lo demostró implícitamente pero no lo articuló como principio. Retomar en módulos de modelado.
