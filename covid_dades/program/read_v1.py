"""Program to read csv's"""
# Suma total de los vacunados con la primera dosis y suma de todos los vacunados con la segunda

from pathlib import Path
import time

text: str = Path("csv/covid-dades-aga.csv").read_text()


def text_to_row(text: str) -> list[str]:
    rows: list[str] = []
    rows = text.splitlines()
    return rows


def rows_to_table(rows: list[str]) -> list[list[str]]:
    buffer: list[str] = []
    table: list[list[str]] = []

    for row in rows:
        buffer = row.split(";")
        table.append(buffer)
    return table


def sum_vacuna(table: list[list[str]], position: int) -> int:
    result: int = 0
    for i in range(len(table)):
        # print(table[i])
        if "BARCELONA" in table[i][0]:
            result = result + int(table[i][position])

    return result

def absolute_dif(first_number: int, second_number: int) -> int:
    result: int = 0
    result_persentage: float = 0

    if first_number > second_number:
        result = first_number - second_number
    else:
        result = second_number - first_number

    result_persentage = (result * 100) / first_number
    return(result, result_persentage)

def main():
    start: float = time.time()

    rows: list[str] = text_to_row(text)
    table: list[list[str]] = rows_to_table(rows)
    sum_vacuna_1: int = sum_vacuna(table, 20)
    sum_vacuna_2: int = sum_vacuna(table, 21)

    stop: float = time.time()

    print(f"Tiempo Ejecucion: {stop-start}")

    print("============================================")
    print(f"Suma de Primera Vacuna: {sum_vacuna_1}")
    print(f"Suma de Segunda Vacuna: {sum_vacuna_2}")
    print(f"Suma Total de Vacunats:", sum_vacuna_2 + sum_vacuna_1)
    print("============================================")

    print(f"Diferencia Absoluta: ", absolute_dif(sum_vacuna_1, sum_vacuna_2)[0])
    print(f"Diferencia Absoluta en Porcentaje: ", round(absolute_dif(sum_vacuna_1, sum_vacuna_2)[1], 2),"%")
    print("============================================")

if __name__ == "__main__":
    main()