"""
Commandline module: Parses command line arguments.
"""
from   pathlib import Path
import argparse

# -----------------------------------------------------------------------------
def parse_args(cmdline: list[str]) -> tuple[Path, Path]:
    """Parses the commandline. Must include executable path in [0], like sys.argv."""

    # Split command line
    program_name: str       = Path(cmdline[0]).name
    program_args: list[str] = cmdline[1:]

    # Description
    description: str = "Reads markdown entries and writes them in an html blog."

    # Create parser
    parser = argparse.ArgumentParser(prog=program_name, description=description)

    # Define expected arguments
    parser.add_argument("input_dir",  help="Input directory",  type=Path)
    parser.add_argument("output_dir", help="Output directory", type=Path)

    # Parse program arguments
    parsed_args: argparse.Namespace = parser.parse_args(program_args)

    # Return arguments
    return parsed_args.input_dir, parsed_args.output_dir


# -----------------------------------------------------------------------------
