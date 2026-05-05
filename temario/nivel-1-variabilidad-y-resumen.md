# Nivel 1 — Variabilidad y resumen

## Pregunta-eje del nivel

¿Cómo describir un sistema variable con pocas piezas que conserven su esencia?

## Lugar en la columna vertebral

Es la base. Los demás niveles asumen que un sistema variable se puede describir. Antes de comparar (N2), relacionar (N3), inferir (N4) o modelar (N5), hay que saber qué dice un grupo.

## Módulos

### 1.1 — Tendencia central

**Pregunta-eje**: dado un grupo de números, ¿qué número los representa?

**Sistema-anchor candidato**: tres familias miran el mismo termómetro durante un mes. Una decide qué ropa sacar mañana (frecuencia → moda). Otra decide si la calefacción del invierno servirá (mitad de los días arriba/abajo → mediana). Otra calcula cuánto gas comprar (reparto total → media). Mismo dato, tres preguntas, tres centros.

**Conceptos**: moda, mediana, media. Cada uno como respuesta a una pregunta distinta sobre estabilidad.

**Formalización**:
- Moda = arg max f(x) — lo que domina por frecuencia.
- Mediana = valor que parte la masa en dos.
- Media = Σx/N — el reparto que conserva el total.

**Conecta con**: 1.2 (la pregunta natural que abre es: "OK, ya sé el centro, pero ¿qué tan lejos están los demás?").

### 1.2 — Dispersión

**Pregunta-eje**: ¿qué tan lejos están los demás del centro?

**Sistema-anchor candidato**: dos pueblos con la misma temperatura media anual. Uno costero (estable todo el año), uno continental (extremos de calor y frío). La media los iguala; la dispersión los separa.

**Conceptos**: rango, desviación absoluta, varianza, desviación estándar. Cada uno como una manera distinta de medir la separación del centro.

**Formalización**:
- Rango = max − min.
- Desviación absoluta = promedio de |x − x̄|.
- Varianza = promedio de (x − x̄)² — penalizar más lo que se aleja.
- Desviación estándar = √varianza — devolver a unidades originales.

**Conecta con**: 1.1 (centro y dispersión son lecturas complementarias del mismo sistema). 1.3 (abre la pregunta: "¿cómo está repartida la masa alrededor del centro?").

### 1.3 — Forma de la distribución

**Pregunta-eje**: ¿cómo está repartida la masa? ¿Simétrica, sesgada, con colas?

**Sistema-anchor candidato**: comparar tres histogramas: salarios de una empresa (sesgo a la derecha por pocos altos cargos), tiempo de espera del bus (cola larga por días malos), calificaciones de un examen difícil vs uno fácil. La forma es propiedad del sistema, no del cálculo.

**Conceptos**: simetría, asimetría (sesgo), curtosis, multimodalidad.

**Formalización**: índices de asimetría y curtosis (presentación intuitiva, profundización en N4).

**Conecta con**: 1.2 (la dispersión cuenta solo parte de la historia; la forma cuenta el resto). 1.4 (las colas largas anuncian la pregunta de outliers).

### 1.4 — Outliers y robustez

**Pregunta-eje**: ¿lo raro es ruido o es la señal?

**Sistema-anchor candidato**: en epidemiología, el caso raro fue la pista que abrió el campo (cólera en Soho). En finanzas, el cisne negro define el riesgo real. En clima, el evento extremo es el que importa. La decisión de "ignorar o investigar" es metodológica, no estadística.

**Conceptos**: outlier, robustez, sensibilidad de los estimadores. Por qué la mediana resiste y la media se mueve.

**Formalización**: criterios típicos (1.5×IQR, ±3σ) presentados como reglas pragmáticas, no como verdad. La pregunta importante es "¿este valor cuenta como dato del mismo sistema o de otro sistema?".

**Conecta con**: 1.1 (un outlier mueve la media pero no la mediana). 1.2 (un outlier infla la varianza). Abre N4 (la pregunta de muestreo: ¿el outlier es del sistema o vino de afuera?).

### 1.5 — Cierre transferencial del nivel

**Pregunta-eje**: las mismas 4 herramientas (centro + dispersión + forma + outliers), aplicadas al MISMO conjunto de preguntas, en 4 dominios distintos. ¿La estructura de relaciones se conserva?

**Estructura**: presentar 4 sistemas:
- Clima: temperatura diaria de un año.
- Clínica: presión arterial sistólica de pacientes en una consulta.
- Finanzas: rendimientos diarios de una acción durante un trimestre.
- Redes: tiempo entre publicaciones de un usuario en redes sociales.

Para cada uno, las mismas preguntas: ¿centro? ¿dispersión? ¿forma? ¿outliers?

**Lo que se gana**: ver que el aparato del nivel 1 es invariante al dominio. Cuando una pregunta vale en clima y en sangre, el concepto deja de pertenecer a un dominio. Esto es lo que produce "ver estadística en todo".

## Salida del nivel

La pregunta que abre N2 nace acá: "OK, sé describir un sistema variable. Pero ¿cómo distingo si DOS sistemas son realmente distintos?".
