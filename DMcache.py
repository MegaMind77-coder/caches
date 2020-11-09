import Conversions
import readTrace

numberOfBlocks = pow(2,16)
tagBits = 14
indexBits = 16

def buildDMCache(numberOfBlocks):
    print('Building Cache')
    cache = []
    for i in range(numberOfBlocks):
        cache.append(['0'])
    print('Built Cache')
    return cache

def startDMcache(DMcache, binAddr):
    count = 0
    i = 0
    hitCount = 0
    missCount = 0
    while(i<len(binAddr)):
        addr = binAddr[i]
        tagStr = addr[0:tagBits]
        idxStr = addr[tagBits:tagBits+indexBits]
        intIdx = Conversions.BinToDec(idxStr)
        intIdx = intIdx % numberOfBlocks
        validBit = DMcache[intIdx][0]

        if(validBit == '0'):
            DMcache[intIdx].append(tagStr)
            DMcache[intIdx][0] = '1'
            missCount += 1
            #print("MISS")
        else:
            if(DMcache[intIdx][1] == tagStr):
                hitCount += 1
                #print("HIT")
            else:
                DMcache[intIdx][1] = tagStr
                missCount += 1
                #print("MISS")
        i+=1
    print(hitCount,missCount)
        


if __name__ == "__main__":
    DMcache = buildDMCache(numberOfBlocks)
    binAddr = readTrace.binAddresses
    print(len(binAddr))
    startDMcache(DMcache, binAddr)
