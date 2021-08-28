import yaml


def yaml_to_dict(filename):
    with open(filename, "r") as f:
        d = f.read()

    return yaml.load(d, Loader=yaml.FullLoader)
