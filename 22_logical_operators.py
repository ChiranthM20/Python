a = 22
b = 88
c = 238

# and

print("a>b and b>c  --> ", a>b and b>c)
print("a<b and b<c  --> ", a<b and b<c)
print("a>b and b<c  --> ", a>b and b<c)

# or

print("a>b or b>c  --> ", a>b or b>c)
print("a<b or b<c  --> ", a<b or b<c)
print("a>b or b<c  --> ", a>b or b<c)

# not

print("not a>b  b>c  --> ", not(a>b or b>c))
print("not a<b  b<c  --> ", not(a<b or b<c))
print("not a>b  b<c  --> ", not(a>b or b<c))
