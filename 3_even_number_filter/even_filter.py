def find_evens(numbers):
    even_list = []
    for i in numbers:
        if i % 2 == 0:
            even_list.append(i)
    return even_list


result = find_evens([1, 2, 3, 4, 5, 6])
print(result)

"""
 Filters and returns all even numbers from a given list.
    
Args:
     numbers (list): A list of integers to filter
    
Returns:
     list: A new list containing only the even numbers from the input
    
Example:
     find_evens([1, 2, 3, 4, 5, 6])
     [2, 4, 6]
"""

