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

# ======================================================================================


def get_dirpath_size(dirpath: Path) -> int:

    filepath_list: list[Path] = get_filepath_list(dirpath)
    size: int = get_filepath_list_size(filepath_list)

    return size


# ======================================================================================


def get_pretty_dirpath(dirpath: Path) -> str:

    dirname: str = str(dirpath)
    size: int = get_dirpath_size(dirpath)

    result: str = f"{dirname}: {size}"

    return result


# ======================================================================================


def get_filepath_list(dirpath: Path):
    path_list: list[Path] = list(dirpath.rglob("*"))
    filepath_list: list[Path] = [path for path in path_list if path.is_file()]
    return filepath_list


# ======================================================================================


def get_filepath_size(filepath: Path) -> int:
    size: int = filepath.stat().st_size
    return size


# ======================================================================================


def get_filepath_list_size(filepath_list: list[Path]) -> int:
    size_list: list[int] = [get_filepath_size(filepath) for filepath in filepath_list]
    total_size: int = sum(size_list)
    return total_size


# ======================================================================================


def get_sorted_dirpath_list(dirpath_list: list[Path]) -> list[Path]:

    result: list[Path] = sorted(
        dirpath_list, key=lambda dirpath: get_dirpath_size(dirpath)
    )
    return result


# ======================================================================================


def get_dirpath_list(dirpath: Path) -> list[Path]:
    path_list: list[Path] = list(dirpath.rglob("*"))
    dirpath_list: list[Path] = [path for path in path_list if path.is_dir()]
    dirpath_list.append(dirpath)

    return dirpath_list


# ======================================================================================


def print_tree(dir: str) -> None:
    dirpath: Path = Path(dir)
    dirpath_list: list[Path] = get_dirpath_list(dirpath)
    sorted_dirpath_list = get_sorted_dirpath_list(dirpath_list)

    for dirpath in sorted_dirpath_list:
        print(get_pretty_dirpath(dirpath))


# ======================================================================================


def parse_command_line(command_line: list[str]) -> str:

    # Separate program name from program parameters
    program_name: str = command_line[0]
    program_parameters: list[str] = command_line[1:]

    # Make sure we have two parameters
    assert len(program_parameters) == 1

    # List deconstruction
    dir = program_parameters[0]

    return dir


# ======================================================================================
#                                    MAIN

if __name__ == "__main__":
    dir = parse_command_line(sys.argv)
    print_tree(dir)

# ======================================================================================
