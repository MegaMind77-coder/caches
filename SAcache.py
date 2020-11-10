#4-way set associative cache
#cache is like

#[[[v,tag],[v,tag],[v,tag],[v,tag]],
# [[v,tag],[v,tag],[v,tag],[v,tag]],
# [[v,tag],[v,tag],[v,tag],[v,tag]],
# [[v,tag],[v,tag],[v,tag],[v,tag]],
# .
# .
# .
# [[v,tag],[v,tag],[v,tag],[v,tag]]]

import Conversions
import readTrace

numberOfSets = pow(2,14)
indexBits = 14
tagBits = 16


def BuildSAcache(numSets):
    print('Building Cache')
    cache = []
    for i in range(numSets):
        set1 = [['0'],['0'],['0'],['0']]
        lruSet = [0,1,2,3]
        set1.append(lruSet)
        cache.append(set1)
    print('Built Cache')
    return cache

def StartSAcache(SAcache, binAddr):
    count = 0
    i = 0
    hitCount = 0
    missCount = 0
    while(i<len(binAddr)):
        addr = binAddr[i]
        #print(addr)
        tagStr = addr[0:tagBits]
        #print(tagStr)
        idxStr = addr[tagBits:tagBits+indexBits]
        #print(idxStr)
        intIdx = Conversions.BinToDec(idxStr)
        intIdx = intIdx % numberOfSets
        #print(intIdx)
        validBlocks = []
        

        i+=1


if __name__ == "__main__":
    SAcache = BuildSAcache(numberOfSets)
    binAddr = readTrace.binAddresses
    print(len(binAddr))
    StartSAcache(SAcache, binAddr)


