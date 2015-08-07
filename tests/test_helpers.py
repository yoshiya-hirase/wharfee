from __future__ import unicode_literals

import pytest
from wharfee.helpers import parse_port_bindings, parse_volume_bindings


@pytest.mark.parametrize("ports, expected", [
    (['3306'], {'3306': None}),
    (['9999:3306'], {'3306': '9999'}),
    (['0.0.0.0:9999:3306'], {'3306': ('0.0.0.0', '9999')}),
    (['9999:3306', '127.0.0.1::8001'],
     {'8001': ('127.0.0.1', None), '3306': '9999'}),
])
def test_port_parsing(ports, expected):
    """
    Parse port mappings.
    """
    result = parse_port_bindings(ports)

    assert result == expected


@pytest.mark.parametrize("volumes, expected", [
    (['/tmp'], {}),
    (['/var/www:/webapp'], {'/var/www': {'bind': '/webapp', 'ro': False}}),
    (['/var/www:/webapp:ro'], {'/var/www': {'bind': '/webapp', 'ro': True}}),
])
def test_volume_parsing(volumes, expected):
    """
    Parse volume mappings.
    :param volumes: list of string
    :param expected: dict
    """
    result = parse_volume_bindings(volumes)

    assert result == expected
