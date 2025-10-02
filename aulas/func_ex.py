def add_item(L):
    L.append(4)       # mutação IN-PLACE

nums = [1, 2, 3]
add_item(nums)
print(nums)  # [1, 2, 3, 4]