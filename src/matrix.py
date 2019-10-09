class Matrix:
    """
    class representing matrix
    """

    def __init__(self, list2d, dtype=int):
        self._dtype = dtype
        self._validate_matrix(list2d)
        self._m = len(list2d)
        self._n = len(list2d[0])
        self._list2d = list2d

    @property
    def m(self):
        """
        Number of rows
        """
        return self._m

    @property
    def n(self):
        """
        Number of columns
        """
        return self._n

    @property
    def list2d(self):
        return self._list2d

    def _validate_matrix(self, list2d):
        """
        Method validates provided 2d list:
            if matrix and rows are lists
            if rows are same length
            if items are correct type
            if is not empty

        Args:
            list2d:

        Returns:

        """
        rows_len_set = set()
        if not isinstance(list2d, list):
            ValueError(' Not 2d list')
        for idx, row in enumerate(list2d):
            if not isinstance(row, list):
                raise ValueError('Row {} is not lists'.format(idx))
            rows_len_set.add(len(row))
            if 0 in rows_len_set:
                raise ValueError('Row {} is empty'.format(idx))
            if len(rows_len_set) != 1:
                raise ValueError('Rows dont have same length')

            if not all([isinstance(i, self._dtype) for i in row]):
                raise ValueError('Matrix elements are not same as configured type')

    def multiply(self, matrix):
        """
        Checks if provided matrix is valid for multiplication and perform multiply.


        Args:
            matrix: Matrix for multiplication

        Returns:
             Matrix
        """
        if self.n != matrix.m:
            raise ValueError('Matrices have to be mXn nXp')

        mx_a = self._list2d
        mx_b = matrix._list2d
        return Matrix(
            [[sum(a * b for a, b in zip(mx_a_row, mx_b_col)) for mx_b_col in zip(*mx_b)] for mx_a_row in mx_a])


def __repr__(self):
    return 'Matrix(%s, %s)' % self._list2d, self._dtype

