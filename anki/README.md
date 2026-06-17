# Anki — Estadística y Probabilidad

Decks para memorizar los **conceptos e infraestructuras indispensables** de
probabilidad y estadística, como capa de retención sobre el tutor socrático.
Construidos con la metodología de los *ejes diagnósticos* de `examen-ecoe-anki`:
cada concepto se indexa por **dos ejes complementarios**.

## Los dos ejes

| Eje | Dirección de recall | Para qué |
|---|---|---|
| **Eje Clínico** | del **problema** → al concepto que lo resuelve | construir el **mapa**: "tengo esta pregunta, ¿qué herramienta la responde?" |
| **Integrador** | de las **señales** → al concepto + cómo verbalizarlo | **dominio**: reconocer un concepto por sus rasgos y saber explicarlo |

El campo *"Dilo así"* del Integrador lleva la verbalización y, cuando aplica, la
**convergencia** (el hilo asociativo): la varianza viajando de capa en capa, el TLC
como bisagra, SD≠SE, la tabla 2×2 como nodo. Así la red conceptual vive dentro de las cartas.

## Estructura

```
anki/
├── _parts/                 # FUENTE ÚNICA de contenido (editar aquí)
│   ├── probabilidad.py     # NAME, EJES (eje clínico), ESTACIONES (integrador)
│   ├── descriptiva.py
│   └── inferencial.py
├── data_eje_clinico.py     # loader: importa _parts, extrae EJES
├── data_integrador.py      # loader: importa _parts, extrae ESTACIONES
├── build/
│   ├── _common.py          # registro de áreas + esquema de deck_id + modelo
│   ├── build_eje_clinico.py
│   └── build_integrador.py
└── output/                 # los .apkg generados (importar en Anki)
```

Árbol de decks en Anki: `Estadistica::<Área>::Eje Clinico` y `::Integrador`.

## Regenerar

```bash
source ../.venv/bin/activate    # genanki instalado aquí
python build/build_eje_clinico.py
python build/build_integrador.py
```

## Reglas de diseño (heredadas de la metodología ECOE)

- **Datos separados del render:** el contenido vive en `_parts/`; los builders solo pintan HTML.
- **GUID estable por posición** (`estad:ec:<area>:<i>`): corregir un texto y reimportar
  **actualiza** la carta en su sitio, nunca la duplica.
- **deck_id determinista** (`1600_AA_C`): sin colisión con otros repos de Anki.
- Usar entidades HTML (`&lt;` `&gt;`) para `<` y `>` dentro del texto (p. ej. `p &lt; 0.05`).

Total actual: **41 tarjetas** (13 Eje Clínico + 28 Integrador).
