# pylint: disable=W,C,R

from __future__ import print_function

from pytest import mark
from marshmallow import ValidationError
from mock import patch
from unittest import TestCase

from restful_ssh_config.models import Keyword


@mark.parametrize(
    'keyword,argument,expected',
    [
        ('host', 'value', "<Keyword 'host': 'value'>"),
    ],
)
def test_representation(keyword, argument, expected):
    model = Keyword(keyword=keyword, argument=argument)
    assert expected == model.__repr__()


class KeywordModelUnitTests(TestCase):

    @patch(
        'restful_ssh_config.models.keyword_model.KEYWORDS',
        [],
    )
    def test_keyword_validation(self):
        with self.assertRaises(ValidationError):
            model = Keyword(keyword='any', argument='value')
