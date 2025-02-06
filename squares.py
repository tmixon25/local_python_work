# squares=[value**2 for value in range(1,11)]
# print(squares)
#count to 20
# numbers=list(range(1,21))
# for number in numbers:
#     print(number)
# numbers=list(range(1,1_000_001))
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))
# cubes=[]
# for number in range(1,11):
#     cube = number**3
#     cubes.append(cube)
# for cube in cubes:
#     print(cube)
cubes=[number**3 for number in range(1,11)]
for cube in cubes:
    print (cube)