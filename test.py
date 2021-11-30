m = "sdjlwdd"
c
print(mBytes)
mInt = int.from_bytes(mBytes, byteorder="big")
mBytes2 = mInt.to_bytes(((mInt.bit_length() + 7) // 8), byteorder="big")
m2 = mBytes2.decode("utf-8")
print(m == m2)