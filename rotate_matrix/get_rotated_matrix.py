import numpy

def rotate_numpy_matrix(mat:numpy.ndarray) -> numpy.ndarray:
    '''
    Example:
    N = 2
    1 1
    0 0
    Ans:
    0 1
    0 1
    and
    N = 3
    1 1 2
    0 0 2
    0 0 2
    Ans:
    0 0 1
    0 0 1
    2 2 2
    '''
    N:int = len(mat)
    for layer in range (N//2):
        first = layer
        last = N - layer - 1
        for j in range(first, last):
            offset = j - first
            saved_value = mat[first, j]
            mat[first, j] = mat[last - offset, first]  # 0 0 <= 2 0, 0 1 <= 1 0  
            mat[last - offset, first] = mat[last, last - offset]  # 2 0 <= 2 2, 1 0 <= 2 1
            mat[last, last - offset] = mat[j, last]  # 2 2 <= 0 2, 2 1 <= 1 2
            mat[j, last] = saved_value  # 0 2 <= 0 0, 2 1 <= 1 2
    return (mat)

if __name__ == "__main__":
    x = numpy.array([[0, 0, 0],[1, 1, 1],[2, 2, 2]])
    print ('x = {} and shape = {}'.format(x, x.shape))
    print ('Rotated mat = {}'.format(rotate_numpy_matrix(x)))
