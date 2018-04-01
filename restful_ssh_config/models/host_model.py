"""This file provides the Keyword model"""
# pylint: disable=too-few-public-methods

from datetime import datetime

from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    String as SqlString,
)

from restful_ssh_config import DATABASE
from restful_ssh_config.models import HOST_CONFIG_LOOKUP, KEYWORD_HOST_LOOKUP


class Host(DATABASE.Model):
    """This class sets up the fields for the Keyword model"""

    __tablename__ = 'hosts'

    id = Column(  # pylint: disable=invalid-name
        Integer,
        primary_key=True,
    )
    reference_name = Column(
        SqlString(255),
    )
    config_files = DATABASE.relationship(  # pylint: disable=no-member
        'ConfigFile',
        secondary=HOST_CONFIG_LOOKUP,
        lazy='subquery',
    )
    keywords = DATABASE.relationship(  # pylint: disable=no-member
        'Keyword',
        secondary=KEYWORD_HOST_LOOKUP,
        lazy='subquery',
        backref=DATABASE.backref(  # pylint: disable=no-member
            'hosts',
            lazy=True,
        ),
    )
    created = Column(
        DateTime,
        default=datetime.utcnow,
    )
    updated = Column(
        DateTime,
        default=datetime.utcnow,
    )
