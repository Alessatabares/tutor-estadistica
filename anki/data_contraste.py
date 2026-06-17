# -*- coding: utf-8 -*-
"""Carga CONTRASTE (Capa 2) desde los modulos en _parts/.

Cada _parts/<slug>.py puede definir CONTRASTES (list de (tema, planteamiento, resolucion)).
Si un modulo no la define, se omite.
"""
import os
import importlib.util

PARTS_DIR = os.path.join(os.path.dirname(__file__), "_parts")

CONTRASTE = {}
for fn in sorted(os.listdir(PARTS_DIR)):
    if not fn.endswith(".py") or fn.startswith("_"):
        continue
    spec = importlib.util.spec_from_file_location(fn[:-3], os.path.join(PARTS_DIR, fn))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    contrastes = getattr(mod, "CONTRASTES", None)
    if contrastes:
        CONTRASTE[mod.NAME] = {"contrastes": contrastes}
