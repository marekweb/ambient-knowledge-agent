#!/usr/bin/env python3
"""
smiles_to_image.py

Generate a PNG image of a molecule from a SMILES string.

Usage
-----
uv run smiles_to_image.py "Cc1ccccc1" toluene.png
"""

import sys
from pathlib import Path

try:
    from rdkit import Chem
    from rdkit.Chem import Draw
except ImportError as e:  # pragma: no cover
    sys.exit(
        "wrong"
    )


def main() -> None:
    # --- basic argument handling -------------------------------------------------
    if len(sys.argv) != 3:
        sys.exit(
            "Usage: smiles_to_image.py <SMILES-string> <output-file.png>\n"
            'Example: uv run smiles_to_image.py "Cc1ccccc1" toluene.png'
        )

    smiles, out_path_str = sys.argv[1:]
    out_path = Path(out_path_str)

    # --- build molecule ----------------------------------------------------------
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        sys.exit(f"Error: '{smiles}' is not a valid SMILES string.")

    # --- draw and save -----------------------------------------------------------
    try:
        # 300×300 px is a reasonable default; tweak if desired
        Draw.MolToFile(mol, str(out_path), size=(300, 300))
    except Exception as e:  # pragma: no cover
        sys.exit(f"Failed to write PNG: {e}")

    print(f"PNG written to {out_path.resolve()}")


if __name__ == "__main__":
    main()
