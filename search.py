import sys
import argparse
import re
import os


def main():
    args = argparser()
    searchlist = createlist(args)
    search(args, searchlist)

    return (0)


# Handle Argobj setup/creation
def argparser():
    parser = argparse.ArgumentParser(description='Search Function - Assignment 2')
    parser.add_argument('--match', '-m', required='True', help='comma-seperated list of patterns to match (Required)')
    parser.add_argument('--ignore-case', '-i', action='store_true', help='ignore upper/lower case')
    parser.add_argument('-r', action='store_true', help="""traverse all sub-directories recursively to search for 
    matches within any sub-directories""")

    args = parser.parse_args()
    # Regex match Letters/Numbers/Commas
    if re.match('[a-zA-Z0-9,.]', args.match):
        return args
    else:
        print("Match Failure!")
        sys.exit()


# Argparse into List
def createlist(args):
    # Any internal - characters in an argparse will be converted to _
    if args.ignore_case:
        searchstring = args.match.lower()
    else:
        searchstring = args.match

    searchlist = searchstring.split(',')
    return searchlist


# Dir/file search Handling
def search(args, searchlist):
    cwd = os.getcwd()
    foundf = []
    foundd = []

    if args.r:
        for term in searchlist:
            for root, directory, file in os.walk(cwd):
                for string in file:
                    if term in string:
                        foundf.append(os.path.join(root, string))

    print("Files Matching '" + searchlist[0] + "':")
    if not foundf:
        print('   None')
    else:
        print("   " + "\n   ".join(foundf))


if __name__ == "__main__":
    sys.exit(main())