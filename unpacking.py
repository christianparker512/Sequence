a = b = c = d = e = f= 12
print(c)

x, y, z = 1, 2, 37
print(x)
print(y)
print(z)

print("unpacking a tuple")

data = 1, 2, 37
x, y, z = data
print(x)
print(y)
print(z)

print()
data_list = [12,13,14]
# doesn't work because tuples can't be changed
# data_list.append(15)
p,q,r = data_list
print(p)
print(q)
print(r)