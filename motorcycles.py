motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
motorcycles[0]='ducati'
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)
motorcycles.insert(0,'schwin')
print(motorcycles)
del motorcycles[1]
print(motorcycles)
popped_motorcycle=motorcycles.pop()
print(motorcycles)
print (popped_motorcycle)
last_owned=motorcycles.pop()
print(f"The last bike I owned was a {last_owned.title()}")
first_owned=motorcycles.pop(0)
print(f"The first bike I owned was a {first_owned.title()}")
motorcycles=['honda','yamaha','suzuki']
too_exp='yamaha'
motorcycles.remove(too_exp)
print(motorcycles)
print(f"\nA {too_exp.title()} is too expensive for me.")