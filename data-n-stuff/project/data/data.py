import json

import numpy as np
from pkg_resources import resource_filename, resource_stream


def load_default():
    filename = resource_filename(__package__, "samples/default.npz")
    return dict(np.load(filename).items())


def load_template():
    with resource_stream("project.data", "samples/template.json") as fin:
        return json.load(fin)
