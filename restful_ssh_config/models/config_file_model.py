"""This file provides the ConfigFile model"""
# pylint: disable=too-few-public-methods

from sqlalchemy import Column, String as SqlString

from restful_ssh_config import DATABASE
from restful_ssh_config.models import BaseModel, HOST_CONFIG_LOOKUP


class ConfigFile(BaseModel):
    """This class sets up the fields for the ConfigFile model"""

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
        return "<ConfigFile %r>" % self.file_path
