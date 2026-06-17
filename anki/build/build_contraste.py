"""Builder de los decks CONTRASTE (Capa 2: discriminacion + supuestos/fallos).

Front: dos conceptos cercanos o un escenario de eleccion + la pregunta discriminadora.
Back:  la regla que los separa y donde falla cada uno.
Lee data_contraste.CONTRASTE y emite un .apkg por area presente.
"""
import os
import sys
import genanki

sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _common import MODEL_QA_ID, PADRE, AREAS, deck_id
from data_contraste import CONTRASTE

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

CSS = """
.card { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-size: 19px; text-align: left; color: #1a1a1a; background-color: #fafafa;
  padding: 20px; line-height: 1.55; }
.eje { display: inline-block; padding: 5px 14px; margin-bottom: 14px;
  background: #be123c; color: #fff; border-radius: 6px; font-size: 13px;
  letter-spacing: 0.6px; font-weight: 700; text-transform: uppercase; }
.plant { color: #1a1a1a; margin: 6px 0 4px 0; }
.prompt { color: #2563eb; font-weight: 600; margin-top: 8px; }
.reso { color: #047857; font-weight: 500; }
#extra { margin-top: 16px; border: none; border-top: 1px solid #d4d4d4; padding-top: 12px; }
"""

model_qa = genanki.Model(
    MODEL_QA_ID, "Estadistica QA",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[{"name": "QA", "qfmt": "{{Front}}",
                "afmt": '{{Front}}<hr id="extra">{{Back}}'}],
    css=CSS,
)


def make_note(tema, planteamiento, resolucion, base_tags, guid):
    front = (
        f'<div class="eje">CONTRASTE: {tema}</div>'
        f'<div class="plant">{planteamiento}</div>'
    )
    back = f'<div class="reso">{resolucion}</div>'
    # GUID estable por posicion (no por contenido): reimportar tras corregir
    # texto ACTUALIZA la carta en su sitio, nunca duplica.
    return genanki.Note(model=model_qa, fields=[front, back], tags=base_tags, guid=guid)


def build():
    total = 0
    for data_name, short, slug, tag, idx in AREAS:
        sysdata = CONTRASTE.get(data_name)
        if not sysdata:
            continue
        deck = genanki.Deck(deck_id(idx, 3), f"{PADRE}::{short}::Contraste")
        base_tags = ["estadistica", "contraste", "capa2", tag]
        for ci, (tema, plant, reso) in enumerate(sysdata["contrastes"]):
            guid = genanki.guid_for(f"estad:con:{idx}:{ci}")
            deck.add_note(make_note(tema, plant, reso, base_tags, guid))
        out = os.path.join(OUTPUT_DIR, f"Estadistica_{slug}_Contraste.apkg")
        genanki.Package(deck).write_to_file(out)
        print(f"OK: {os.path.basename(out)}  ({len(deck.notes)} notas)")
        total += 1
    print(f"--- {total} decks Contraste generados ---")


if __name__ == "__main__":
    build()
