import Conversions
file1 = open("traces/gcc.trace", 'r')

data = file1.readlines()

binAddresses = []

for i in range(len(data)):
    binstr = Conversions.HexToBin(data[i][4:12])
    binAddresses.append(binstr)

