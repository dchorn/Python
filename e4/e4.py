# Denys Chorny, examen de recuperació: Ejercicio 4

"""
Exercici 4:

- Fes un programa que llegeixi les dades covid del fitxer adjunt i calculi el següent:
- Ranking d'àrees (NOM) per número de morts (EXITUS).
- Primer mostrar les àrees amb més morts i al final les de menys morts.
- El programa només rep un paràmetre: el nom del fitxer .csv amb les dades covid.
- El programa ha de rebre el nom del fitxer des de la línia d'ordres.
- **Poseu el vostre nom i número d'exercici al principi del vostre codi.**

Pasos recomanats:
1. Filtrar per nom d'àrea
2. Sumar els morts d'una àrea
3. Llistar les àrees úniques
4. Per cada àrea calcular la suma total de morts
5. Ordenar àrees pel total de morts
6. Llegir csv per la línea d'ordres
"""

import sys
import table

# ======================================================================================


def remove_duplicate_rows(table: list[str]) -> list[str]:
    """Remove duplicate rows from a table"""
    deduplicated_list = list()
    for item in table:
        if item not in deduplicated_list:
            deduplicated_list.append(item)
    return deduplicated_list


# ======================================================================================


def parse_command_line(command_line: list[str]) -> int:
    """Parse argv from the command line to programm"""

    program_name: str = command_line[0]
    program_parameters: list[str] = command_line[1:]

    assert len(program_parameters) == 1

    dir = program_parameters[0]

    return dir


# ======================================================================================


def sum_exitus(merged_list_name_exitus, nom, city) -> int:
    """Sum all exitus from a certain city"""
    suma = 0
    for num in table.filter_rows(merged_list_name_exitus, nom, city):
        suma = suma + int(num[1])
    return suma


# ======================================================================================


def sortby(x):
    """Sort the list by int using the secont list in the list[list[xxx]]"""
    try:
        return int(x[1])
    except ValueError:
        return float("esto no funciona u.u")


# ======================================================================================


def merge_lists(first_list, second_list) -> list[list[str]]:
    """merge two list[list[xxx]] into a new one"""
    buffer = []
    for i in range(len(first_list)):
        new_list = [first_list[i], second_list[i]]
        buffer.append(new_list)
    return buffer


# ======================================================================================


def pretty_print(sorted_list: list[list[str]]):
    """print the result"""
    for i in range(len(sorted_list)):
        print(f"{sorted_list[i][0]}: {sorted_list[i][1]}")


# ======================================================================================


def get_sorted_list(list_to_sort, merged_list_name_exitus, row_name, nom):
    """supuestamente deberia de sortearme las listas"""
    result = sorted(
        list_to_sort,
        key=lambda suma: sum_exitus(merged_list_name_exitus, row_name, nom),
    )
    return result


# ======================================================================================
#                                    MAIN
def main(csv_dir: str):
    """Donde ocurre la magia del programa"""
    nom: str = "NOM"
    exitus: str = "EXITUS"
    header: list[str] = [nom, exitus]
    covid_table: list[list[str]] = table.read_table(csv_dir)

    name_column: list[str] = table.get_column(covid_table, nom)
    exitusumn: list[int] = table.get_column(covid_table, exitus)
    deduplicated_list: list[str] = remove_duplicate_rows(name_column)
    deduplicated_list.pop(0)

    merged_list_name_exitus = merge_lists(name_column, exitusumn)

    sum_list = []
    for city in deduplicated_list:
        sum_list.append(sum_exitus(merged_list_name_exitus, nom, city))

    sorted_list = merge_lists(deduplicated_list, sum_list)
    sorted_list.sort(key=sortby, reverse=True)
    pretty_print(sorted_list)


if __name__ == "__main__":
    """Take argvs from the command line"""
    csv_dir: str = parse_command_line(sys.argv)
    main(csv_dir)

# ======================================================================================
