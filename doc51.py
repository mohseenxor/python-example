sen = input("enter the string")
string = sen.lower()
print(string)
count = 0
list1 = ["a","e","i","o","u"]
for i in string:
	if i in list1:
		count = count+1

print("no. of vowels in given sentence",count)
