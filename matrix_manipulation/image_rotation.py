'''
Rotate image by 90% clockwise
'''
from typing import List


def rotate_image(img: List[List[int]]) -> List[List[int]]:
    '''

    '''
    n = len(img)
    for layer in range(n // 2):
        # number of rotations in each side = (n-1) - (2 * layer)
        num_side_rot = (n - 1) - (2 * layer)
        end_offset = n - 1 - layer
        # print('For n = {} layer {} nsr {} eo {}'.format(n, layer, num_side_rot, end_offset))
        for j in range(num_side_rot):
            saved_top = img[layer][layer + j]

            # print('{} {} <- {} {}'.format(layer, layer + j, end_offset - j, layer))
            img[layer][layer + j] = img[end_offset - j][layer]

            # print('{} {} <- {} {}'.format(end_offset - j, layer, end_offset, end_offset - j))
            img[end_offset - j][layer] = img[end_offset][end_offset - j]

            # print('{} {} <- {} {}'.format(end_offset, end_offset - j, layer + j, end_offset))
            img[end_offset][end_offset - j] = img[layer + j][end_offset]

            # print('{} {} <- {} {}'.format(layer + j, end_offset, layer, layer + j))
            img[layer + j][end_offset] = saved_top

    return (img)


if __name__ == "__main__":
    img = [[1, 0, 0, 2], [0, 2, 1, 0], [2, 0, 1, 0], [0, 1, 2, 0]]
    print('Input:')
    print('\n'.join([' '.join(str(y) for y in x) for x in img]))
    print('\nOutput:')
    print('\n'.join([' '.join(str(y) for y in x) for x in rotate_image(img)]))
