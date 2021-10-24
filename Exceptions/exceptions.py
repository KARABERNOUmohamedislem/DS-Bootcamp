a = 12
s = "hello"
try:
	print("inside try")
	s = int(s)
	a = a/0  # will raise ZeroDivisionError
	s[2] = 'd' # will raise TypeError
	print(s[10]) # will raise IndexError
	print(a + s) # will raise TypeError
	print("Printed using original data types")
except TypeError: # will handle only TypeError
	print("inside except")
	print(str(a) + s)
	print("Printed using type-casted data types")
except IndexError:
	print("Index out of range")
	print(s[len(s)-1])
except ZeroDivisionError:
	print('You devided by zero!!')
except ValueError:
	print('Can\'t cast strings to integer')
else:
    print('The program is executed succesfully.')
finally:
	print('This will be printed every time.')
