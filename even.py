even_numbers_list = []
number = 1

while number < 300:
    even_numbers_list.append(number)
    number += 2

print(len(even_numbers_list))

for even_number in even_numbers_list:
    print("The squared value of ",even_number," is : ",even_number**2)

print("57 is in the list : ",57 in even_numbers_list)
