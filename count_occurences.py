def count_occurences(arr, target):
    return arr.count(target)


arr = [1, 4, 5, 1, 0, 5, 1]

target = 1

results = count_occurences(arr, target)

print(f"The number {target} appers {results} times")