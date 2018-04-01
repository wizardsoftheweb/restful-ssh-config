from datetime import datetime

from flask_sqlalchemy import Model
from sqlalchemy import (
    Column,
    DateTime as SqlDateTime,
    Integer as SqlInteger,
)
from sqlalchemy.ext.declarative import declared_attr


class BaseModel(Model):

    @declared_attr
    def id(cls):
        return Column(
            'id',
            SqlInteger,
            unique=True,
            primary_key=True,
            autoincrement=True,
        )

    @declared_attr
    def created(cls):
        return Column(
            'created',
            SqlDateTime,
            default=datetime.utcnow,
        )

    @declared_attr
    def updated(cls):
        return Column(
            'updated',
            SqlDateTime,
            default=datetime.utcnow,
            onupdate=datetime.utcnow,
        )
