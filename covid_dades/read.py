"""Program to read csv's"""
#Suma total de los vacunados con la primera dosis y suma de todos los vacunados con la segunda dosis

from pathlib import Path

text: str = Path("csv/covid-dades-simple.csv").read_text()

def text_to_row(text: str) -> list[str]:
    rows: list[str] = []
    rows = text.splitlines()
    return(rows)

def rows_to_table(rows: list[str]) -> list[list[str]]:
    buffer: list[str] = []
    table: list[list[str]] = []

    for row in rows:
        buffer = row.split(";")
        table.append(buffer)
    return(table)

rows: list[str] = text_to_row(text)
table: list[list[str]] = rows_to_table(rows)
