# pylint: disable=W,C,R

from __future__ import print_function

from pytest import mark

from restful_ssh_config.models import BaseModel


class BaseModelTest(BaseModel):
    """"""


@mark.parametrize(
    'column,expected',
    [
        ('id', 'INTEGER'),
        ('created', 'DATETIME'),
        ('updated', 'DATETIME'),
    ],
)
def test_column_type(column, expected):
    model = BaseModelTest()
    assert expected == model.__table__.columns[column].type.__str__()
