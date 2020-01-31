import json


def flatten_json(json):
    def process_value(keys, value, flattened):
        if isinstance(value, dict):
            for key in value.keys():
                process_value(keys + [key], value[key], flattened)
        elif isinstance(value, list):
            for idx, v in enumerate(value):
                process_value(keys + [str(idx)], v, flattened)
        else:
            flattened['__'.join(keys)] = value

    flattened = {}
    for key in json.keys():
        process_value([key], json[key], flattened)
    return flattened