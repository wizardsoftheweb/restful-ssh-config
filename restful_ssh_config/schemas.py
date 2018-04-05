"""This file sets up model schemas"""
# pylint: disable=too-few-public-methods

from marshmallow_sqlalchemy import ModelSchema
from sqlalchemy.orm import validates

from restful_ssh_config.models import (
    ConfigFile,
    Host,
    Keyword
)


class KeywordSchema(ModelSchema):
    """Provides the schema for Keywords"""
    class Meta(object):
        """The schema's metadata"""
        model = Keyword

    @validates('keyword')
    def validate_keyword(self, keyword):  # pylint: disable=no-self-use
        """Ensures the provided keyword is a valid OpenSSH keyword"""
        return Keyword.validates_keyword(self, 'keyword', keyword)


class HostSchema(ModelSchema):
    """Provides the schema for Hosts"""

    class Meta(object):
        """The schema's metadata"""
        model = Host


class ConfigFileSchema(ModelSchema):
    """Provides the schema for Config Files"""

    class Meta(object):
        """The schema's metadata"""
        model = ConfigFile
