"""This file provides the Keyword model"""
# pylint: disable=too-few-public-methods

from datetime import datetime

from restful_ssh_config import DATABASE
from restful_ssh_config.models import HOST_CONFIG_LOOKUP

# pylint: disable=invalid-name
# pylint: disable=no-member
Column = DATABASE.Column
DateTime = DATABASE.DateTime
SqlInteger = DATABASE.Integer
SqlString = DATABASE.String
# pylint: enable=no-member
# pylint: enable=invalid-name


class ConfigFile(DATABASE.Model):
    """This class sets up the fields for the Keyword model"""

    # __tablename__ = 'config_files'

    id = Column(  # pylint: disable=invalid-name
        SqlInteger,
        primary_key=True,
    )
    file_path = Column(
        SqlString(255),
    )
    hosts = DATABASE.relationship(  # pylint: disable=no-member
        'Host',
        secondary=HOST_CONFIG_LOOKUP,
        lazy='subquery',
    )
    created = Column(
        DateTime,
        default=datetime.utcnow,
    )
    updated = Column(
        DateTime,
        default=datetime.utcnow,
    )
