# pylint: disable=W,C,R

from __future__ import print_function

from pytest import mark

from restful_ssh_config.models import ConfigFile


@mark.parametrize(
    'file_path,expected',
    [
        ('some/path', "<ConfigFile 'some/path'>"),
    ],
)
def test_representation(file_path, expected):
    model = ConfigFile(file_path=file_path)
    assert expected == model.__repr__()
