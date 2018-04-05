# pylint: disable=W,C,R

from __future__ import print_function

from pytest import mark

from restful_ssh_config.models import Host


@mark.parametrize(
    'id,reference_name,expected',
    [
        (1, 'SomeHostname', "<Host 1 - 'SomeHostname'>"),
    ],
)
def test_representation(id, reference_name, expected):
    model = Host(id=id, reference_name=reference_name)
    assert expected == model.__repr__()
