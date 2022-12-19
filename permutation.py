PC2 = [
    14, 17, 11, 24, 1, 5, 
    3, 28, 15, 6, 21, 10,
    23, 19, 12, 4, 26, 8,
    16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
]
PC1 = [
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4,
]
# r1s3 : 15 23(real key) 35 59
# r12s4 : 0 1 2 3 4 5 6 7
# 
P = [
    16,  7, 20, 21, 
    29, 12, 28, 17, 
    1, 15, 23, 26, 
    5, 18, 31, 10, 
    2,  8, 24, 14, 
    32, 27,  3,  9, 
    19, 13, 30,  6, 
    22, 11,  4, 25
]

E = [
    32,  1,  2,  3,  4,  5,  
    4,  5,  6,  7,  8,  9,  
    8,  9, 10, 11, 12, 13, 
    12, 13, 14, 15, 16, 17, 
    16, 17, 18, 19, 20, 21, 
    20, 21, 22, 23, 24, 25, 
    24, 25, 26, 27, 28, 29, 
    28, 29, 30, 31, 32,  1
]
def get_loc_from_key_reg_to_subkey():
    shift_num = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1,]

    #KEY = [i for i in range(56)]
    KEY = [0xc4, 0x0e, 0x2a, 0x89, 0x78, 0x10, 0x04, 0xe1]
    a = lambda p: bin(p)[2:].rjust(8, "0")
    KEY = "".join(list(map(a, KEY)))
    EXPANDED = []
    for i in range(len(PC1)):
        EXPANDED.append(KEY[PC1[i] - 1])
    print(EXPANDED)
    LEFT = EXPANDED[:28]
    RIGHT = EXPANDED[28:]
    print(RIGHT)
    ROUDNS = 12
    SUBKEYS = []
    for i in range(ROUDNS):
        SUBKEY = []
        LEFT = LEFT[shift_num[i]:] + LEFT[:shift_num[i]]
        RIGHT = RIGHT[shift_num[i]:] + RIGHT[:shift_num[i]]
        for j in range(len(PC2)):
            if PC2[j] <= 28:
                SUBKEY.append(LEFT[PC2[j] - 1])
            else:
                SUBKEY.append(RIGHT[PC2[j] - 28 - 1])
        unused = []
        for a in range(56):
            if a not in SUBKEY:
                unused.append(a)
        SUBKEYS.append(SUBKEY)
        # print(f"{i + 1}'th SUBKEY's bits are from initail register's {SUBKEY} bits")
        # print(f"{i + 1}'th SUBKEY's bits doesn't have initial register's {unused} bits")
    R1_KEY = SUBKEYS[0]
    R12_KEY = SUBKEYS[11]
    print(R1_KEY)
    print(SUBKEYS[10])
    print(R12_KEY)
    table = []
    for _ in range(10):
        table.append([0 for i in range(10)])
    for i in range(56):
        try:
            if i >= 28:
                R1_Sbox_num = (R1_KEY.index(i) // 6) + 1
            else:
                R1_Sbox_num = (R1_KEY.index(i) // 6)
        except:
            if i >= 28:
                R1_Sbox_num = 9
            else:
                R1_Sbox_num = 4
        try:
            if i >= 28:
                R12_Sbox_num = (R12_KEY.index(i) // 6) + 1
            else:
                R12_Sbox_num = (R12_KEY.index(i) // 6)
        except:
            if i >= 28:
                R12_Sbox_num = 9
            else:
                R12_Sbox_num = 4
        table[R1_Sbox_num][R12_Sbox_num] += 1
    #import pandas as pd
    #df = pd.DataFrame(table, columns=["S1", "S2", "S3", "S4", "X", "S5", "S6", "S7", "S8", "X"])
    #df = df.rename(index={0: 'S1', 1: 'S2', 2: 'S3', 3: 'S4', 4: 'X', 5: "S5", 6: "S6", 7: "S7", 8: "S8", 9: "X"}) #행(row) 이름 바꾸기
    #print(df)
        

def round_to_block():
    result_round = [i for i in range(32)]
    left = []
    for i in range(len(P)):
        left.append(result_round[P[i] - 1])

    print(f"{result_round} => {left}")
    return left

def block_to_round(block):
    expanded = []
    for i in range(len(E)):
        expanded.append(block[E[i] - 1])
    print(f"{block} => {expanded}")

get_loc_from_key_reg_to_subkey()

#block = round_to_block()

#block_to_round(block)


