# Logic for DES Key Generation
from collections import deque


def permutation_order_1(key):
    permutation_order = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60,
                         52, 44, 36, 63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29,
                         21, 13, 5, 28, 20, 12, 4]

    permuted_key = []

    for i in range(0, 56):
        perm = permutation_order[i]
        permuted_key.append(key[perm - 1])

    return permuted_key


def left_shift(half_key):
    half_key_copy = deque(half_key)
    half_key_copy.rotate(-1)
    return half_key_copy


def combine_left_and_right(left_side, right_side):
    key = left_side + right_side

    permutation_order = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52,
                         31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]

    permuted_key = []

    for i in range(0, 48):
        perm = permutation_order[i]
        permuted_key.append(key[perm - 1])

    return permuted_key  # 48 bits long


def gen_key(key, num_of_rounds):
    key = permutation_order_1(key)

    for x in range(0, num_of_rounds):
        key = list(key)
        left_side = key[:28]
        right_side = key[28:]
        left_side = left_shift(left_side)
        right_side = left_shift(right_side)
        round_key = combine_left_and_right(left_side, right_side)
        key = left_side + right_side
    return round_key
