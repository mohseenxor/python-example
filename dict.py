my_dict = { 
	"class" : "animal",
	"name"  : "giraffe",
	"age"   : 10
}

print(my_dict)
print(my_dict["name"])
print(my_dict.get("name"))
print(my_dict.values())

for x in my_dict:
	print(my_dict[x])

for x,y in my_dict.items():
	print(x,y)
