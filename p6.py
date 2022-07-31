# inputs:  Keys P10 and P8 permutations 1D list
#          Plain text (binary); 8 length matrix
#          IP Order, 8 length list
#          EP order, 8 length list
#          Key, length 8 or 16 x 8 matrix
#          S key matrix, 4 x 4 matrix
#          P4 value, length 4 list

keyP10 = [2, 4, 1, 6, 3, 9, 0, 8, 7, 5]
keyP8 = [5, 2, 6, 3, 7, 4, 9, 8]

TEXT_LENGTH = 8
ipTable = [1, 5, 2, 0, 3, 7, 4, 6]
ipInvTable = [3, 0, 2, 4,6, 1, 7, 5]
epTable = [3, 0, 1, 2, 1, 2, 3, 0]
S0 = [[1,0,3,2],
      [3,2,1,0],
      [0,2,1,3],
      [3,1,3,2]]
S1=  [[0,1,2,3],
      [2,0,1,3],
      [3,0,1,0],
      [2,1,0,3]]
p4Table = [1,3,2,0]

def shift_left(k, nth_shifts):
	s = list()
	for i in range(nth_shifts):
		for j in range(1,len(k)):
			s.append(k[j])
		s.append(k[0])
		k = s
		s = list()
	return k

def keyGeneration(p10Table, p8Table, key):
    finalKey = list()
    step1Key = list()
    for i in range(0, 10):
        step1Key.append(key[p10Table[i]])
    l = step1Key[:5]
    r = step1Key[5:]
    for z in range(1, 3):
        l = shift_left(l, z)
        r = shift_left(r, z)
        combineKey = l + r
        fk = list()
        for i in range(0, 8):
            fk.append(combineKey[p8Table[i]])
        finalKey.append(fk)

    return finalKey

def xor(a, b):
	ans = list()
	for i in range(len(a)):
		if a[i] == b[i]:
			ans.append(0)
		else:
			ans.append(1)
	return ans

def binToDec(val):
    return int(val,2)

def decToBin(val):
    return list(map(lambda x:int(x), [char for char in format(val, 'b')]))

def switchBoxResults(sMatrix, a):
  return decToBin(sMatrix[ binToDec(str(a[0]) + str(a[3])) ][ binToDec(str(a[1]) + str(a[2])) ])

def fBoxResult(arrLeft, arrRight, key):
    epRes = list()
    for i in range(0, 8):
        epRes.append(arrRight[epTable[i]])
    xorRes = xor(epRes, key)
    l1 = xorRes[:4]
    r1 = xorRes[4:]
    s0Val = switchBoxResults(S0, l1)
    s1Val = switchBoxResults(S1, r1)
    combineSbox = s0Val + s1Val
    p4Res = list()
    for i in range(0, 4):
        p4Res.append(combineSbox[p4Table[i]])
    p4XorRes = xor(arrLeft, p4Res)
    return p4XorRes

def encryptText(pt, key): 
    ipRes = list()
    for i in range(0, 8):
        ipRes.append(pt[ipTable[i]])
    l = ipRes[:4]
    r = ipRes[4:]
    fBoxResOne = fBoxResult(l, r, key[0])
    fBoxResTwo = fBoxResult(r, fBoxResOne, key[1])
    roundTwoRes = fBoxResTwo + fBoxResOne
    cipher = list()
    for i in range(0, 8):
        cipher.append(roundTwoRes[ipInvTable[i]])
    return cipher


inputKey = [1, 0, 1, 0, 0, 0, 0, 0, 1, 0]
print("Input Key Taken: ", inputKey)
getKey = keyGeneration(keyP10, keyP8, inputKey)
print("K1 Generated: ", getKey[0])
print("K2 Generated: ", getKey[1])

plainText = [1, 0, 0, 1, 0, 1, 1, 1]
print("\n\nPlain Text Taken: ", plainText)
cipherText = encryptText(plainText, getKey)
print("Cipher Text: ", cipherText)
