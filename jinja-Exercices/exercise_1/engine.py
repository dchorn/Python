#! /usr/bin/env python3
#  Made by Denys Chorny - @dchorn
"""
Engine module: Uses Text and Jinja to put content on templates.
"""

from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape
from jinja2.environment import Template

# -----------------------------------------------------------------------------
# Jinja functions
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
def fill_template(template_dir: Path, template_filename: str, vars_dict: dict) -> str:
    """ Reads the template and fills it with the contents.
        - template_dir: A directory path relative to main_module_name.
        - template_filename: Template file to fill.
        - contents: Contents to put in the template.
        Keeping the template_dir and filename separate allows template inheritance.
        Autoescapes by default.
        Returns the result as a string."""

    env: Environment = Environment(
        loader=FileSystemLoader(template_dir), autoescape=select_autoescape()
    )
    template: Template = env.get_template(template_filename)
    filled_str: str = template.render(vars_dict)
    return filled_str


# -----------------------------------------------------------------------------
