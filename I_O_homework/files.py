file = open("./student_names.txt")

# Read all of the content of the file in one variable.
names = file.read()

# Write a list of random names to your file.
random_names = ["April Reiter","Emory Miller","David Ballin","Alice Trotter","Virginia Rios","Thomas Wheeler"]

for name in random_names:
    names += "\n"+name

file.close()
file = open("./student_names.txt","w")

file.write(names)
file.close()

# Read the first n lines of the file.
# Read the last n lines of the file.
file = open("./student_names.txt")

n = int(input("Enter the number of lines to read : "))

all_names = file.readlines()

print("The first ",n," names:\n",''.join(all_names[:n]))
print("The last ", n, " names:\n", ''.join(all_names[(len(all_names)-n):]))

# Check if the name x is in the file.

all_names = ''.join(all_names)

name = input("Enter the name to check if it is in the file : ")

if name+" " in all_names:
    print(name," is in the file.")
else:
    print(name, " is not in the file.")

file.close()
# Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.

for letter_index in range(0,26):
    file = open(chr(ord('A') + letter_index)+'.txt','w')
    file.close()

