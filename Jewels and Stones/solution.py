def numJewelsInStones(J, S):
    setJ = set(J)
    return sum(s in setJ for s in S)

firstJ = 'aA'
firstS = 'aAAbbbb'

secondJ = 'z'
secondS = 'ZZ'

print('First case:', numJewelsInStones(firstJ, firstS))

print('Second case:', numJewelsInStones(secondJ, secondS))