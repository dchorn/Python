#! /usr/bin/env python3
# Made by Denys Chorny - @ dechorn
"""
Exercici 3:

- Fes un programa que calculi quant ocupa un arbre a disc.
- Mostra el resultat en bytes.
- Permet filtrar per un glob.
- Permet passar el glob per la línia d'ordres utilitzant sys.argv.

"""
from pathlib import Path

import cmdline
import sys

def list_tree(pattern: Path):
    return


def main():

    print(list(p.glob("**/*")))


if __name__ == "__main__":
    # args: list[str] = sys.argv         # For command-line
    args: list[str] = [sys.argv[0], "input"]  # For easy testing

    pattern = cmdline.parse_args(args)

    main()