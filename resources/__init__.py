import json
import os


def get_resource(path):
    with open(os.path.join('resources', path), 'r') as f:
        return json.load(f)


config = get_resource('config.json')
