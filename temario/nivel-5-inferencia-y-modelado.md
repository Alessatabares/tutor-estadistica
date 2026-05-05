# Nivel 5 — Inferencia y modelado

## Pregunta-eje del nivel

¿Cómo decido qué creer? ¿Cómo construyo modelos del mundo y elijo entre ellos?

## Lugar en la columna vertebral

Es el cierre. Acá se integra todo lo previo en CRITERIO DE MODELADO. La pregunta deja de ser "qué dicen los datos" y pasa a ser "qué representación del sistema sostiene mejor lo que veo".

## Módulos

### 5.1 — Test de hipótesis: ritual y lógica

**Pregunta-eje**: cuando la diferencia podría ser azar o efecto real, ¿cómo decidimos?

**Sistema-anchor candidato**: una moneda — ¿es justa? Tiramos 100 veces, salen 60 caras. ¿Suficiente para sospechar?

**Conceptos**: hipótesis nula, hipótesis alternativa, lógica del rechazo, tipos de error. El test como ritual con función específica, NO como respuesta automática.

**Conecta con**: 2.1 (el test es la formalización de "¿la diferencia es real?"). 4.4 (el test usa la distribución muestral).

### 5.2 — p-valores

**Pregunta-eje**: ¿qué dice un p-valor y qué NO dice?

**Sistema-anchor candidato**: el sistema 5.1 con número concreto. p < 0.05 vs. p = 0.06. La diferencia narrativa es enorme; la diferencia real es ínfima.

**Conceptos**: p-valor, significancia, malinterpretaciones (probabilidad de que la hipótesis sea verdad ≠ p-valor), problemas de reproducibilidad.

**Conecta con**: 5.1 (es la salida del test). 5.3 (la lectura bayesiana ofrece otra forma de pensar).

### 5.3 — Intuición bayesiana

**Pregunta-eje**: ¿cómo actualizo lo que creo cuando llega evidencia nueva?

**Sistema-anchor candidato**: prueba diagnóstica con sensibilidad y especificidad dadas. Una persona da positivo. ¿Qué probabilidad tiene de estar enferma? Depende de la prevalencia (creencia previa).

**Conceptos**: prior, likelihood, posterior. Bayes como mecanismo de actualización. Por qué dos personas con la misma evidencia pueden razonablemente creer cosas distintas.

**Conecta con**: 4.1 (probabilidad como expectativa vs. probabilidad como creencia). 5.2 (lectura alternativa al frecuentismo).

### 5.4 — Elección de modelos

**Pregunta-eje**: si hay varios modelos posibles, ¿cómo elegir?

**Sistema-anchor candidato**: ajustar polinomios de grado creciente a unos datos. Grado 1 subajusta. Grado 20 sobreajusta. ¿Cuál sirve?

**Conceptos**: bias-varianza, sobreajuste, parsimonia, validación. Criterios de información (AIC, BIC) como formalización del trade-off.

**Conecta con**: 3.3 (la regresión es el caso lineal del modelado). 4.3 (la validación se basa en muestreo).

### 5.5 — Cierre integrador del temario completo

**Pregunta-eje**: el cierre. Ver el mundo con lentes estadísticos antes de calcular.

**Estructura**: tomar UN problema real complejo (epidemiológico, social, financiero) y recorrerlo aplicando todo:
- Describirlo (N1).
- Comparar grupos relevantes (N2).
- Detectar relaciones (N3).
- Reconocer la incertidumbre (N4).
- Elegir un modelo (N5).

Y articular en cada paso QUÉ pregunta estamos haciendo.

**Lo que se gana**: la meta del cierre es poder decir "veo estadística en todo" no como slogan sino como capacidad operativa.

## Salida del temario

Al cerrar este módulo, Alessa debería poder:

- Tomar un fenómeno cualquiera y articular qué preguntas estadísticas lo iluminarían.
- Discriminar cuándo una herramienta cabe y cuándo no.
- Reconocer cuándo le están vendiendo certezas falsas (p-valores mal usados, gráficos engañosos, asociaciones disfrazadas de causalidad).
- Construir su propio criterio de modelado.

Esto es el objetivo declarado del proyecto: "saber estadística real y verla en todo".
