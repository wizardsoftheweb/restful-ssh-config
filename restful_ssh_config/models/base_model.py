"""This file provides the common Model interface"""
# pylint: disable=no-self-argument

from datetime import datetime

from sqlalchemy import (
    Column,
    DateTime as SqlDateTime,
    Integer as SqlInteger,
)
from sqlalchemy.ext.declarative import declared_attr

from restful_ssh_config import DATABASE


class BaseModel(DATABASE.Model):
    """This class provides a common interface for models."""

    __abstract__ = True

    @declared_attr
    def id(cls):  # pylint: disable=invalid-name
        """Builds the id column"""
        return Column(
            'id',
            SqlInteger,
            unique=True,
            primary_key=True,
            autoincrement=True,
        )

    @declared_attr
    def created(cls):
        """Builds the created date/time column"""
        return Column(
            'created',
            SqlDateTime,
            default=datetime.utcnow,
        )

    @declared_attr
    def updated(cls):
        """Builds the updated date/time column"""
        return Column(
            'updated',
            SqlDateTime,
            default=datetime.utcnow,
            onupdate=datetime.utcnow,
        )
