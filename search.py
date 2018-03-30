import sys
import argparse
import re
import os


def main():
    args = argparser()
    searchlist = createlist(args)
    search(searchlist)

    return (0)


# Handle Argobj setup/creation
def argparser():
    parser = argparse.ArgumentParser(description='Search Function - Assignment 2')
    parser.add_argument('--match', '-m', required='True', help='comma-seperated list of patterns to match (Required)')
    parser.add_argument('--ignore-case', '-i', action='store_true', help='if this argument is used, will ignore upper/lower case')

    args = parser.parse_args()
    # Regex match Letters/Numbers/Commas
    if re.match('[a-zA-Z0-9,.]', args.match):
        print("Match Success!")
        return args
    else:
        print("Match Failure!")
        sys.exit()


# Argparse into List
def createlist(args):
    # Any internal - characters in an argparse will be converted to _ characters to make sure the string is a valid attribute name.
    if args.ignore_case:
        searchstring = args.match.lower()
    else:
        searchstring = args.match

    searchlist = searchstring.split(',')
    return searchlist

# Dir/file search Handling
def search(searchlist):
    print(searchlist)


if __name__ == "__main__":
    sys.exit(main())