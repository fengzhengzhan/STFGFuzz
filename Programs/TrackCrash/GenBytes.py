import binascii

HEX_ASCII = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '0a', '0b', '0c', '0d', '0e', '0f', '10', '11',
             '12', '13', '14', '15', '16', '17', '18', '19', '1a', '1b', '1c', '1d', '1e', '1f', '20', '21', '22', '23',
             '24', '25', '26', '27', '28', '29', '2a', '2b', '2c', '2d', '2e', '2f', '30', '31', '32', '33', '34', '35',
             '36', '37', '38', '39', '3a', '3b', '3c', '3d', '3e', '3f', '40', '41', '42', '43', '44', '45', '46', '47',
             '48', '49', '4a', '4b', '4c', '4d', '4e', '4f', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59',
             '5a', '5b', '5c', '5d', '5e', '5f', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '6a', '6b',
             '6c', '6d', '6e', '6f', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '7a', '7b', '7c', '7d',
             '7e', '7f', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '8a', '8b', '8c', '8d', '8e', '8f',
             '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '9a', '9b', '9c', '9d', '9e', '9f', 'a0', 'a1',
             'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'aa', 'ab', 'ac', 'ad', 'ae', 'af', 'b0', 'b1', 'b2', 'b3',
             'b4', 'b5', 'b6', 'b7', 'b8', 'b9', 'ba', 'bb', 'bc', 'bd', 'be', 'bf', 'c0', 'c1', 'c2', 'c3', 'c4', 'c5',
             'c6', 'c7', 'c8', 'c9', 'ca', 'cb', 'cc', 'cd', 'ce', 'cf', 'd0', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7',
             'd8', 'd9', 'da', 'db', 'dc', 'dd', 'de', 'df', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9',
             'ea', 'eb', 'ec', 'ed', 'ee', 'ef', 'f0', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'fa', 'fb',
             'fc', 'fd', 'fe', 'ff']

BYTES_ASCII = [b'\x00', b'\x01', b'\x02', b'\x03', b'\x04', b'\x05', b'\x06', b'\x07', b'\x08', b'\t', b'\n', b'\x0b',
               b'\x0c', b'\r', b'\x0e', b'\x0f', b'\x10', b'\x11', b'\x12', b'\x13', b'\x14', b'\x15', b'\x16', b'\x17',
               b'\x18', b'\x19', b'\x1a', b'\x1b', b'\x1c', b'\x1d', b'\x1e', b'\x1f', b' ', b'!', b'"', b'#', b'$',
               b'%', b'&', b"'", b'(', b')', b'*', b'+', b',', b'-', b'.', b'/', b'0', b'1', b'2', b'3', b'4', b'5',
               b'6', b'7', b'8', b'9', b':', b';', b'<', b'=', b'>', b'?', b'@', b'A', b'B', b'C', b'D', b'E', b'F',
               b'G', b'H', b'I', b'J', b'K', b'L', b'M', b'N', b'O', b'P', b'Q', b'R', b'S', b'T', b'U', b'V', b'W',
               b'X', b'Y', b'Z', b'[', b'\\', b']', b'^', b'_', b'`', b'a', b'b', b'c', b'd', b'e', b'f', b'g', b'h',
               b'i', b'j', b'k', b'l', b'm', b'n', b'o', b'p', b'q', b'r', b's', b't', b'u', b'v', b'w', b'x', b'y',
               b'z', b'{', b'|', b'}', b'~', b'\x7f', b'\x80', b'\x81', b'\x82', b'\x83', b'\x84', b'\x85', b'\x86',
               b'\x87', b'\x88', b'\x89', b'\x8a', b'\x8b', b'\x8c', b'\x8d', b'\x8e', b'\x8f', b'\x90', b'\x91',
               b'\x92', b'\x93', b'\x94', b'\x95', b'\x96', b'\x97', b'\x98', b'\x99', b'\x9a', b'\x9b', b'\x9c',
               b'\x9d', b'\x9e', b'\x9f', b'\xa0', b'\xa1', b'\xa2', b'\xa3', b'\xa4', b'\xa5', b'\xa6', b'\xa7',
               b'\xa8', b'\xa9', b'\xaa', b'\xab', b'\xac', b'\xad', b'\xae', b'\xaf', b'\xb0', b'\xb1', b'\xb2',
               b'\xb3', b'\xb4', b'\xb5', b'\xb6', b'\xb7', b'\xb8', b'\xb9', b'\xba', b'\xbb', b'\xbc', b'\xbd',
               b'\xbe', b'\xbf', b'\xc0', b'\xc1', b'\xc2', b'\xc3', b'\xc4', b'\xc5', b'\xc6', b'\xc7', b'\xc8',
               b'\xc9', b'\xca', b'\xcb', b'\xcc', b'\xcd', b'\xce', b'\xcf', b'\xd0', b'\xd1', b'\xd2', b'\xd3',
               b'\xd4', b'\xd5', b'\xd6', b'\xd7', b'\xd8', b'\xd9', b'\xda', b'\xdb', b'\xdc', b'\xdd', b'\xde',
               b'\xdf', b'\xe0', b'\xe1', b'\xe2', b'\xe3', b'\xe4', b'\xe5', b'\xe6', b'\xe7', b'\xe8', b'\xe9',
               b'\xea', b'\xeb', b'\xec', b'\xed', b'\xee', b'\xef', b'\xf0', b'\xf1', b'\xf2', b'\xf3', b'\xf4',
               b'\xf5', b'\xf6', b'\xf7', b'\xf8', b'\xf9', b'\xfa', b'\xfb', b'\xfc', b'\xfd', b'\xfe', b'\xff']

