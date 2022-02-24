#! /usr/bin/env python3
#  Made by Denys Chorny - @dchorn
"""
Exercici 1:

- Fes un programa que enviï invitacions a una llista d'amics.
- Utilitza engine.py
- Utilitza els fitxers friends.txt i letter.txt
- Modifica letter.txt utilitzant Jinja.
"""

from pathlib import Path
import sys

import cmdline
import engine


def text_to_list(text: str) -> list[str]:
    """get the file and convert it into a list"""
    text_list: list[str] = []
    text_list = text.strip().splitlines()
    return text_list


def main(input_dir: Path, output_dir: Path) -> None:
    """Reads an imput file with friends names, output a text file with an invitation to every friend."""

    input_text: str = Path("input/friends.txt").read_text()
    friend_list: list[str] = text_to_list(input_text)

    template_dir: Path = input_dir / "templates"
    template_filename: str = "template.txt"

    for friend in friend_list:
        vars_dict: dict = {"friend": friend}
        text_str: str = engine.fill_template(template_dir, template_filename, vars_dict)
        output_invitation: str = Path(output_dir / f"{friend}.txt").write_text(text_str)


# -----------------------------------------------------------------------------
if __name__ == "__main__":

    # args: list[str] = sys.argv                       # For command-line
    args: list[str] = [sys.argv[0], "input", "output"]  # For easy testing

    input_dir, output_dir = cmdline.parse_args(args)

    main(input_dir, output_dir)

# -----------------------------------------------------------------------------
