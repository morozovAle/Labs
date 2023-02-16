import random

INT_BITS = 32
ROUNDS = 16

DATA_BLOCK_WIDE = 32
S_BLOCK_WIDE = 4
MAGIC_ROTATE = 11
KEY_SIZE = int(ROUNDS * DATA_BLOCK_WIDE / S_BLOCK_WIDE)
S_BLOCKS = int(2 * DATA_BLOCK_WIDE / S_BLOCK_WIDE)

s = [[[0 for x in range(int(2 ** S_BLOCK_WIDE))] for y in range(S_BLOCKS)] for z in range(ROUNDS)]  # 16 16 16


def generate(studentNum):
    random.seed(studentNum)
    for r in range(0, len(s)):
        print("ROUND: {}".format(r))
        for i in range(0, len(s[r])):
            print("  {", end='')
            for j in range(0, len(s[r][i])):
                s[r][i][j] = random.randint(0, len(s[r][i]) - 1)
                print("  {},".format(s[r][i][j]), end='')
            print("},")


def str2int(s):
    rez = 0
    for i in range(0, 4):
        rez |= (ord(s[i]) & 255) << (i * 8)
    return rez


def int2str(l):
    rez = ""
    for i in range(0, 4):
        rez += chr(l & 255)
        l >>= 8
    return rez


def leftRotate(n, d):
    return (n << d) | (n >> (INT_BITS - d))


def rightRotate(n, d):
    return (n >> d) | (n << (INT_BITS - d)) & 0xFFFFFFFF


def getValueFromS(numberRound, indexS, value, key):
    return s[numberRound][indexS * 2 + key][value]


def f(r, key, round):
    r = leftRotate(r, MAGIC_ROTATE)

    numOfBlocks = int(S_BLOCKS / 2)
    resultSBlock = [0] * numOfBlocks
    for indexS in range(numOfBlocks):
        currentForBit = (r >> (4 * indexS)) & 0b1111
        resultSBlock[numOfBlocks - 1 - indexS] = getValueFromS(round, indexS, currentForBit, (key >> indexS) & 0b1)

    r = 0
    i = 0
    for elemForBit in resultSBlock:
        r |= elemForBit << (4 * i)
        i += 1

    return r


def crypt(message, pass_key):
    r = str2int(message[:4])
    l = str2int(message[4:8])

    resultF = 0
    for round in range(ROUNDS):
        key = ord(pass_key[round])
        resultF = f(r, key, round)

        temp = r
        r = resultF ^ l
        l = temp

    return int2str(r) + int2str(l)


def decrypt(message, pass_key):
    r = str2int(message[4:8])
    l = str2int(message[:4])

    resultF = 0
    for round in range(ROUNDS - 1, -1, -1):
        key = ord(pass_key[round])
        resultF = f(r, key, round)

        temp = r
        r = resultF ^ l
        l = temp

    return int2str(l) + int2str(r)


def main():
    generate(7)
    str = "suburban"
    pass_key = "wild dragon fire"
    print("==========\nисходные данные(2x32бит): \"{}\"".format(str))
    print("ключ шифрования(128 бит): \"{}\"".format(pass_key))
    rez = crypt(str, pass_key)
    print("зашифрованные данные: ", rez)
    rez = decrypt(rez, pass_key)
    print("расшифрованные данные: ", rez)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()