BYTES_DICT = {b'\x00': 0, b'\x01': 1, b'\x02': 2, b'\x03': 3, b'\x04': 4, b'\x05': 5, b'\x06': 6, b'\x07': 7,
              b'\x08': 8, b'\t': 9, b'\n': 10, b'\x0b': 11, b'\x0c': 12, b'\r': 13, b'\x0e': 14, b'\x0f': 15,
              b'\x10': 16, b'\x11': 17, b'\x12': 18, b'\x13': 19, b'\x14': 20, b'\x15': 21, b'\x16': 22, b'\x17': 23,
              b'\x18': 24, b'\x19': 25, b'\x1a': 26, b'\x1b': 27, b'\x1c': 28, b'\x1d': 29, b'\x1e': 30, b'\x1f': 31,
              b' ': 32, b'!': 33, b'"': 34, b'#': 35, b'$': 36, b'%': 37, b'&': 38, b"'": 39, b'(': 40, b')': 41,
              b'*': 42, b'+': 43, b',': 44, b'-': 45, b'.': 46, b'/': 47, b'0': 48, b'1': 49, b'2': 50, b'3': 51,
              b'4': 52, b'5': 53, b'6': 54, b'7': 55, b'8': 56, b'9': 57, b':': 58, b';': 59, b'<': 60, b'=': 61,
              b'>': 62, b'?': 63, b'@': 64, b'A': 65, b'B': 66, b'C': 67, b'D': 68, b'E': 69, b'F': 70, b'G': 71,
              b'H': 72, b'I': 73, b'J': 74, b'K': 75, b'L': 76, b'M': 77, b'N': 78, b'O': 79, b'P': 80, b'Q': 81,
              b'R': 82, b'S': 83, b'T': 84, b'U': 85, b'V': 86, b'W': 87, b'X': 88, b'Y': 89, b'Z': 90, b'[': 91,
              b'\\': 92, b']': 93, b'^': 94, b'_': 95, b'`': 96, b'a': 97, b'b': 98, b'c': 99, b'd': 100, b'e': 101,
              b'f': 102, b'g': 103, b'h': 104, b'i': 105, b'j': 106, b'k': 107, b'l': 108, b'm': 109, b'n': 110,
              b'o': 111, b'p': 112, b'q': 113, b'r': 114, b's': 115, b't': 116, b'u': 117, b'v': 118, b'w': 119,
              b'x': 120, b'y': 121, b'z': 122, b'{': 123, b'|': 124, b'}': 125, b'~': 126, b'\x7f': 127, b'\x80': 128,
              b'\x81': 129, b'\x82': 130, b'\x83': 131, b'\x84': 132, b'\x85': 133, b'\x86': 134, b'\x87': 135,
              b'\x88': 136, b'\x89': 137, b'\x8a': 138, b'\x8b': 139, b'\x8c': 140, b'\x8d': 141, b'\x8e': 142,
              b'\x8f': 143, b'\x90': 144, b'\x91': 145, b'\x92': 146, b'\x93': 147, b'\x94': 148, b'\x95': 149,
              b'\x96': 150, b'\x97': 151, b'\x98': 152, b'\x99': 153, b'\x9a': 154, b'\x9b': 155, b'\x9c': 156,
              b'\x9d': 157, b'\x9e': 158, b'\x9f': 159, b'\xa0': 160, b'\xa1': 161, b'\xa2': 162, b'\xa3': 163,
              b'\xa4': 164, b'\xa5': 165, b'\xa6': 166, b'\xa7': 167, b'\xa8': 168, b'\xa9': 169, b'\xaa': 170,
              b'\xab': 171, b'\xac': 172, b'\xad': 173, b'\xae': 174, b'\xaf': 175, b'\xb0': 176, b'\xb1': 177,
              b'\xb2': 178, b'\xb3': 179, b'\xb4': 180, b'\xb5': 181, b'\xb6': 182, b'\xb7': 183, b'\xb8': 184,
              b'\xb9': 185, b'\xba': 186, b'\xbb': 187, b'\xbc': 188, b'\xbd': 189, b'\xbe': 190, b'\xbf': 191,
              b'\xc0': 192, b'\xc1': 193, b'\xc2': 194, b'\xc3': 195, b'\xc4': 196, b'\xc5': 197, b'\xc6': 198,
              b'\xc7': 199, b'\xc8': 200, b'\xc9': 201, b'\xca': 202, b'\xcb': 203, b'\xcc': 204, b'\xcd': 205,
              b'\xce': 206, b'\xcf': 207, b'\xd0': 208, b'\xd1': 209, b'\xd2': 210, b'\xd3': 211, b'\xd4': 212,
              b'\xd5': 213, b'\xd6': 214, b'\xd7': 215, b'\xd8': 216, b'\xd9': 217, b'\xda': 218, b'\xdb': 219,
              b'\xdc': 220, b'\xdd': 221, b'\xde': 222, b'\xdf': 223, b'\xe0': 224, b'\xe1': 225, b'\xe2': 226,
              b'\xe3': 227, b'\xe4': 228, b'\xe5': 229, b'\xe6': 230, b'\xe7': 231, b'\xe8': 232, b'\xe9': 233,
              b'\xea': 234, b'\xeb': 235, b'\xec': 236, b'\xed': 237, b'\xee': 238, b'\xef': 239, b'\xf0': 240,
              b'\xf1': 241, b'\xf2': 242, b'\xf3': 243, b'\xf4': 244, b'\xf5': 245, b'\xf6': 246, b'\xf7': 247,
              b'\xf8': 248, b'\xf9': 249, b'\xfa': 250, b'\xfb': 251, b'\xfc': 252, b'\xfd': 253, b'\xfe': 254,
              b'\xff': 255}

