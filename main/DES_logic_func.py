import random


def initial_perm(plaintext):
    permutation_order_no_1 = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54, 46, 38, 30, 22, 14,
                              6, 64, 56, 48, 40, 32, 24, 16, 8, 57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19,
                              11, 3, 61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]
    plaintext_copy = []
    for x in range(0, 64):
        perm = permutation_order_no_1[x]
        plaintext_copy.append(plaintext[perm - 1])

    return plaintext_copy


def undo(ciphertext):
    permutation_order_no_1 = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54, 46, 38, 30, 22, 14,
                              6, 64, 56, 48, 40, 32, 24, 16, 8, 57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19,
                              11, 3, 61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]
    ciphertext_copy = ciphertext
    arr = []
    for t in range(0, 64):
        arr.append(ciphertext_copy[t])

    for y in range(0, 64):
        ciphertext[permutation_order_no_1[y] - 1] = arr[y]
    return ciphertext


def right_side_expansion(initial_right_side):
    expansion_order = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18,
                       19, 20, 21, 20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]

    right_side_after_expansion = []
    for order in expansion_order:
        right_side_after_expansion.append(initial_right_side[order - 1])
    return right_side_after_expansion


def right_xor_key(right_side, key):
    right_side_after_xor = []
    for i in range(0, 48):
        each_key = int(key[i])
        each_right = int(right_side[i])
        if each_right ^ each_key:
            right_side_after_xor.append("1")
        else:
            right_side_after_xor.append("0")
    return right_side_after_xor


