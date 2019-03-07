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
    for num_iter in range (N//2):
        for j in range(num_iter, N - num_iter):
            saved_value = mat[num_iter, j]
            #mat[num_iter, j] = mat[num_iter, j]
    return (mat)

if __name__ == "__main__":
    x = numpy.indices((3,3))[0]
    print ('x = {} and shape = {}'.format(x, x.shape))
    print ('Rotated mat = {}'.format(rotate_numpy_matrix(x)))
