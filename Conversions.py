import math


def HexToBin(hex):
    b1 = (bin((int(hex, 16)))[2:]).zfill(32)
    return b1

def BinToDec(binStr):
    return int(binStr,2)