def s_box(right_side):
    right_side_8_blocks = []
    for z in range(0, 48, 6):
        right_side_6_bit_block = []
        for q in range(0, 6):
            right_side_6_bit_block.append(right_side[z + q])
        right_side_8_blocks.append(right_side_6_bit_block)

    lookup_table = [[["1110", "0100", "1101", "0001", "0010", "1111", "1011", "1000", "0011", "1010", "0110", "1100",
                      "0101", "1001", "0000", "0111"],
                     ["0000", "1111", "0111", "0100", "1110", "0010", "1101", "0001", "1010", "0110", "1100", "1011",
                      "1001", "0101", "0011", "1000"],
                     ["0100", "0001", "1110", "1000", "1101", "0110", "0010", "1011", "1111", "1100", "1001", "0111",
                      "0011", "1010", "0101", "0000"],
                     ["1111", "1100", "1000", "0010", "0100", "1001", "0001", "0111", "0101", "1011", "0011", "1110",
                      "1010", "0000", "0110", "1101"]],

                    [["1111", "0001", "1000", "1110", "0110", "1011", "0011", "0100", "1001", "0111", "0010", "1101",
                      "1100", "0000", "0101", "1010"],
                     ["0011", "1101", "0100", "0111", "1111", "0010", "1000", "1110", "1100", "0000", "0001", "1010",
                      "0110", "1001", "1011", "0101"],
                     ["0000", "1110", "0111", "1011", "1010", "0100", "1101", "0001", "0101", "1000", "1100", "0110",
                      "1001", "0011", "0010", "1111"],
                     ["1101", "1000", "1010", "0001", "0011", "1111", "0100", "0010", "1011", "0110", "0111", "1100",
                      "0000", "0101", "1110", "1001"]],

                    [["1010", "0000", "1001", "1110", "0110", "0011", "1111", "0101", "0001", "1101", "1100", "0111",
                      "1011", "0100", "0010", "1000"],
                     ["1101", "0111", "0000", "1001", "0011", "0100", "0110", "1010", "0010", "1000", "0101", "1110",
                      "1100", "1011", "1111", "0001"],
                     ["1101", "0110", "0100", "1001", "1000", "1111", "0011", "0000", "1011", "0001", "0010", "1100",
                      "0101", "1010", "1110", "0111"],
                     ["0001", "1010", "1101", "0000", "0110", "1001", "1000", "0111", "0100", "1111", "1110", "0011",
                      "1011", "0101", "0010", "1100"]],

                    [["0111", "1101", "1110", "0011", "0000", "0110", "1001", "1010", "0001", "0010", "1000", "0101",
                      "1011", "1100", "0100", "1111"],
                     ["1101", "1000", "1011", "0101", "0110", "1111", "0000", "0011", "0100", "0111", "0010", "1100",
                      "0001", "1010", "1110", "1001"],
                     ["1010", "0110", "1001", "0000", "1100", "1011", "0111", "1101", "1111", "0001", "0011", "1110",
                      "0101", "0010", "1000", "0100"],
                     ["0011", "1111", "0000", "0110", "1010", "0001", "1101", "1000", "1001", "0100", "0101", "1011",
                      "1100", "0111", "0010", "1110"]],

                    [["0010", "1100", "0100", "0001", "0111", "1010", "1011", "0110", "1000", "0101", "0011", "1111",
                      "1101", "0000", "1110", "1001"],
                     ["1110", "1011", "0010", "1100", "0100", "0111", "1101", "0001", "0101", "0000", "1111", "1010",
                      "0011", "1001", "1000", "0110"],
                     ["0100", "0010", "0001", "1011", "1010", "1101", "0111", "1000", "1111", "1001", "1100", "0101",
                      "0110", "0011", "0000", "1110"],
                     ["1011", "1000", "1100", "0111", "0001", "1110", "0010", "1101", "0110", "1111", "0000", "1001",
                      "1010", "0100", "0101", "0011"]],

                    [["1100", "0001", "1010", "1111", "1001", "0010", "0110", "1000", "0000", "1101", "0011", "0100",
                      "1110", "0111", "0101", "1011"],
                     ["1010", "1111", "0100", "0010", "0111", "1100", "1001", "0101", "0110", "0001", "1101", "1110",
                      "0000", "1011", "0011", "1000"],
                     ["1001", "1110", "1111", "0101", "0010", "1000", "1100", "0011", "0111", "0000", "0100", "1010",
                      "0001", "1101", "1011", "0110"],
                     ["0100", "0011", "0010", "1100", "1001", "0101", "1111", "1010", "1011", "1110", "0001", "0111",
                      "0110", "0000", "1000", "1101"]],

                    [["0100", "1011", "0010", "1110", "1111", "0000", "1000", "1101", "0011", "1100", "1001", "0111",
                      "0101", "1010", "0110", "0001"],
                     ["1101", "0000", "1011", "0111", "0100", "1001", "0001", "1010", "1110", "0011", "0101", "1100",
                      "0010", "1111", "1000", "0110"],
                     ["0001", "0100", "1011", "1101", "1100", "0011", "0111", "1110", "1010", "1111", "0110", "1000",
                      "0000", "0101", "1001", "0010"],
                     ["0110", "1011", "1101", "1000", "0001", "0100", "1010", "0111", "1001", "0101", "0000", "1111",
                      "1110", "0010", "0011", "1100"]],

                    [["1101", "0010", "1000", "0100", "0110", "1111", "1011", "0001", "1010", "1001", "0011", "1110",
                      "0101", "0000", "1100", "0111"],
                     ["0001", "1111", "1101", "1000", "1010", "0011", "0111", "0100", "1100", "0101", "0110", "1011",
                      "0000", "1110", "1001", "0010"],
                     ["0111", "1011", "0100", "0001", "1001", "1100", "1110", "0010", "0000", "0110", "1010", "1101",
                      "1111", "0011", "0101", "1000"],
                     ["0010", "0001", "1110", "0111", "0100", "1010", "1000", "1101", "1111", "1100", "1001", "0000",
                      "0011", "0101", "0110", "1011"]]]

    # right_side_shrink = 8-4 bit string
    right_side_shrink = ""
    for block_num in range(0, 8):
        first_digits = right_side_8_blocks[block_num][0] + right_side_8_blocks[block_num][5]

        if first_digits == "10":
            first_digits = "2"
        elif first_digits == "11":
            first_digits = "3"

        middle_digits = right_side_8_blocks[block_num][1] + right_side_8_blocks[block_num][2] \
                        + right_side_8_blocks[block_num][3] + right_side_8_blocks[block_num][4]

        if middle_digits == "0000":
            middle_digits = 0
        elif middle_digits == "0001":
            middle_digits = 1
        elif middle_digits == "0010":
            middle_digits = 2
        elif middle_digits == "0100":
            middle_digits = 4
        elif middle_digits == "1000":
            middle_digits = 8
        elif middle_digits == "0011":
            middle_digits = 3
        elif middle_digits == "0101":
            middle_digits = 5
        elif middle_digits == "1001":
            middle_digits = 9
        elif middle_digits == "0110":
            middle_digits = 6
        elif middle_digits == "1010":
            middle_digits = 10
        elif middle_digits == "1100":
            middle_digits = 12
        elif middle_digits == "0111":
            middle_digits = 7
        elif middle_digits == "1011":
            middle_digits = 11
        elif middle_digits == "1101":
            middle_digits = 13
        elif middle_digits == "1110":
            middle_digits = 14
        elif middle_digits == "1111":
            middle_digits = 15

        right_side_4_bit_block = lookup_table[block_num][int(first_digits)][middle_digits]
        right_side_shrink += right_side_4_bit_block
    return right_side_shrink


