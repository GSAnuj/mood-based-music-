import array

# Step 1: Initialize an array
arr = array.array('i', [10, 20, 30, 40, 50])

# Step 2: Insert an element at a specific index
arr.insert(2, 25)  # Inserts 25 at index 2

# Step 3: Delete an element from the array
arr.remove(40)  # Removes the first occurrence of 40

# Step 4: Search for an element
search_element = 30
index_found = arr.index(search_element) if search_element in arr else -1

# Step 5: Sort the array (Convert to list first)
sorted_arr = sorted(arr)

# Step 6: Reverse the array
reversed_arr = arr[::-1]

# Step 7: Find maximum and minimum elements
max_element = max(arr)
min_element = min(arr)

# Step 8: Compute sum of all elements
sum_of_elements = sum(arr)

# Display results
print("Updated Array:", arr)
print(f"Index of {search_element}: {index_found}")
print("Sorted Array:", sorted_arr)
print("Reversed Array:", reversed_arr)
print(f"Maximum Element: {max_element}")
print(f"Minimum Element: {min_element}")
print(f"Sum of Elements: {sum_of_elements}")

# Additional Details
print("Name - ANUJ GUPTA")
print("24BAI10152")
