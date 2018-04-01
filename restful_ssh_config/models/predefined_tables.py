"""This file provides predefined lookup tables"""

from sqlalchemy import (
    Column,
    ForeignKey,
    Integer as SqlInteger,
    Table,
)

KEYWORD_HOST_LOOKUP = Table(
    'keywords',
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
    'hosts',
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
