string = int(input("enter the string:"))
string = str(string)
rev_string = string[::-1]
print("reversed string:", rev_string)
if string == rev_string:
	print("string is palindrome")
else:
	print("string is not palindrom")
