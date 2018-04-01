"""This file provides the Keyword model"""
# pylint: disable=too-few-public-methods

from datetime import datetime

from restful_ssh_config import DATABASE

# pylint: disable=invalid-name
# pylint: disable=no-member
Column = DATABASE.Column
DateTime = DATABASE.DateTime
SqlInteger = DATABASE.Integer
SqlString = DATABASE.String
SqlText = DATABASE.Text
# pylint: enable=no-member
# pylint: enable=invalid-name


class Keyword(DATABASE.Model):
    """This class sets up the fields for the Keyword model"""

    __tablename__ = 'keywords'

    id = Column(  # pylint: disable=invalid-name
        SqlInteger,
        primary_key=True,
    )
    keyword = Column(
        SqlString(255),
        nullable=False,
    )
    argument = Column(
        SqlText,
        nullable=False,
    )
    created = Column(
        DateTime,
        default=datetime.utcnow,
    )
    updated = Column(
        DateTime,
        default=datetime.utcnow,
    )