def second_permutation(right_side):
    permutation_order_no_2 = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 8, 31, 10, 2, 8, 24, 14, 32, 27,
                              3, 9, 19, 13, 30, 6, 22, 11, 4, 25]
    permuted_right = []
    for f in range(0, 32):
        permuted_right.append(right_side[permutation_order_no_2[f] - 1])
    return permuted_right


def right_xor_left(right_side, left_side):
    right_xor_left = []
    for b in range(0, 32):
        each_left = int(left_side[b])
        each_right = int(right_side[b])
        if each_right ^ each_left:
            right_xor_left.append("1")
        else:
            right_xor_left.append("0")
    return right_xor_left


def make_ciphertext(left_side, right_side):
    final_left = right_side
    final_right = left_side
    ciphertext = final_left + final_right

    for x in range(0, 64):
        print(ciphertext[x], end="")
    print()
    return ciphertext


def run_encrypt(plaintext, key):
    print('Encryption: Plaintext ' + ''.join(plaintext))
    permuted_plaintext = initial_perm(plaintext)
    print('Encryption: Permuted plaintext ', ''.join(permuted_plaintext))
    right_side = permuted_plaintext[32:64]
    initial_left = permuted_plaintext[0:32]
    initial_right = right_side

    right_side = right_side_expansion(right_side)
    print('Encryption: Expanded Right ', ''.join(right_side))
    right_side = right_xor_key(right_side, key)
    print('Encryption: Right XOR Key ', ''.join(right_side))
    right_side = s_box(right_side)
    print('Encryption: S Box ', ''.join(right_side))
    right_side = second_permutation(right_side)
    print('Encryption: Second Permutation Right Side ', ''.join(right_side))
    initial_left = right_xor_left(right_side, initial_left)
    print('Encryption: Right xor Left ', ''.join(initial_left))
    ciphertext = initial_left + initial_right
    print(''.join(ciphertext))

    return ciphertext


def run_decrypt(ciphertext, key):
    print('Decryption: Ciphertext ' + ''.join(ciphertext))
    left_side = ciphertext[0:32]
    right_side = ciphertext[32:64]
    initial_right_side = right_side
    print('Decryption: Permuted Right Side', ''.join(right_side))

    right_side = right_side_expansion(right_side)
    print("Decryption: Expanded Right ", ''.join(right_side))
    right_side = right_xor_key(right_side, key)
    print("Decryption: Right xor Key ", ''.join(right_side))
    right_side = s_box(right_side)
    print("Decryption: S Box ", ''.join(right_side))
    right_side = second_permutation(right_side)
    print("Decryption: Second Permutation Right Side ", ''.join(right_side))
    left_side = right_xor_left(right_side, left_side)
    print("Decryption: Right xor Left ", ''.join(right_side))
    permuted_plaintext = left_side + initial_right_side
    print("Decryption: Permuted Plaintext", ''.join(permuted_plaintext))
    plaintext = undo(permuted_plaintext)
    print(''.join(plaintext))

    return plaintext
