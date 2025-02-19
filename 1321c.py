from cffi.backend_ctypes import unicode

someString = "bacabcab"
for i in range(0, len(someString)):
    a = ord(someString[i])
    print(a)

