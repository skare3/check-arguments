import pprint
import sys


def main():
    arguments = dict([arg.split(':') for arg in ' '.join((sys.argv[2:-1])).split(',')])
    pprint.pprint(arguments)


if __name__ == "__main__":
    main()
