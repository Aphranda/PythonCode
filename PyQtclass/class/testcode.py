
nums =[3, 2, 4]
target = 6
item = {}
for i, n  in enumerate(nums):
    if target - n in item:
        print(item[target-n], i)
    item[n] = i
