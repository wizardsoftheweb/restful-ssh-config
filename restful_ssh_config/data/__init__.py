"""This file provides Python access to the local data files"""

from json import load as json_load
from os.path import dirname, join

__location__ = dirname(__file__)
DATA_DIRECTORY = join(dirname(__location__), 'data')

KEYWORDS_FILE = join(DATA_DIRECTORY, 'keywords.json')

KEYWORDS = []
with open(KEYWORDS_FILE, 'r') as keywords_file:
    KEYWORDS = json_load(keywords_file)
