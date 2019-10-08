

def read_input():
    print('Matrix A')
    val = input('width:')
    mx_a_width = int(val)
    val = input('height:')
    mx_a_height = int(val)

    print('\nMatrix B')
    val = input('width:')
    mx_b_width = int(val)
    val = input('height:')
    mx_b_height = int(val)

    print('\nMatrix A values:')
    mx_a = read_mx(mx_a_width, mx_a_height)
    print('Matrix B values:')
    mx_b = read_mx(mx_b_width, mx_b_height)

    return mx_a, mx_b


def read_mx(width, height):
    mx = []
    for _ in range(height):
        row_raw = input()
        row = [int(val) for val in filter(None, row_raw.split(' '))]
        if len(row) != width:
            raise ValueError('{} value required'.format(width))
        mx.append(row)
    return mx


if __name__ == '__main__':
    print(read_input())