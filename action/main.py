import pprint
import json
import yaml


def main():
    with open("arguments.json") as fh:
        arguments = json.load(fh)
    with open("argument_spec.yml") as fh:
        argument_spec = yaml.load(fh, Loader=yaml.SafeLoader)
    pprint.pprint(arguments)
    pprint.pprint(argument_spec)


if __name__ == "__main__":
    main()
