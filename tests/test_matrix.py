from contextlib import contextmanager

import pytest

from matrix import Matrix


@contextmanager
def does_not_raise():
    yield


@pytest.mark.parametrize('list2d, expectation',
                         [pytest.param([[1]], does_not_raise(), id='correct_one_element'),
                          pytest.param([[1, 2, 3]], does_not_raise(), id='correct_one_row'),
                          pytest.param([[1], [2], [3]], does_not_raise(), id='correct_one_column'),
                          pytest.param([[1, 11], [2, 22], [3, 33]], does_not_raise(), id='correct_one_column'),
                          pytest.param([[]], pytest.raises(ValueError, match=r'Row \d is empty'),
                                       id='incorrect_empty_2dlist'),
                          pytest.param([[1, 2], [3, 4], [5, 'a']], pytest.raises(ValueError,
                                                                                 match=r'Matrix elements are not same as configured type'),
                                       id='incorrect_empty_2dlist'),
                          pytest.param([[1], [2, 2]], pytest.raises(ValueError, match=r'Rows dont have same length'),
                                       id='incorrect_empty_2dlist'),
                          ])
def test_matrix_init(list2d, expectation):
    with expectation:
        Matrix(list2d)


@pytest.mark.parametrize('list2d, expectation', [
    pytest.param([[1.0, 2.0, 3.0]], does_not_raise(), id='correct_type_float'),
    pytest.param([[1, 2], [3, 4], [5, 6.0]], pytest.raises(ValueError,
                                                           match=r'Matrix elements are not same as configured type'),
                 id='incorrect_empty_2dlist'),
])
def test_matrix_init_float_type(list2d, expectation):
    with expectation:
        mx = Matrix(list2d, float)
        assert isinstance(mx._list2d[0][0], float)


def test_matrix_init_dimensions_m_n():
    mx = Matrix([[1, 2], [3, 4], [5, 6]])
    assert (mx.m, mx.n) == (3, 2)


@pytest.mark.parametrize('mx_a, mx_b, expected_result, expectation', [
    pytest.param([[1, 2, 3]], [[1], [2], [3]], [[14]], does_not_raise(), id='correct_1Xn_nX1'),
    pytest.param([[1, 2], [3, 4], [5, 6]],[[1]],'n/a', pytest.raises(ValueError,
                                                         match=r'Matrices have to be mXn nXp'),
                 id='incorrect_empty_2dlist'),
])
def test_matrix_multiply(mx_a, mx_b, expected_result, expectation):
    with expectation:
        mx_result = Matrix(mx_a).multiply(Matrix(mx_b))
        assert mx_result._list2d == expected_result