BYTESHEX_DICT = {b'\x00': '0x0', b'\x01': '0x1', b'\x02': '0x2', b'\x03': '0x3', b'\x04': '0x4', b'\x05': '0x5',
              b'\x06': '0x6', b'\x07': '0x7', b'\x08': '0x8', b'\t': '0x9', b'\n': '0xa', b'\x0b': '0xb',
              b'\x0c': '0xc', b'\r': '0xd', b'\x0e': '0xe', b'\x0f': '0xf', b'\x10': '0x10', b'\x11': '0x11',
              b'\x12': '0x12', b'\x13': '0x13', b'\x14': '0x14', b'\x15': '0x15', b'\x16': '0x16', b'\x17': '0x17',
              b'\x18': '0x18', b'\x19': '0x19', b'\x1a': '0x1a', b'\x1b': '0x1b', b'\x1c': '0x1c', b'\x1d': '0x1d',
              b'\x1e': '0x1e', b'\x1f': '0x1f', b' ': '0x20', b'!': '0x21', b'"': '0x22', b'#': '0x23', b'$': '0x24',
              b'%': '0x25', b'&': '0x26', b"'": '0x27', b'(': '0x28', b')': '0x29', b'*': '0x2a', b'+': '0x2b',
              b',': '0x2c', b'-': '0x2d', b'.': '0x2e', b'/': '0x2f', b'0': '0x30', b'1': '0x31', b'2': '0x32',
              b'3': '0x33', b'4': '0x34', b'5': '0x35', b'6': '0x36', b'7': '0x37', b'8': '0x38', b'9': '0x39',
              b':': '0x3a', b';': '0x3b', b'<': '0x3c', b'=': '0x3d', b'>': '0x3e', b'?': '0x3f', b'@': '0x40',
              b'A': '0x41', b'B': '0x42', b'C': '0x43', b'D': '0x44', b'E': '0x45', b'F': '0x46', b'G': '0x47',
              b'H': '0x48', b'I': '0x49', b'J': '0x4a', b'K': '0x4b', b'L': '0x4c', b'M': '0x4d', b'N': '0x4e',
              b'O': '0x4f', b'P': '0x50', b'Q': '0x51', b'R': '0x52', b'S': '0x53', b'T': '0x54', b'U': '0x55',
              b'V': '0x56', b'W': '0x57', b'X': '0x58', b'Y': '0x59', b'Z': '0x5a', b'[': '0x5b', b'\\': '0x5c',
              b']': '0x5d', b'^': '0x5e', b'_': '0x5f', b'`': '0x60', b'a': '0x61', b'b': '0x62', b'c': '0x63',
              b'd': '0x64', b'e': '0x65', b'f': '0x66', b'g': '0x67', b'h': '0x68', b'i': '0x69', b'j': '0x6a',
              b'k': '0x6b', b'l': '0x6c', b'm': '0x6d', b'n': '0x6e', b'o': '0x6f', b'p': '0x70', b'q': '0x71',
              b'r': '0x72', b's': '0x73', b't': '0x74', b'u': '0x75', b'v': '0x76', b'w': '0x77', b'x': '0x78',
              b'y': '0x79', b'z': '0x7a', b'{': '0x7b', b'|': '0x7c', b'}': '0x7d', b'~': '0x7e', b'\x7f': '0x7f',
              b'\x80': '0x80', b'\x81': '0x81', b'\x82': '0x82', b'\x83': '0x83', b'\x84': '0x84', b'\x85': '0x85',
              b'\x86': '0x86', b'\x87': '0x87', b'\x88': '0x88', b'\x89': '0x89', b'\x8a': '0x8a', b'\x8b': '0x8b',
              b'\x8c': '0x8c', b'\x8d': '0x8d', b'\x8e': '0x8e', b'\x8f': '0x8f', b'\x90': '0x90', b'\x91': '0x91',
              b'\x92': '0x92', b'\x93': '0x93', b'\x94': '0x94', b'\x95': '0x95', b'\x96': '0x96', b'\x97': '0x97',
              b'\x98': '0x98', b'\x99': '0x99', b'\x9a': '0x9a', b'\x9b': '0x9b', b'\x9c': '0x9c', b'\x9d': '0x9d',
              b'\x9e': '0x9e', b'\x9f': '0x9f', b'\xa0': '0xa0', b'\xa1': '0xa1', b'\xa2': '0xa2', b'\xa3': '0xa3',
              b'\xa4': '0xa4', b'\xa5': '0xa5', b'\xa6': '0xa6', b'\xa7': '0xa7', b'\xa8': '0xa8', b'\xa9': '0xa9',
              b'\xaa': '0xaa', b'\xab': '0xab', b'\xac': '0xac', b'\xad': '0xad', b'\xae': '0xae', b'\xaf': '0xaf',
              b'\xb0': '0xb0', b'\xb1': '0xb1', b'\xb2': '0xb2', b'\xb3': '0xb3', b'\xb4': '0xb4', b'\xb5': '0xb5',
              b'\xb6': '0xb6', b'\xb7': '0xb7', b'\xb8': '0xb8', b'\xb9': '0xb9', b'\xba': '0xba', b'\xbb': '0xbb',
              b'\xbc': '0xbc', b'\xbd': '0xbd', b'\xbe': '0xbe', b'\xbf': '0xbf', b'\xc0': '0xc0', b'\xc1': '0xc1',
              b'\xc2': '0xc2', b'\xc3': '0xc3', b'\xc4': '0xc4', b'\xc5': '0xc5', b'\xc6': '0xc6', b'\xc7': '0xc7',
              b'\xc8': '0xc8', b'\xc9': '0xc9', b'\xca': '0xca', b'\xcb': '0xcb', b'\xcc': '0xcc', b'\xcd': '0xcd',
              b'\xce': '0xce', b'\xcf': '0xcf', b'\xd0': '0xd0', b'\xd1': '0xd1', b'\xd2': '0xd2', b'\xd3': '0xd3',
              b'\xd4': '0xd4', b'\xd5': '0xd5', b'\xd6': '0xd6', b'\xd7': '0xd7', b'\xd8': '0xd8', b'\xd9': '0xd9',
              b'\xda': '0xda', b'\xdb': '0xdb', b'\xdc': '0xdc', b'\xdd': '0xdd', b'\xde': '0xde', b'\xdf': '0xdf',
              b'\xe0': '0xe0', b'\xe1': '0xe1', b'\xe2': '0xe2', b'\xe3': '0xe3', b'\xe4': '0xe4', b'\xe5': '0xe5',
              b'\xe6': '0xe6', b'\xe7': '0xe7', b'\xe8': '0xe8', b'\xe9': '0xe9', b'\xea': '0xea', b'\xeb': '0xeb',
              b'\xec': '0xec', b'\xed': '0xed', b'\xee': '0xee', b'\xef': '0xef', b'\xf0': '0xf0', b'\xf1': '0xf1',
              b'\xf2': '0xf2', b'\xf3': '0xf3', b'\xf4': '0xf4', b'\xf5': '0xf5', b'\xf6': '0xf6', b'\xf7': '0xf7',
              b'\xf8': '0xf8', b'\xf9': '0xf9', b'\xfa': '0xfa', b'\xfb': '0xfb', b'\xfc': '0xfc', b'\xfd': '0xfd',
              b'\xfe': '0xfe', b'\xff': '0xff', }


