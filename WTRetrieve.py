import argparse
import os
import sys
import requests
from lxml import html

# Parser for arguments
parser = argparse.ArgumentParser()
parser.add_argument("url", default=None, nargs='*')
parser.add_argument("-f", nargs=1, help='specify file', metavar='file')
parser.add_argument("--nolinks", action='store_true', help='no links')
parser.add_argument("--nonewlines", action='store_true',
                    help='no newlines between links')
args = parser.parse_args()


def print_titles(urls):
    # Remove empty entries
    urls = [url.strip() for url in urls if url.strip() != ""]

    # Process each URL
    for index, url in enumerate(urls):
        # Attempt to retrieve and print the title
        try:
            r = requests.get(url)
            tree = html.fromstring(r.content)
            print(tree.findtext(".//title"))
        except Exception as err:
            print("Error:", err)
            sys.exit(1)

        # Print URL
        if not args.nolinks:
            print(url)
        # Print newline when appropriate
        if not args.nonewlines and index != len(urls) - 1:
            print("")


# URL arguments
if args.url:
    print_titles(args.url)

# File argument
if args.f:
    # Ensure that file exists
    if not os.path.isfile(args.f[0]):
        print("File does not exist")
        sys.exit(1)

    # Read file and get each line
    try:
        f = open(args.f[0], 'r')
        filecontents = f.readlines()
        f.close()
        print_titles(filecontents)
    except Exception as err:
        print("Error:", err)
        sys.exit(1)
