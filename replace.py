string = input("Enter string:\n")
str2 = string.replace("WUB", " ").split()
string = ""
for x in str2:
	string = string + " " + x
print(string.strip())
