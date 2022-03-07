#! /usr/bin/env python3
# Made by Denys Chorny - @ dechorn

# Calculate and print subdirectory size

"""
Exercici 1:

- Fes un programa que calculi quant ocupa un arbre a disc.
- El programa només rep un paràmetre: un directori 'dir'.
- El programa ha de llistar dir i tots els seus subdirectoris recursivament.
- Per cada directori, ha de mostrar el seu tamany.
- El tamany d'un directori és la suma de tots els arxius que conté recursivament.
- Mostra el resultat en bytes.
- Els directoris han d'estar llistat per tamany, de menor a major.
- El programa ha de rebre el directori 'dir' des de la línia d'ordres.
- **Poseu el vostre nom i número d'exercici al principi del vostre codi.**

"""

from pathlib import Path
import sys
from os import stat_result

# ======================================================================================


def sum_dir(filepath: list[Path]):
    for path in filepath:
        print(f"{path.parent} = {path.stat().st_size} bytes")
    return


# ======================================================================================


def get_total_size_dir(filepath_list: list[Path]) -> int:

    print(filepath_list)
    stat_list: list[stat_result] = [filepath.stat() for filepath in filepath_list]
    size_list: list[int] = [stat.st_size for stat in stat_list]
    total_size: int = sum(size_list)
    return total_size


def get_total_size(filepath_list: list[Path]) -> int:

    stat_list: list[stat_result] = [filepath.stat() for filepath in filepath_list]
    size_list: list[int] = [stat.st_size for stat in stat_list]
    total_size: int = sum(size_list)
    return total_size


# ======================================================================================


def get_filepath_list(dir: str, pattern: str):
    dirpath: Path = Path(dir)
    path_list: list[Path] = list(dirpath.rglob(pattern))
    filepath_list: list[Path()] = [path for path in path_list if path.is_file]
    return filepath_list


# ======================================================================================


def print_dir_size(dir: str, pattern: str) -> None:

    filepath_list: list[Path] = get_filepath_list(dir, pattern)
    total_size: int = get_total_size(filepath_list)
    sum_dir(filepath_list)

    print(f"Total size: {total_size} bytes")


# ======================================================================================


def parse_command_line(command_line: list[str]) -> tuple[str, str]:

    # Separate program name from program parameters
    program_name: str = command_line[0]
    program_parameters: list[str] = command_line[1:]

    # Make sure we have two parameters
    assert len(program_parameters) == 2

    # List deconstruction
    dir, pattern = program_parameters

    return dir, pattern


# ======================================================================================
#                                    MAIN

if __name__ == "__main__":
    dir, pattern = parse_command_line(sys.argv)
    print_dir_size(dir, pattern)

# ======================================================================================