def numToHexChar(num):
    h = str(hex(num)[2:])

    l = []
    for i in range(0, len(h), 2):
        l.append(h[i:i + 2])
    # print(l)
    print(h)

    for one in l:
        print("\\x{}".format(one), end="")
    print()
    for one in l[::-1]:
        print("\\x{}".format(one), end="")
    print()

    for one in l:
        print("{}".format(chr(int(one, 16))), end="")
    print()
    for one in l[::-1]:
        print("{}".format(chr(int(one, 16))), end="")
    print()
    print()


def hexToNum(num):
    num = "0x" + str(num)
    intnum = int(num, 16)
    print(intnum)
    return intnum


# a = 'aabbccddeeff'
# a_bytes = bytes.fromhex(a)
# print(a_bytes)
# # b'\xaa\xbb\xcc\xdd\xee\xff'
# aa = a_bytes.hex()
# print(aa)
# aabbccddeeff

# for i in HEX_ASCII:
#     # print("'{:0>2}',".format(hex(i)[2:]), end=" ")
#     print(bytes.fromhex(i))
#
# print(bytes.fromhex("".join(HEX_ASCII[65:91])))

# x = bytes.fromhex("".join(HEX_ASCII[65:91]))
# print(x[0:])
#
# for i in HEX_ASCII:
#     print(bytes.fromhex(i),end=", ")

# print(b'\\')
# print(len(BYTES_ASCII))

# print(hex(1818326372))
# x = '\x6c\x61\x75\x64'

# numToHexChar(1818326624)
# numToHexChar(1618370924)
#
i = hexToNum('14dc2228')  # 349970984
numToHexChar(i)
i = hexToNum('2822dc14')  # 673373204
numToHexChar(i)

# 1818326624
i = hexToNum('7f454c46')
i = hexToNum('464c45')
numToHexChar(i)
#
numToHexChar(3883718427)
numToHexChar(305419896)
numToHexChar(573855352)
numToHexChar(305419896)
# numToHexChar(573855352)


# for i, one in enumerate(BYTES_ASCII):
#     print("{}:'{}',".format(one, hex(i)), end=" ")
#
# print(int('0xAAAA',16))
# print(int('0xc7ff',16))
# print(int('0xcaff',16))
# print(int('0xC0DE',16))