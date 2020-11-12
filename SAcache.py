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
        set1 = [['0', ''],['0', ''],['0', ''],['0', '']]
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
        #print(intIdx)
        intIdx = intIdx % numberOfSets
        #print(intIdx)
        missFlag = 1
        for x in range(4):
            if(SAcache[intIdx][x][0] == '1'):
                if(SAcache[intIdx][x][1] == tagStr):
                    missFlag = 0
                    (SAcache[intIdx][4]).remove(x)
                    (SAcache[intIdx][4]).append(x)
                    hitCount += 1
        
        if(missFlag == 1):
            chBlock = SAcache[intIdx][4][0]
            if(SAcache[intIdx][chBlock][0] == '0'):
                SAcache[intIdx][chBlock][0] = '1'
            SAcache[intIdx][chBlock][1] = tagStr
            (SAcache[intIdx][4]).remove(chBlock)
            (SAcache[intIdx][4]).append(chBlock)
            missCount += 1

        i+=1
    print(hitCount, missCount)

if __name__ == "__main__":
    SAcache = BuildSAcache(numberOfSets)
    binAddr = readTrace.binAddresses
    print(len(binAddr))
    StartSAcache(SAcache, binAddr)


