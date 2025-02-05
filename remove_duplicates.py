# Create a function that removes all duplicate elements from the list without using set()

def remove_duplicate(arr):
    unique_list = []
    for i in arr:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list


arr = [1, 2, 3, 3, 4, 5, 5]

new_arr = remove_duplicate(arr)

print("New list removing duplicate items: ", new_arr)

