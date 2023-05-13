import os
import sys
import argparse

"""
usage: subfolders_counter.py [-h] folder_path [folder_path ...]

This script counts the number of subfolders in a given folder(s)

positional arguments:
  folder_path

optional arguments:
  -h, --help   show this help message and exit
"""

def createParser():
    parser = argparse.ArgumentParser(description="This script counts the number of subfolders in a given folder(s)")
    parser.add_argument("folder_path", nargs='+')
    return parser

parser = createParser()
namespace = parser.parse_args(sys.argv[1:])

if all([os.path.isdir(folder) & os.path.exists(folder) for folder in namespace.folder_path]):
    for folder_path in namespace.folder_path:
        total = 0
        for root, dirs, files in os.walk( folder_path ):
            total += len( dirs )
        print(f"Number of subfolders in {folder_path} - ", total )
    sys.exit(0)
else:
    sys.exit("Argument(s) is/are not path-like or path(s) doesn't/don't exist")