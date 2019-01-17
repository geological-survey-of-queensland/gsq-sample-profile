from os import path
from os import listdir
import rdflib
import pyshacl

APP_DIR = path.dirname(path.realpath(__file__))
SHAPES_DIR = path.join(APP_DIR, 'shapes')
DATA_DIR = path.join(APP_DIR, 'data')

# compile total shapes
shapes_files = [f for f in listdir(SHAPES_DIR)]
shapes_graph = rdflib.Graph()
for s in shapes_files:
    shapes_graph += rdflib.Graph().parse(path.join(SHAPES_DIR, s), format='turtle')

# data graph
data_graph = rdflib.Graph().parse(path.join(DATA_DIR, 'sample-invalid.ttl'), format='turtle')

# validate
v = pyshacl.validate(data_graph, shacl_graph=shapes_graph)

import pprint
pprint.pprint(v)
