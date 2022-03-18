
from pathlib import Path
import pprint as pp



def get_recursive_filepath_list_v1(dirpath: Path) -> list[Path]:
    path_list:     list[Path] = list(dirpath.rglob('*'))
    file_list:     list[Path] = []

    for path in path_list:
        get_recursive_filepath_list(path)
        if path.is_file():
            file_list.append(path)
    return file_list


def get_recursive_filepath_list_v2(dirpath: Path) -> list[Path]:
    path_list:     list[Path] = list(dirpath.glob('*'))
    file_list:     list[Path] = []

    for path in path_list:
        if(dirpath.is_dir()):
            get_recursive_filepath_list_v2(path)
        elif(dirpath.is_file()):
            print(path)

    # for path in path_list:
    #     get_recursive_filepath_list(path)
    #     if path.is_file():
    #         file_list.append(path)
    # return file_list


def main():
    dirpath: Path = Path("my data")
    filepath_list: list[Path] = []
    # filepath_list = get_recursive_filepath_list_v1(dirpath)

    pp.pp(filepath_list)


if __name__ == "__main__":

    # Execution from terminal
    main()