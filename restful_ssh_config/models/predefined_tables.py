"""This file provides predefined lookup tables"""

from restful_ssh_config import DATABASE

# pylint: disable=invalid-name
# pylint: disable=no-member
Column = DATABASE.Column
ForeignKey = DATABASE.ForeignKey
SqlInteger = DATABASE.Integer
Table = DATABASE.Table
# pylint: enable=no-member
# pylint: enable=invalid-name

KEYWORD_HOST_LOOKUP = Table(
    'keyword_host_lookups',
    Column(
        'keyword_id',
        SqlInteger,
        ForeignKey('keywords.id'),
        primary_key=True,
    ),
    Column(
        'host_id',
        SqlInteger,
        ForeignKey('hosts.id'),
        primary_key=True,
    )
)

HOST_CONFIG_LOOKUP = Table(
    'host_config_lookups',
    Column(
        'host_id',
        SqlInteger,
        ForeignKey('hosts.id'),
        primary_key=True,
    ),
    Column(
        'config_file_id',
        SqlInteger,
        ForeignKey('config_files.id'),
        primary_key=True,
    )
)
