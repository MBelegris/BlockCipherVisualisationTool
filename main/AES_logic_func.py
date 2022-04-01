# Logic for AES encryption and decryption

def GF_mul(byte_1, byte_2):
    p = 0
    hiBitSet = 0
    for i in range(8):
        if byte_2 & 1 == 1:
            p ^= byte_1
        hiBitSet = byte_1 & 0x80
        byte_1 <<= 1
        if hiBitSet == 0x80:
            byte_1 ^= 0x1b
        byte_2 >>= 1
    return p % 256


# Assumes that padded text has 0x at the front
def add_padding(unpadded_text, n):
    unpadded_text = str(unpadded_text[2:])
    if len(unpadded_text) < n:
        unpadded_text = unpadded_text.zfill(n)
    txt = "0" + str(n) + "x"
    unpadded_text = format(int(unpadded_text, base=16), txt)
    return unpadded_text


def make_table(hex_string):
    # arrangement = [[b0, b4, b8, b12],
    #               [b1, b5, b9, b13],
    #               [b2, b6, b10, b14],
    #               [b3, b7, b11, b15]

    table = [["", "", "", ""],
             ["", "", "", ""],
             ["", "", "", ""],
             ["", "", "", ""]]
    count = 0
    for columns in range(0, 4):
        for rows in range(0, 4):
            table[rows][columns] = hex_string[count] + hex_string[count + 1]
            count += 2
    return table


def add_round_key(text, key):
    for columns in range(0, 4):
        for rows in range(0, 4):
            plain_value = hex(int(text[rows][columns], base=16))
            key_value = hex(int(key[rows][columns], base=16))
            text[rows][columns] = add_padding(hex(int(plain_value, base=16) ^ int(key_value, base=16)), 2)
    return text


def s_box(plaintext):
    s_box = [[0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76],
             [0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0],
             [0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15],
             [0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75],
             [0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84],
             [0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF],
             [0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8],
             [0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2],
             [0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73],
             [0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB],
             [0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79],
             [0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08],
             [0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A],
             [0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E],
             [0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF],
             [0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16]]
    plaintext_copy = plaintext
    for rows in range(0, 4):
        for columns in range(0, 4):
            s_box_row = int(plaintext[rows][columns][0], base=16)
            s_box_column = int(plaintext[rows][columns][1], base=16)
            plaintext_copy[rows][columns] = add_padding(hex(s_box[s_box_row][s_box_column]), 2)
    plaintext = plaintext_copy
    return plaintext


def shift_rows(plaintext):
    for i in range(0, 4):
        first_value = plaintext[i][0]
        second_value = plaintext[i][1]
        third_value = plaintext[i][2]
        fourth_value = plaintext[i][3]
        tmp = plaintext[i]

        if i == 1:
            tmp[0] = second_value
            tmp[1] = third_value
            tmp[2] = fourth_value
            tmp[3] = first_value
        if i == 2:
            tmp[0] = third_value
            tmp[1] = fourth_value
            tmp[2] = first_value
            tmp[3] = second_value
        if i == 3:
            tmp[0] = fourth_value
            tmp[1] = first_value
            tmp[2] = second_value
            tmp[3] = third_value
        plaintext[i] = tmp
    return plaintext


def mix_columns(plaintext):
    matrix = [[2, 3, 1, 1],
              [1, 2, 3, 1],
              [1, 1, 2, 3],
              [3, 1, 1, 2]]
    ptxt_columns = [["", "", "", ""],
                    ["", "", "", ""],
                    ["", "", "", ""],
                    ["", "", "", ""]]

    for x in range(0, 4):
        for y in range(0, 4):
            ptxt_columns[x][y] = plaintext[y][x]

    out = 0
    result = [["", "", "", ""],
              ["", "", "", ""],
              ["", "", "", ""],
              ["", "", "", ""]]

    for row in range(0, 4):
        each_row = ptxt_columns[row]
        for matrix_row in range(0, 4):
            each_matrix_row = matrix[matrix_row]
            for matrix_column in range(0, 4):
                x = int(each_row[matrix_column], base=16)
                y = each_matrix_row[matrix_column]
                if y == 2:
                    x = x << 1
                if y == 3:
                    x ^= (x << 1)
                if x > 255:
                    x = x ^ 0x11B
                out ^= x
            result[row][matrix_row] = out
            out = 0

    for rows in range(0, 4):
        for columns in range(0, 4):
            plaintext[rows][columns] = add_padding(hex(result[columns][rows]), 2)

    return plaintext


def inv_shift_rows(ciphertext):
    for i in range(0, 4):
        first_value = ciphertext[i][0]
        second_value = ciphertext[i][1]
        third_value = ciphertext[i][2]
        fourth_value = ciphertext[i][3]

        if i == 1:
            ciphertext[i][0] = fourth_value
            ciphertext[i][1] = first_value
            ciphertext[i][2] = second_value
            ciphertext[i][3] = third_value
        if i == 2:
            ciphertext[i][0] = third_value
            ciphertext[i][1] = fourth_value
            ciphertext[i][2] = first_value
            ciphertext[i][3] = second_value
        if i == 3:
            ciphertext[i][0] = second_value
            ciphertext[i][1] = third_value
            ciphertext[i][2] = fourth_value
            ciphertext[i][3] = first_value
    return ciphertext


