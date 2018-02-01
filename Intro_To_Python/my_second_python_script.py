def cylinder_volume(height, radius):
    pi = 3.14159
    return height * pi * radius ** 2


print(cylinder_volume(25, 2))

print(cylinder_volume(10, 3))


test = ['a','b','c','d','a']

if test[-1] in test[0:-1]:
    print("duplicate of last item found")
