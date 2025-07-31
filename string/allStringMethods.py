# Sample string
s = "  Hello Python 123  "
s2 = "python"
s3 = "123"
s4 = "Hello\nWorld"

print("the type of data type is:")
print(type(s))

# print("The length of string:")
# print(len(s))

# print(str.find("k"))
# print(str.count("i"))
# print(str.split())



print("isalnum():", s2.isalnum())        
print("isalpha():", s2.isalpha()) 
print("isdigit():", s3.isdigit())
print("islower():", s2.islower())       
print("isupper():", s2.isupper())        
print("isspace():", "   ".isspace())
print("istitle():", "Hello World".istitle())
print("isidentifier():", "name_1".isidentifier())


#Conversion
print("lower():", s2.lower())
print("upper():", s2.upper())
print("title():", s.title())


