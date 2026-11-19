lst = [10,20,30,40,50]

lst.append(5)
lst.append(6)
lst.append(7)
print(lst)

lst.remove(50)
print(lst)
lst.pop(4)
print(lst)
lst.pop()
print(lst)

lst.reverse()
print(lst)
lst.sort()
print(lst)

newlst = lst[1:]
print(newlst)

lst.append(20)
lst.append(20)
print(lst)

count20 = lst.count(20)
print(count20)

index20 = lst.index(20)
print(index20)

cpylst = lst
cpylst[0] = 999
print(cpylst)


cpylst = lst[:]
cpylst[-1] = 999
print(cpylst)
print(lst)

empty = []
print(empty)
for i in lst:
    if i >= 20 and i <= 50:
        empty.append(i)
print(empty)

empty =[0] * 10
print(empty)
empty[0] = 99
print(empty)

squares = []
for i in range(1, 10):
    squares.append(i*i)
print(squares)

squares = [x*x for x in range(1,10)]
print(squares)

values = [34,27,95,18,36,21,64,50,77]
even_values = [x for x in values if x % 2 == 0]
print(even_values)

newlst = [val for val in lst if val >=20 and val <= 50]
print(newlst)

aset = set()
aset = {1,2,3,4,3,3,3}
print(aset)
aset.add(40)
print(aset)

fav_foods = {"Annika" : "ice cream", "Jane" : "pasta", "Jackson" : "Steak", "Emma" : "Chicken", "Ava" : "pasta"}
food = fav_foods["Annika"]
print(food)

if "jane" in fav_foods:
    print(fav_foods["John"])
else:
    fav_foods["John"] = "chocolate"
print(fav_foods)

for name,fav_food in fav_foods.items():
    print(name, fav_food)
