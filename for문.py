arr = ["apple", "banana", "cherry"]

print("메뉴 리스트")
for item in arr:
    print(item)

print("------------------")
print("메뉴 리스트")
sale_list = {'apple':1, 'banana':0, 'cherry':3}
for key in sale_list:
    if sale_list[key] == 0:
        print(key, "sold out")
    else:
        print(key, sale_list[key])

for i in range(10):
    print(i)

ex_arr = [num for num in range(10)]
print(ex_arr)
