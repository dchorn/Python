"""
Exercici 4:

- Fes un programa que llegeixi l'arxiu .csv de dades covid
  i retorni un diccionari de la següent forma:
  - Les claus són els noms de les columnes.
  - Els valors són les columnes de la taula, en forma de llistes.
"""

from pathlib import Path
import pprint as pp


# -----------------------------------------------------------------------------
def csv_to_text(csv_path: Path) -> str:
    csv_text:     str = csv_path.read_text()
    striped_text: str = csv_text.strip()
    return striped_text


# -----------------------------------------------------------------------------
def csv_text_to_list(csv_text: str) -> list[str]:
    csv_list: list[str] = csv_text.split("\n")
    return csv_list

def csv_list_to_table(csv_list: list[str]) -> list[list[str]]:
    buffer: list[str]       = []
    table:  list[list[str]] = []
    for row in csv_list[1:]:
        buffer = row.split(";")
        table.append(buffer)
    return table

def get_header(csv_list: list[str]) -> list[str]:
    header: list[str] = csv_list[0].split(";")
    return header

def create_dictionary(header: list[str], table: list[list[str]]) -> dict:
    csv_dict: dict = {}
    for cols in header:
        csv_dict[cols] = ""

    return csv_dict

# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    csv_path: Path            = Path("covid-dades-simple.csv")
    csv_text: str             = csv_to_text(csv_path)
    csv_list: list[str]       = csv_text_to_list(csv_text)
    header:   list[str]       = get_header(csv_list)
    table:    list[list[str]] = csv_list_to_table(csv_list)
    csv_dict: dict            = create_dictionary(header, table)
    # print(csv_dict)

# -----------------------------------------------------------------------------