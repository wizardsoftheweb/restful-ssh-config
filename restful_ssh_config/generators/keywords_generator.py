"""
This file generates a list of valid keywords from the OpenSSH master branch.
"""
# from __future__ import print_function

from json import dumps
from os import makedirs
from os.path import dirname, exists, join
from re import compile as re_compile, IGNORECASE, search, sub

from requests import get

__location__ = dirname(__file__)
OUT_DIRECTORY = join(dirname(__location__), 'data')
if not exists(OUT_DIRECTORY):
    makedirs(OUT_DIRECTORY)
OUT_FILE = join(OUT_DIRECTORY, 'keywords.json')

OPCODES_PATTERN = re_compile(
    r'enum\s*\{(?P<raw_codes>[^}]*?)\}\s*opcodes;',
    IGNORECASE,
)

READCONF_MASTER_URL = 'https://raw.githubusercontent.com/openssh/openssh-portable/master/readconf.c'
FULL_SOURCE = get(READCONF_MASTER_URL)

SORTED = False
OPCODES_MATCH = search(OPCODES_PATTERN, FULL_SOURCE.text)
if OPCODES_MATCH and OPCODES_MATCH.group('raw_codes'):
    SPACELESS = sub(r'\s', '', OPCODES_MATCH.group('raw_codes'))
    OLESS = sub(r'o(\w+)(,|$)', r'\1\2', SPACELESS)
    CLEANED_CODES = OLESS.split(',')
    SORTED = sorted(CLEANED_CODES)

with open(OUT_FILE, 'w') as data_file:
    data_file.write("%s\n" % dumps(SORTED))
