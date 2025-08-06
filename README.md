# Python List Operations

This is a basic Python script demonstrating common list operations such as indexing, inserting, extending, deleting, sorting, and finding the index of an item.

## 🔧 Features

- Accessing list items using index
- Inserting an element at a specific index
- Extending a list with another list
- Deleting an element using `del`
- Sorting a list without modifying the original
- Finding the index of a specific element

## 📄 Code Example

```python
my_list = [10, 20, 30, 40]
print(my_list[3])  # Access element

my_list.insert(10, 15)
print(my_list)  # Insert

my_list.extend([50, 60, 70])
print(my_list)  # Extend

del my_list[-1]
print(my_list)  # Delete

sorted_list = sorted(my_list)
print("Original list:", my_list)
print("Sorted list:", sorted_list)  # Sort

index_of_30 = my_list.index(30)
print(f"The index of 30 is: {index_of_30}")  # Find index
