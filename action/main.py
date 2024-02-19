import pprint
import json
import sys


def main():
    with open(sys.argv[1]) as fh:
        arguments = json.load(fh)
    pprint.pprint(arguments)


if __name__ == "__main__":
    main()
