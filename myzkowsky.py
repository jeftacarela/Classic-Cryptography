import math

key = "myzkowsky"
plain = "kriptografi"
print("Message : ", plain)
print("Key : ", key)
key= "".join(key.split(" "))
plain = "".join(plain.split(" "))
cipher=""

def TP(key,plain):
    cipher=""
    arr = [[None for _ in range(len(key))] for _ in range(math.ceil(len(plain) / len(key)) + 1)]
    for x in range(len(key)):
        arr[0][x] = key[x]
    z = 0
    for x in range(1, len(arr)):
        for y in range(len(arr[0])):
            if (z < len(plain)):
                arr[x][y] = plain[z]
                z += 1
            else:
                arr[x][y] = "*"

    tmp = sorted(arr[0])
    indx = [None for _ in range(len(key))]
    z = 0
    print(tmp)
    for x in range(len(tmp)):
        for y in range(len(tmp)):
            if (tmp[x] == arr[0][y]):
                indx[z] = y
                z += 1
                break

    for x in range(len(indx)):
        for y in range(1, len(arr)):
            cipher += str(arr[y][indx[x]])
    cipher = cipher.split("*")
    cipher = "".join(cipher)
    return cipher

cipher=TP(key,plain)
cipher2=TP(key,cipher)
print("Transpos         : ",cipher)
print("Double Transpos  : ",cipher2)