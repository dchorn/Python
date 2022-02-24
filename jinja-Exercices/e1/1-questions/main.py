#! /usr/bin/env python3

"""
SSG v09
- Some refactorings to make it easier to understand.
- Easier debugging:   https://github.com/microsoft/debugpy/issues/258
- Also for debugging: import pprint; pprint.pp()
"""

from   pathlib import Path
from   typing  import Iterator

import shutil
import sys

import engine

from jinja2             import Environment, FileSystemLoader, select_autoescape
from jinja2.environment import Template

import pprint as pp

input_text: str = Path("/home/dech/Github/Python/16-exercises/e1/1-questions/input/friends.txt").read_text()

def text_to_list(text: str) -> list[str]:
    """get the file and convert it into a list"""
    text_list: list[str] = []
    text_list = text.splitlines()
    return text_list

def check_space(text: list[str]) -> list[str]:
    """Removes blanc fields in the list"""
    if text[-1] == '':
        text.pop(-1)
    return text

def main() -> None:
    """Reads a txt file and changes another one with text from the first one."""

    text_list: list[str] = text_to_list(input_text)
    friends            = check_space(text_list)


    for i in range(len(friends)):
        file_loader = FileSystemLoader("/home/dech/Github/Python/16-exercises/e1/1-questions/input/template")
        env = Environment(loader=file_loader)
        template = env.get_template("letter.txt")
        output = template.render(friends=friends[i])
        print(output)


# -----------------------------------------------------------------------------
if __name__ == "__main__":
    main()

# -----------------------------------------------------------------------------