#!/usr/bin/env python
import sys
import argparse
import re
import os


def main():
    args = argparser()
    searchlist = createlist(args)
    search(args, searchlist)

    return 0


# Handle Argobj setup/creation
def argparser():
    parser = argparse.ArgumentParser(description='Search Function - Assignment 2')
    parser.add_argument('--match', '-m', required='True', help='comma-separated list of patterns to match (Required)')
    parser.add_argument('--ignore-case', '-i', action='store_true', help='ignore upper/lower case')
    parser.add_argument('-r', action='store_true', help="""traverse all sub-directories recursively to search for 
    matches within any sub-directories""")

    args = parser.parse_args()

    # Regex match Letters/Numbers/Commas/Periods
    if re.match('[a-zA-Z0-9,.]', args.match):
        return args
    else:
        print("Match Failure!")
        sys.exit()


# Argparse into List
def createlist(args):
    # Any internal - characters in an argparse name will be converted to _
    if args.ignore_case:
        searchstring = args.match.lower()
    else:
        searchstring = args.match

    # split string on commas
    searchlist = searchstring.split(',')
    return searchlist


# Dir/file search Handling
def search(args, searchlist):
    # get directory
    cwd = os.getcwd()

    # lists for string storage
    foundfile = []
    founddir = []

    # walk param handling for recursive implementation
    if args.r:
        searchparams = os.walk(cwd)
    else:
        # next will only search starting dir
        searchparams = [next(os.walk(cwd))]

    for term in searchlist:
        for root, directory, file in searchparams:
            for fstring in file:
                if term in fstring:
                    foundfile.append(os.path.join(root, fstring))
            for dstring in directory:
                if term in dstring:
                    founddir.append(os.path.join(root, dstring))
        printresults(foundfile, founddir, term)
        # clear lists for next term
        foundfile.clear()
        founddir.clear()


def printresults(files, dirs, term):
        print("Files Matching '" + term + "':")
        if not files:
            print('   None')
        else:
            print("   " + "\n   ".join(files))

        print("Directory Matching '" + term + "':")
        if not dirs:
            print('   None')
        else:
            print("   " + "\n   ".join(dirs))


if __name__ == "__main__":
    sys.exit(main())