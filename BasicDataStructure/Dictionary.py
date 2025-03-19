# 查看类的方法
dir(dict)
methods = dir(dict)
print('methods = ',methods)

# Create:
# 方法1
dic1 = { 'Author' : 'Python当打之年' , 'age' : 99 , 'sex' : '男' }

# 方法2
lst = [('Author', 'Python当打之年'), ('age', 99), ('sex', '男')]
dic2 = dict(lst)

# 方法3
dic3 = dict( Author = 'Python当打之年', age = 99, sex = '男')

# 方法4
list1 = ['Author', 'age', 'sex']
list2 = ['Python当打之年', 99, '男']
dic4 = dict(zip(list1, list2))

# print output
print(dic1, dic2, dic3, dic4)
# print items
print(dic1.items())
print(dic1['Author'])
print(dic1.get('Author'))
# print keys
print(dic1.keys())
# print value: key-item
print(dic1.values())
# Check if Key Exists
if "model" in dic1:
    print("Yes, 'model' is one of the keys in the dic1 dictionary")
else:
    print("No, 'model' is not a key in dictionary")

#Modify dictionary

# update key-item
# 1
dic1["age"] = 100
print(dic1)
# 2
dic1.update({"age": 101})
print(dic1)
# add key-item
dic1["color"] = "red"
print(dic1)
# remove key-item
# 1
del dic1["color"]
print(dic1)
# 2
dic1.pop("sex")
print(dic1)
# 3 removes the last inserted item
dic1["num"]=1001
print(dic1)
# removes the last inserted item
dic1.popitem()
print(dic1)

# delete the dictionary completely
del dic1
# print(dic1) // through error

# empty the dictionary
dic1={'name':'sharninjak', 'age':99, 'sex':'男'}
print(dic1)
dic1.clear()
print(dic1)


# Loop
dic1={'name':'sharninjak', 'age':99, 'sex':'男'}
# print key
# 1
for x in dic1:
    print(x)
print()
# 2
for x in dic1.keys():
    print(x)
print()
# print value
# 1
for x in dic1.values():
    print(x)
print()
# 2
for x in dic1:
    print(dic1[x])
print()
# print key-value
for x, y in dic1.items():
    print(x, y)
print()


# soft copy
print(dic1)
# dict2 will only be a reference to dict1 changes made in dict1 will automatically also be made in dict2
dic2 = dic1
print(dic2)
dic1.update({"age": 100})
print(dic2)
print()

# hard copy
copydic1 = dic1.copy()
copy1dic1 = dict(dic1)
print(copydic1)
print(copy1dic1)
dic1.update({"age": 1000})
print(copydic1)
print(copy1dic1)

# nested dictionary
# 1
myfamily = {
    "child1" : {
        "name" : "Emil",
        "year" : 2004
    },
    "child2" : {
        "name" : "Tobias",
        "year" : 2007
    },
    "child3" : {
        "name" : "Linus",
        "year" : 2011
    }
}
# 2
child1 = {
    "name" : "Emil",
    "year" : 2004
}
child2 = {
    "name" : "Tobias",
    "year" : 2007
}
child3 = {
    "name" : "Linus",
    "year" : 2011
}

myfamily = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
}
print(myfamily["child2"]["name"])
# Loop Through Nested Dictionaries
for x, obj in myfamily.items():
    print(x)
    for y in obj:
        print(y + ':', obj[y])
# list
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

# tuple
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)  # ['mango', 'papaya', 'pineapple']
print(red)

