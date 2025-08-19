a = [1,3,4,2,5,6,9,22]
b = "Chiranth M"

print(3 in a)

print((3 in a) and ("3" in b))
print((5 in a) and ("h" in b))


print((3 in a) or ("3" in b))
print((5 in a) or ("h" in b))


print(not((3 in a) or ("3" in b)))
print(not((5 in a) or ("h" in b)))

print("h" not in b)