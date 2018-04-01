"""This file sets up model schemas"""
# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods

from json import load as json_load
from os.path import dirname, join

from marshmallow import validates, ValidationError

from restful_ssh_config import MARSHMALLOW
from restful_ssh_config.models import (
    ConfigFile,
    Host,
    Keyword
)

__location__ = dirname(__file__)
DATA_DIRECTORY = join(__location__, 'data')
DATA_FILE = join(DATA_DIRECTORY, 'keywords.json')

KEYWORDS = []
with open(DATA_FILE, 'r') as keywords_file:
    KEYWORDS = json_load(keywords_file)


class KeywordSchema(MARSHMALLOW.ModelSchema):

    class Meta(object):
        model = Keyword

    @validates('keyword')
    def validates_keyword(self, keyword):  # pylint: disable=no-self-use
        """Ensures the provided keyword is a valid OpenSSH keyword"""
        if keyword.lower() not in KEYWORDS:
            raise ValidationError(
                "%s is not a current keyword (or the keywords are outdated)"
                % (keyword)
            )


class HostSchema(MARSHMALLOW.ModelSchema):

    class Meta(object):
        model = Host


class ConfigFileSchema(MARSHMALLOW.ModelSchema):

    class Meta(object):
        model = ConfigFile
