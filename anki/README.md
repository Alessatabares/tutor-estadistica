# Anki — Estadística y Probabilidad

Decks para memorizar los **conceptos e infraestructuras indispensables** de
probabilidad y estadística, como capa de retención sobre el tutor socrático.
Construidos con la metodología de los *ejes diagnósticos* de `examen-ecoe-anki`:
cada concepto se indexa por **dos ejes complementarios**.

## Arquitectura por capas

Sigue la progresión del método del tutor (`CLAUDE.md`): *intuición pura → uso y fallos → formalización*.

| Capa | Entrena | Tipo de carta | Estado |
|---|---|---|---|
| **1 · Reconocer + mapear** | qué es / para qué / cómo lo explico | **Eje Clínico** (problema→concepto) + **Integrador** (señales→concepto+"Dilo así") | ✅ |
| **2 · Discriminar** | concepto cercano + supuestos / dónde falla | **Contraste** ("¿cuál de los dos, cuándo, y por qué NO el otro?") | ✅ |
| **3 · Formalizar** | la fórmula y leer el número | cloze con fórmula PNG (`bin/render_formula.py`) + "¿qué pasa si cambio n?" | ⏳ pendiente |

**Capa 1 — los dos ejes:**
- **Eje Clínico**: del **problema** → al concepto que lo resuelve (construir el mapa).
- **Integrador**: de las **señales** → al concepto + verbalización. El campo *"Dilo así"* lleva
  la verbalización y, cuando aplica, la **convergencia** (varianza viajando de capa en capa, el TLC
  como bisagra, SD≠SE, la tabla 2×2 como nodo). La red conceptual vive dentro de las cartas.

**Capa 2 — Contraste:** ataca la zona de trampas (donde viven la mitad de los errores de
investigación): media vs mediana, Pearson vs Spearman, error tipo I vs II, qué ES y qué NO es el
valor p, t vs Mann-Whitney, efectos fijos vs aleatorios, significancia vs relevancia.

## Estructura

```
anki/
├── _parts/                 # FUENTE ÚNICA de contenido (editar aquí)
│   ├── probabilidad.py     # NAME, EJES (eje clínico), ESTACIONES (integrador)
│   ├── descriptiva.py
│   └── inferencial.py
├── data_eje_clinico.py     # loader: extrae EJES        (Capa 1)
├── data_integrador.py      # loader: extrae ESTACIONES   (Capa 1)
├── data_contraste.py       # loader: extrae CONTRASTES    (Capa 2)
├── build/
│   ├── _common.py          # registro de áreas + esquema de deck_id + modelo
│   ├── build_eje_clinico.py
│   ├── build_integrador.py
│   └── build_contraste.py
└── output/                 # los .apkg generados (importar en Anki)
```

Árbol de decks en Anki: `Estadistica::<Área>::{Eje Clinico | Integrador | Contraste}`.
Cada `_parts/<area>.py` define `EJES`, `ESTACIONES` y `CONTRASTES`.

## Regenerar

```bash
source ../.venv/bin/activate    # genanki instalado aquí
python build/build_eje_clinico.py
python build/build_integrador.py
python build/build_contraste.py
```

## Reglas de diseño (heredadas de la metodología ECOE)

- **Datos separados del render:** el contenido vive en `_parts/`; los builders solo pintan HTML.
- **GUID estable por posición** (`estad:ec:<area>:<i>`): corregir un texto y reimportar
  **actualiza** la carta en su sitio, nunca la duplica.
- **deck_id determinista** (`1600_AA_C`): sin colisión con otros repos de Anki.
- Usar entidades HTML (`&lt;` `&gt;`) para `<` y `>` dentro del texto (p. ej. `p &lt; 0.05`).
- `deck_id(idx, fmt)`: fmt 1 = Eje Clínico, 2 = Integrador, 3 = Contraste.

Total actual: **59 tarjetas** — Capa 1: 41 (13 Eje Clínico + 28 Integrador) · Capa 2: 18 Contraste.
