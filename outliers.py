#data = [4, 5, 104, 105, 110, 120, 130, 130, 150
#        , 160, 170, 183, 185, 187, 188, 191, 350, 360]

#data = [4, 5, 104, 105, 110, 120, 130, 130, 150
#        , 160, 170, 183, 185, 187, 188, 190]
data = [104, 105, 110, 120, 130, 130, 150
        , 160, 170, 183, 185, 187, 188, 191, 350, 360]
del data[0:2]
#print(data)

min_valid = 100
max_valid = 200

stop = 0
for index, value in enumerate(data):
    if value < min_valid or max_valid:
        stop = index
        break

print(stop)
del data[:stop]
print(data)

start = 0
for index in range(len(data) -1, -1, -1):
    #We have the indexs of the last item to keep
    #Set 'STart to the position of th efirst
    #item to delete
    print(index)