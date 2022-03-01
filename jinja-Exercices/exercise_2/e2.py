#! /usr/bin/env python3
# Made by Denys Chorny - @ dechorn

"""
Exercici 2:

- Fes un programa que renombri una llista d'arxius.
- Heu de vigilar que no es produeixin errors.

- Inputs:
  - La llista d'arxius.
  - Un string a cercar.
  - Un string de substitució.

- Exemple:
  - Llista d'arxius: ['a1.txt', 'a2.txt', 'a3.txt']
  - String de cerca: 'a'
  - String de substitució: 'b'
  - Resultat: ['b1.txt', 'b2.txt', 'b3.txt']

- Exemple d'error:
  - Llista d'arxius: ['a1.txt', 'a2.txt', 'b1.txt']
  - String de cerca: 'a'
  - String de substitució: 'b'
  - Resultat: El programa ha d'abortar avisant que b1.txt es sobreescriuria.

- Notes:
  - Utilitzeu el directori 2-test-files per fer proves.
"""

from pathlib import Path

def rename_filename_list(old_filename_list: list[str], old_str: str, new_str: str) -> list[str]:
    """Change values from a list"""
    new_filename_list: list[str] = [filename.replace(old_str, new_str) for filename in old_filename_list]
    return new_filename_list

def rename_files(glob: str, old_str: str, new_str: str):
    """Rename files"""
    glob_dir: Path = Path(glob)
    dir:      Path = glob_dir.parent
    pattern:  Path = glob_dir.name

    old_filename_list: list[str] = [filepath.name for filepath in dir.glob(pattern)]
    new_filename_list: list[str] = rename_filename_list(old_filename_list, old_str, new_str)
    print(old_filename_list)
    print(new_filename_list)

def main():
    rename_files("2-test-files/*.txt", "a", "b")


if __name__ == "__main__":
    main()
