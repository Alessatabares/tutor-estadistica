# 🔬 Laboratorio de Intuiciones

Página interactiva (HTML + JS vanilla, sin build) para **repasar las intuiciones de
estadística simulándolas con el dedo**. No es un quiz: cada concepto se manipula y la
fórmula emerge solo al final, siguiendo el método del repo.

## El método, hecho interactivo

Cada lente recorre las fases del tutor, en este orden fijo:

```
① La necesidad (escenario real con tensión)
② Predice (tu corazonada, antes de tocar nada)
③ Simula (manipulas: arrastras puntos, mueves sliders)
④ La forma matemática (recién aquí emerge la fórmula)
⑤ Cuándo engaña
⑥ Interpretación real + frase-ancla
```

Es el principio del canon hecho gesto: **primero ver, después nombrar, finalmente
formalizar**. Los escenarios son médicos (urgencias, presión arterial, glucosa) para
que peguen con tu dominio.

## Bloque 1 · Una variable (este archivo)

| # | Lente | Imagen-de-sistema | Qué manipulas |
|---|-------|-------------------|----------------|
| 1 | Media | balanza / objetos con peso | arrastras un turno → el fulcro corre |
| 2 | Mediana | la fila ordenada, el del medio | sueltas un outlier → media persigue, mediana aguanta |
| 3 | Varianza | ligas tensas + cuadrados | estiras puntos → crecen los cuadrados; ves que las desviaciones suman 0 |
| 4 | n−1 | muestrear un mundo oculto | tomas muchas muestras → ÷n subestima, ÷n−1 corrige |
| 5 | SD | banda ±1 SD | aparece la franja donde vive el dato típico |
| 6 | Normal / z | curva de densidad | mueves un valor → su z y su percentil; bandas 68/95/99.7 |
| 7 | Área | rectángulos de Riemann | subes el nº de rectángulos → el área converge a la probabilidad |

Cada lente entrega una **frase-ancla** que se colecciona abajo. El progreso se guarda en
`localStorage`.

## Cómo abrirlo

- **Local:** abre `index.html` en el navegador (sin servidor). O:
  ```bash
  cd laboratorio
  python -m http.server 8003   # http://localhost:8003
  ```
- Funciona con mouse y con gestos táctiles (celular/tablet).

## Nota sobre las fórmulas

El repo renderiza fórmulas como PNG porque **la terminal** no muestra LaTeX. Aquí no
hace falta: es una página web, así que las fórmulas van como texto matemático que el
navegador sí muestra bien.

## Bloque 2 · Dos variables (`bloque-2.html`)

Mismo motor, nubes 2D que arrastras. Enlazado desde el Bloque 1 (botón arriba).

| # | Lente | Imagen-de-sistema | Qué manipulas |
|---|-------|-------------------|----------------|
| 1 | Covarianza | rectángulos firmados desde el centro | arrastras un punto de cuadrante → su rectángulo cambia de signo |
| 2 | Varianza vs Covarianza | cuadrado (X·X) vs rectángulo (X·Y) | toggle «X contra sí misma» → la nube colapsa a la diagonal y salen cuadrados (Var=Cov(X,X)) |
| 3 | Pearson | covarianza normalizada | arrastras puntos → Cov se dispara pero r se queda en [−1,+1] |
| 4 | Pearson como ángulo | dos vectores de desviaciones | giras el ángulo θ → r=cos θ y la nube se aprieta/abre/refleja |
| 5 | Escala y unidades | nube bajo transformación | sliders a·Y+b → Cov se estira, Pearson no; a<0 voltea el signo |

Progreso independiente del Bloque 1 (otra clave de `localStorage`).

## Gimnasio Simbólico (`gimnasio-simbolico.html`)

Complemento distinto: los laboratorios entrenan la **intuición** (ver el sistema);
el gimnasio entrena el **músculo simbólico** (leer la fórmula como partitura). Cada
ejercicio sigue el protocolo: traducir → sustituir → resultado → interpretar.

10 bloques con autocorrección:

1. Leer y expandir símbolos (∑ como «hazlo para todos y súmalo»)
2. Media, desviaciones, varianza (X=2,4,10)
3. Media vs mediana (X=2,4,5,100)
4. Z-score (μ=100, σ=15)
5. Covarianza (rectángulos firmados)
6. Pearson
7. Relación negativa (r=−1)
8. Cambio de escala (Cov se estira, Pearson no)
9. Área y probabilidad (uniforme)
10. Normal y regla 68-95-99.7

Más dos secciones de referencia: **🔧 Desarme** (clicas cada pieza de varianza /
z / Pearson y ves qué hace y en qué unidades queda) y **📓 Cuaderno** (tabla
símbolo → traducción → imagen). Numéricos: auto-check con tolerancia. Traducciones:
escribes, revelas la canónica y te auto-marcas. Progreso en `localStorage`.
