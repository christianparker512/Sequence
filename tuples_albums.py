welcome = "Welcome to my Nightmare", "alice cooper", 1975
bad = "bad company", "bad company", 1974
budgie = "Nightflight", "budgie", 1981
imelda = "more mayhem", "emilda may", 2011
metallica = "ride the lightning", "metallica", 1984
print(metallica)

print(metallica[0])
print(metallica[1])
print(metallica[2])

metallica2 = list(metallica)
print(metallica2)

metallica2[0] = "Master of Puppets"
print(metallica2)

table = ("Coffee table", 200, 100, 75, 34.50)

print(table[1] * table[2])

name, length, width, height, price = table
print(length * width)