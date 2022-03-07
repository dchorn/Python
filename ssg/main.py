#! /usr/bin/env python3

"""
SSG v09
- Some refactorings to make it easier to understand.
- Easier debugging:   https://github.com/microsoft/debugpy/issues/258
- Also for debugging: import pprint; pprint.pp()
"""

from pathlib import Path
from typing import Iterator

import shutil
# import sys

import cmdline
import engine


# -----------------------------------------------------------------------------
def main(input_dir: Path, output_dir: Path) -> None:
    """Reads a markdown file and writes its html conversion."""

    # Creates output directory, if it doesn't exist
    output_dir.mkdir(exist_ok=True)

    # Get the list of all markdown files
    markdown_dir:           Path = input_dir/"md"
    markdown_filepath_iter: Iterator[Path] = markdown_dir.glob("*.md")
    markdown_filepath_list: list[Path] = sorted(
        markdown_filepath_iter, reverse=True)
    markdown_filenames: list[Path] = [
        filename.stem for filename in markdown_filepath_list if filename.is_file()]

    # Read all MarkDown (md) files and convert their contents to html and metadata
    md_str_list:   list[str] = [path.read_text()
                                for path in markdown_filepath_list]
    html_str_list: list[str] = [
        engine.convert_md_to_html(md_str) for md_str in md_str_list]
    metadata_list: list[dict] = [
        engine.get_md_metadata(md_str) for md_str in md_str_list]

    # Fill template with entries (html, metadata)
    template_dir:      Path = input_dir/"html"
    template_filename: str = "template.html"

    counter: int = 0

    # Loops trought each pair and creates each file.
    for (html, meta) in zip(html_str_list, metadata_list):
        vars_dict: dict = {"html_list": html, "meta_list": meta}
        html_str: str = engine.fill_template(
            template_dir, template_filename, vars_dict)
        filename: str = f"{markdown_filenames[counter]}.html"
        (output_dir / filename).write_text(html_str)
        counter += 1

    # Copy all resource dirs to output_path
    shutil.copytree(input_dir/"css", output_dir/"css", dirs_exist_ok=True)
    shutil.copytree(input_dir/"img", output_dir/"img", dirs_exist_ok=True)
    #  shutil.copytree(input_dir/"js",  output_dir/"js",  dirs_exist_ok=True)


# -----------------------------------------------------------------------------
if __name__ == "__main__":

    #  args: list[str] = sys.argv                       # For command-line
    #  args: list[str] = [sys.argv[0], "input", "output"] # For easy testing
    args = cmdline.parse_args()

    input_dir, output_dir = args.inputDir, args.outputDir

    main(input_dir, output_dir)

# -----------------------------------------------------------------------------
