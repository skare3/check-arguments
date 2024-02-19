import json
import yaml
import logging
import sys


def main():
    with open("arguments.json") as fh:
        arguments = json.load(fh)
    with open("argument_spec.yml") as fh:
        argument_spec = yaml.load(fh, Loader=yaml.SafeLoader)
        argument_spec = {arg["name"]: arg for arg in argument_spec}

    # Check for unknown or missing arguments
    missing = [
        name
        for name in argument_spec
        if argument_spec[name].get("required", False) and name not in arguments
    ]
    unknown = [name for name in arguments if name not in argument_spec]
    if missing or unknown:
        if missing:
            logging.error("Missing arguments:", missing)
        if unknown:
            logging.error("Unknown arguments:", unknown)
        raise sys.exit(1)

    # if not required and default is not specified, then default is the empty string
    arguments = {
        name: arguments.get(name, argument_spec[name].get("default", ""))
        for name in argument_spec
    }

    # if type is bool, coerce into string with values 'true' or 'false'
    for name in argument_spec:
        if argument_spec[name].get("type", "str") == "bool":
            arguments[name] = (
                "true" if str(arguments[name]) in ["true", "True", "1"] else "false"
            )

    for key, value in arguments.items():
        print(f'{key}="{value}"')


if __name__ == "__main__":
    main()
