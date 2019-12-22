# 
# Example file for variables
#

# # Declare a variable and initialize it
f = 0
# print(f)

# # # re-declaring the variable works
# f = "abcd"
# print(f)

# # ERROR: variables of different types cannot be combined
# print("this is a string" + str(123)) #casting a different variable

# Global vs. local variables in functions

def someFunction():
	global f
	f = "def"
	print(f)

someFunction()


