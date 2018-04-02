"""This file provides the Keyword model"""
# pylint: disable=too-few-public-methods

from restful_ssh_config import BaseModel, DATABASE
from restful_ssh_config.models import HOST_CONFIG_LOOKUP

# pylint: disable=invalid-name
# pylint: disable=no-member
Column = DATABASE.Column
SqlString = DATABASE.String
# pylint: enable=no-member
# pylint: enable=invalid-name


class ConfigFile(BaseModel):
    """This class sets up the fields for the Keyword model"""

    __tablename__ = 'config_files'

    file_path = Column(
        SqlString(255),
    )
    hosts = DATABASE.relationship(  # pylint: disable=no-member
        'Host',
        secondary=HOST_CONFIG_LOOKUP,
        lazy='subquery',
    )

    def __repr__(self):
        return "<ConfigFile '%r'>" % self.file_path
