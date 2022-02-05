from pathlib import Path

csv_text: str = Path("csv/covid-dades-aga.csv").read_text()

def text_into_rows(csv_text: str) -> list[str]:
    rows: list[str] = []
    rows = csv_text.splitlines()
    return(rows)

def rows_to_table(rows: list[str]) -> list[list[str]]:
    buffer: list[str] = []
    table: list[list[str]] = []

    for row in rows:
        buffer = row.split(";")
        table.append(buffer)
    return(table)

def table_to_dictionary(table: list[list[str]]) -> dict:
    dictionary_list: dict = {}
    dictionary_table: list[dict[str, str]] = []
    header: list[str] = table[0]
    table.pop(0)

    for i, _j in enumerate(table):
        dictionary_table.append(dict(zip(header, table[i])))

    return(dictionary_table)

def sum_vacuna(dictionary_table: list[dict[str,str]], position: str, city: str) -> int:
    result : int = 0
    for i, _j in enumerate(dictionary_table):
        if city in dictionary_table[i]["NOM"]:
            result = result + int(dictionary_table[i][position])
    return(result)

def absolute_dif(first_number: int, second_number: int) -> tuple:
    """Calculates the absolute diference"""
    result: int = 0
    result_persentage: float = 0

    if first_number > second_number:
        result = first_number - second_number
    else:
        result = second_number - first_number

    result_persentage = (result * 100) / first_number
    return (result, result_persentage)

def main():
    rows: list[str] = text_into_rows(csv_text)
    table: list[list[str]] = rows_to_table(rows)
    dictionary_list: dict = table_to_dictionary(table)

    sum_vacuna_1: int = sum_vacuna(dictionary_list, "VACUNATS_DOSI_1", "BARCELONA")
    sum_vacuna_2: int = sum_vacuna(dictionary_list, "VACUNATS_DOSI_2", "BARCELONA")
    absolute_difference: int = absolute_dif(sum_vacuna_1, sum_vacuna_2)[0]
    absolute_percentage: float = round(absolute_dif(sum_vacuna_1, sum_vacuna_2)[1], 2)

    print("============================================")
    print(f"Suma de Primera Vacuna: {sum_vacuna_1}")
    print(f"Suma de Segunda Vacuna: {sum_vacuna_2}")
    print(f"Suma Total de Vacunats: {sum_vacuna_2 + sum_vacuna_1}")
    print("============================================")

    print(f"Diferencia Absoluta: {absolute_difference}")
    print(f"Diferencia Absoluta en Porcentaje: {absolute_percentage}%")
    print("============================================")

if __name__ == "__main__":
    main()
