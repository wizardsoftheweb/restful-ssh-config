"""This file provides the Keyword model"""
# pylint: disable=too-few-public-methods

from datetime import datetime

from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    ForeignKey,
    String as SqlString,
    Text as SqlText
)

from restful_ssh_config import DATABASE


class Keyword(DATABASE.Model):
    """This class sets up the fields for the Keyword model"""
    id = Column(  # pylint: disable=invalid-name
        Integer,
        primary_key=True,
    )
    keyword = Column(
        SqlString(255),
        nullable=False
    )
    argument = Column(
        SqlText,
        nullable=False
    )
    created = Column(
        DateTime,
        default=datetime.utcnow
    )
    updated = Column(
        DateTime,
        default=datetime.utcnow
    )
