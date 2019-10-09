from contextlib import contextmanager

import pytest

from mx_mul import read_input, read_mx_data, read_mx_dimensions


@contextmanager
def does_not_raise():
    yield


@pytest.mark.parametrize('input_values, expectation',
                         [pytest.param(('1', '2'), does_not_raise(), id='correct'),
                          pytest.param(('1', 's'), pytest.raises(ValueError, match=r'.*invalid literal for int\(\) with base 10:*'), id='incorrect type',
                                       ),
                          ])
def test_read_mx_dimensions(mocker, input_values, expectation):
    input_mock = mocker.patch('mx_mul.input')

    input_mock.side_effect = input_values
    with expectation:
        read_mx_dimensions()


@pytest.mark.parametrize('read_mx_args, input_values, expectation', [
    pytest.param((3, 2), ('11 12', '21 22', '31 32'), does_not_raise(), id='correct'),
    pytest.param((3, 2), ('11 12', '21 22 23', '31 32'), pytest.raises(ValueError),  id='too_many_values'),
    pytest.param((3, 2), ('11 12', '21 22', 'one 32'), pytest.raises(ValueError, match=r'.*invalid literal for int\(\) with base 10:*'),id='incorrect_value_type')

])
def test_read_mx_data(mocker, read_mx_args, input_values, expectation):
    input_mock = mocker.patch('mx_mul.input')
    input_mock.side_effect = input_values

    with expectation:
        mx = read_mx_data(*read_mx_args)

        assert mx == [[11, 12], [21, 22], [31, 32]]

@pytest.mark.parametrize('mx_dimemsions_return, expectation',
                         [pytest.param(((1, 2), (2, 5)), does_not_raise(), id='correct'),
                          pytest.param(((1, 2), (3, 5)), pytest.raises(ValueError, match='Matrices have to have mXn nXp dimensions'), id='incorrect dimensions',
                                       ),
                          ])
def test_read_input(mocker, mx_dimemsions_return, expectation):
    read_mx_dim_mock = mocker.patch('mx_mul.read_mx_dimensions')
    read_mx_dim_mock.side_effect = mx_dimemsions_return
    read_mx_data_mock = mocker.patch('mx_mul.read_mx_data')

    with expectation:
        read_input()
        read_mx_data_mock.assert_has_calls([mocker.call(1, 2), mocker.call(2, 5)])


