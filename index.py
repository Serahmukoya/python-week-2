my_list = [10, 20, 30, 40]
print(my_list[3])

my_list.insert(10, 15)
print(my_list)

my_list.extend([50, 60, 70])
print(my_list)

del my_list[-1]
print(my_list)

sorted_list = sorted(my_list)
print("Original list:", my_list)
print("Sorted list:", sorted_list)

index_of_30 =my_list.index(30)
print(f"The index of 30 is: {index_of_30}")