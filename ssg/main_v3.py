#! /usr/bin/env python3
# Made by Denys Chorny - @ dechorn

from   pathlib import Path
from   typing  import Iterator

import shutil
import sys

import cmdline
import engine

import pprint as pp

# -----------------------------------------------------------------------------

def main(input_dir: Path, output_dir: Path) -> None:
    """Reads a markdown file and writes its html conversion."""

    markdown_dir:           Path           = input_dir/"md"
    markdown_filepath_iter: Iterator[Path] = markdown_dir.glob("*.md")
    markdown_filepath_list: list[Path]     = sorted(markdown_filepath_iter, reverse=True)

    # Read all MarkDown (md) files and convert their contents to html and metadata
    md_str_list:   list[str]  = [path.read_text() for path in markdown_filepath_list]
    html_str_list: list[str]  = [engine.convert_md_to_html(md_str) for md_str in md_str_list]
    metadata_list: list[dict] = [engine.get_md_metadata(md_str)    for md_str in md_str_list]

    # Fill template with entries (html, metadata)
    template_dir:      Path = input_dir/"html"
    template_filename: str  = "template.html"

    counter: int = 1

    for (html, meta) in zip(html_str_list, metadata_list):
        vars_dict:         dict = {"html_list": html, "meta_list": meta}
        html_str:          str  = engine.fill_template(template_dir, template_filename, vars_dict)
        filename: str  = f"Archivo_{counter}.html"
        (output_dir/filename).write_text(html_str)
        counter += 1;
    # vars_dict:         dict = {"entry_list": zip(html_str_list, metadata_list)}










# -----------------------------------------------------------------------------
if __name__ == "__main__":

    #  args: list[str] = sys.argv                       # For command-line
    args: list[str] = [sys.argv[0], "input", "output"] # For easy testing

    input_dir, output_dir = cmdline.parse_args(args)

    main(input_dir, output_dir)

# -----------------------------------------------------------------------------
