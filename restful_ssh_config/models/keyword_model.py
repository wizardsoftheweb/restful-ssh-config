"""This file provides the Keyword model"""
# pylint: disable=too-few-public-methods

from sqlalchemy import (
    Column,
    String as SqlString,
    Text as SqlText
)
from sqlalchemy.orm import validates
from marshmallow import ValidationError

from restful_ssh_config.data import KEYWORDS
from restful_ssh_config.models import BaseModel


class Keyword(BaseModel):
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

    def __repr__(self):
        return "<Keyword %r: '%s'>" % (self.keyword, self.argument)

    # pylint: disable=no-self-use
    # pylint: disable=unused-argument
    @validates('keyword')
    def validate_keyword(self, key, value):
        """Ensures the provided keyword is a valid OpenSSH keyword"""
        if value.lower() not in KEYWORDS:
            raise ValidationError(
                "%s is not a current keyword (or the keywords are outdated)"
                % (value)
            )
        return value
    # pylint: enable=unused-argument
    # pylint: enable=no-self-use