def inv_s_box(ciphertext):
    inverted_s_box = [[0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB],
                      [0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB],
                      [0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E],
                      [0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25],
                      [0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92],
                      [0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84],
                      [0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06],
                      [0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B],
                      [0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73],
                      [0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E],
                      [0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B],
                      [0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4],
                      [0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F],
                      [0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF],
                      [0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61],
                      [0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D]]
    ciphertext_copy = ciphertext
    for rows in range(0, 4):
        for columns in range(0, 4):
            s_box_row = int(ciphertext[rows][columns][0], base=16)
            s_box_column = int(ciphertext[rows][columns][1], base=16)
            ciphertext_copy[rows][columns] = add_padding(hex(inverted_s_box[s_box_row][s_box_column]), 2)
    return ciphertext_copy


def inv_mix_columns(ciphertext):
    matrix = [[0x0e, 0x0b, 0x0d, 0x09],
              [0x09, 0x0e, 0x0b, 0x0d],
              [0x0d, 0x09, 0x0e, 0x0b],
              [0x0b, 0x0d, 0x09, 0x0e]]

    ciphertext_columns = [["", "", "", ""],
                          ["", "", "", ""],
                          ["", "", "", ""],
                          ["", "", "", ""]]
    result = [["", "", "", ""],
              ["", "", "", ""],
              ["", "", "", ""],
              ["", "", "", ""]]

    for rows in range(0, 4):
        for columns in range(0, 4):
            ciphertext_columns[columns][rows] = ciphertext[rows][columns]
    out = 0
    for row in range(0, 4):
        each_row = ciphertext_columns[row]
        for matrix_row in range(0, 4):
            each_matrix_row = matrix[matrix_row]
            for matrix_column in range(0, 4):
                x = int(each_row[matrix_column], base=16)
                y = each_matrix_row[matrix_column]
                out ^= GF_mul(x, y)
            result[row][matrix_row] = add_padding(hex(out), 2)
            out = 0
    ciphertext_columns = result

    for row in range(0, 4):
        for columns in range(0, 4):
            ciphertext[row][columns] = ciphertext_columns[columns][row]

    return ciphertext


def do_encrypt(plaintext, key_1, key_2):
    ptxt = make_table(plaintext)
    k_1 = make_table(key_1)
    k_2 = make_table(key_2)
    print("\nMake table")
    for i in range(0, 4):
        print(ptxt[i])

    ptxt = add_round_key(ptxt, k_1)
    print("\nAdd Round Key")
    for i in range(0, 4):
        print(ptxt[i])

    ptxt = s_box(ptxt)
    print("\nS Box")
    for i in range(0, 4):
        print(ptxt[i])

    ptxt = shift_rows(ptxt)
    print("\nShift Rows")
    for i in range(0, 4):
        print(ptxt[i])

    ptxt = mix_columns(ptxt)
    print("\nMix Columns")
    for i in range(0, 4):
        print(ptxt[i])

    ptxt = add_round_key(ptxt, k_2)
    print("\nAdd Round Key")
    for i in range(0, 4):
        print(ptxt[i])

    ciphertext = ""
    for rows in range(0, 4):
        for columns in range(0, 4):
            ciphertext += str(ptxt[columns][rows])
    ciphertext = '0x' + ciphertext
    print()
    print(ciphertext)
    return ciphertext


def do_decrypt(ciphertext, key_1, key_2):
    ciphertext = add_padding(ciphertext, 32)
    key_1 = add_padding(key_1, 32)
    key_2 = add_padding(key_2, 32)
    ciphertext = make_table(ciphertext)
    k_1 = make_table(key_1)
    k_2 = make_table(key_2)
    print("\nMake Table")
    for i in range(0, 4):
        print(ciphertext[i])

    ciphertext = add_round_key(ciphertext, k_2)
    print("\nAdd Round Key")
    for i in range(0, 4):
        print(ciphertext[i])

    ciphertext = inv_mix_columns(ciphertext)
    print("\nInvert Mix Columns")
    for i in range(0, 4):
        print(ciphertext[i])

    ciphertext = inv_shift_rows(ciphertext)
    print("\nInvert Shift Rows")
    for i in range(0, 4):
        print(ciphertext[i])

    ciphertext = inv_s_box(ciphertext)
    print("\nInvert S Box")
    for i in range(0, 4):
        print(ciphertext[i])

    ciphertext = add_round_key(ciphertext, k_1)
    print("\nAdd Round Key")
    for i in range(0, 4):
        print(ciphertext[i])

    plaintext = ""
    for rows in range(0, 4):
        for columns in range(0, 4):
            plaintext += str(ciphertext[columns][rows])
    plaintext = '0x' + plaintext
    print()
    print(plaintext)
    return plaintext
