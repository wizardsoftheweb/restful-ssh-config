"""This file sets up model schemas"""
# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods

from sqlalchemy.orm import validates

from restful_ssh_config import MARSHMALLOW
from restful_ssh_config.models import (
    ConfigFile,
    Host,
    Keyword
)


class KeywordSchema(MARSHMALLOW.ModelSchema):

    class Meta(object):
        model = Keyword

    @validates('keyword')
    def validate_keyword(self, keyword):  # pylint: disable=no-self-use
        """Ensures the provided keyword is a valid OpenSSH keyword"""
        return Keyword.validates_keyword(self, 'keyword', keyword)


class HostSchema(MARSHMALLOW.ModelSchema):

    class Meta(object):
        model = Host


class ConfigFileSchema(MARSHMALLOW.ModelSchema):

    class Meta(object):
        model = ConfigFile
