"""This file provides the Keyword model"""
# pylint: disable=too-few-public-methods

from json import load as json_load
from os.path import dirname, join

from sqlalchemy.orm import validates
from marshmallow import ValidationError
from restful_ssh_config import DATABASE

__location__ = dirname(__file__)
DATA_DIRECTORY = join(dirname(__location__), 'data')
DATA_FILE = join(DATA_DIRECTORY, 'keywords.json')

# pylint: disable=invalid-name
# pylint: disable=no-member
Column = DATABASE.Column
SqlString = DATABASE.String
SqlText = DATABASE.Text
# pylint: enable=no-member
# pylint: enable=invalid-name

KEYWORDS = []
with open(DATA_FILE, 'r') as keywords_file:
    KEYWORDS = json_load(keywords_file)


class Keyword(DATABASE.Model):
    """This class sets up the fields for the Keyword model"""

    __tablename__ = 'keywords'

    keyword = Column(
        'keyword',
        SqlString(255),
        nullable=False,
    )
    argument = Column(
        'argument',
        SqlText,
        nullable=False,
    )

    @validates('keyword')
    def validates_keyword(self, key, value):  # pylint: disable=no-self-use
        """Ensures the provided keyword is a valid OpenSSH keyword"""
        if value.lower() not in KEYWORDS:
            raise ValidationError(
                "%s is not a current keyword (or the keywords are outdated)"
                % (value)
            )
            return False
        return value
