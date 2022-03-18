n = [2,4,6,8,10,12,14,16,18,20]
print("list of integers:")
print(n)
print("Square every number in list:")
square = list(map(lambda x: x ** 2, n))
print(square)
print("Cube every number in list:")
cube = list(map(lambda x: x ** 3, n))
print(cube)