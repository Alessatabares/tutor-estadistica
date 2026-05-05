#!/usr/bin/env python3
"""
Renderiza fórmulas LaTeX a PNG usando matplotlib.mathtext.

Acepta una o varias líneas LaTeX (separadas por '||'). Útil para fórmulas
con casos cuando \\begin{cases} no está disponible en mathtext.

Uso:
    python3 bin/render_formula.py "<latex>" <output_path> [opciones]

Opciones:
    --fontsize N   Tamaño de la fórmula (default 28).
    --label "..."  Pie de fórmula (italic, gris).

Ejemplo:
    python3 bin/render_formula.py "\\bar{x} = \\frac{1}{N}\\sum_{i=1}^{N} x_i" \\
        progreso/imagenes-formulas/media.png \\
        --label "Media: el reparto que conserva el total"

Para varias líneas, separá con '||':
    python3 bin/render_formula.py \\
        "x_{((N+1)/2)} \\;\\;\\text{si N impar}||\\dfrac{x_{(N/2)} + x_{(N/2+1)}}{2} \\;\\;\\text{si N par}" \\
        progreso/imagenes-formulas/mediana.png
"""
import argparse
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def render(latex: str, output: Path, fontsize: int = 28, label: str | None = None) -> None:
    lines = [l.strip() for l in latex.split("||") if l.strip()]
    n_lines = len(lines)

    base_height = 1.4 + 0.9 * (n_lines - 1)
    if label:
        base_height += 0.8
    fig, ax = plt.subplots(figsize=(8, base_height), dpi=180)
    ax.axis("off")
    fig.patch.set_facecolor("white")

    if label:
        formula_top = 0.88
        formula_bottom = 0.42
        label_y = 0.10
    else:
        formula_top = 0.92
        formula_bottom = 0.08
        label_y = None

    if n_lines == 1:
        ys = [(formula_top + formula_bottom) / 2]
    else:
        step = (formula_top - formula_bottom) / (n_lines - 1)
        ys = [formula_top - i * step for i in range(n_lines)]

    for y, line in zip(ys, lines):
        ax.text(
            0.5, y, f"${line}$",
            ha="center", va="center",
            fontsize=fontsize, color="#111111",
        )

    if label:
        ax.text(
            0.5, label_y, label,
            ha="center", va="center",
            fontsize=14, color="#555555", style="italic",
        )

    output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output, bbox_inches="tight", pad_inches=0.25, facecolor="white")
    plt.close(fig)


def main() -> int:
    parser = argparse.ArgumentParser(description="Renderiza LaTeX a PNG.")
    parser.add_argument("latex", help="Cadena LaTeX (sin $). Usá '||' para separar líneas.")
    parser.add_argument("output", type=Path, help="Ruta del PNG de salida.")
    parser.add_argument("--fontsize", type=int, default=28)
    parser.add_argument("--label", default=None, help="Pie de fórmula opcional.")
    args = parser.parse_args()

    render(args.latex, args.output, fontsize=args.fontsize, label=args.label)
    print(args.output)
    return 0


if __name__ == "__main__":
    sys.exit(main())
