"""This file sets up model schemas"""
# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods

from restful_ssh_config import MARSHMALLOW
from restful_ssh_config.models import (
    ConfigFile,
    Host,
    Keyword
)


class KeywordSchema(MARSHMALLOW.ModelSchema):

    class Meta(object):
        model = Keyword


class HostSchema(MARSHMALLOW.ModelSchema):

    class Meta(object):
        model = Host


class ConfigFileSchema(MARSHMALLOW.ModelSchema):

    class Meta(object):
        model = ConfigFile
