my_list = ["Tokyo", "london", "new york"]
print(my_list)
print(my_list[2])

my_list[2] = "New Delhi"
print(my_list)

for val in my_list:
	print(val)

print(len(my_list))
my_list.append("Boston")
print(my_list)
my_list.insert(4,"Durham")
my_list.pop(1)
print(my_list)

fruits = ["apples", "oranges", "cherry"]
print(fruits)
fruits.reverse()
print(fruits)

my_list_2 = ["apples", 1,2,3.0]
my_list_3 = ["apples", [1,2,3], ['a','b','c']]
print(my_list_3[1][2])
