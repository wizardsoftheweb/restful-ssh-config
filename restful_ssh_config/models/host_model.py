"""This file provides the Keyword model"""
# pylint: disable=too-few-public-methods

from datetime import datetime

from restful_ssh_config import DATABASE
from restful_ssh_config.models import HOST_CONFIG_LOOKUP, KEYWORD_HOST_LOOKUP

# pylint: disable=invalid-name
# pylint: disable=no-member
Column = DATABASE.Column
DateTime = DATABASE.DateTime
SqlInteger = DATABASE.Integer
SqlString = DATABASE.String
# pylint: enable=no-member
# pylint: enable=invalid-name


class Host(DATABASE.Model):
    """This class sets up the fields for the Keyword model"""

    # __tablename__ = 'hosts'

    id = Column(  # pylint: disable=invalid-name
        SqlInteger,
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
