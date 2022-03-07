"""
Commandline module: Parses command line arguments.
"""
from   pathlib import Path
import argparse
import sys

# -----------------------------------------------------------------------------
#  def parse_args(cmdline: list[str]) -> tuple[Path, Path]:
    #  """Parses the commandline. Must include executable path in [0], like sys.argv."""
def parse_args():

    # Split command line
    #  program_name: str       = Path(cmdline[0]).name
    #  program_args: list[str] = cmdline[1:]

    # Description
    description: str = "Reads markdown entries and writes them in an html blog."

    # Create parser
    parser = argparse.ArgumentParser(prog=sys.argv[0], description=description)

    # Define expected arguments
    parser.add_argument("-i", "--inputDir",  help="Input directory",  type=Path, required=True)
    parser.add_argument("-o", "--outputDir", help="Output directory", type=Path, required=True)

    # Parse program arguments
    parsed_args: argparse.Namespace = parser.parse_args()

    # Return arguments
    return parsed_args


# -----------------------------------------------------------------------------
