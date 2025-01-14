dict1 = {
    "name":"mahendrakumar"
}
dict2 = {
    "class":"csai-f"
}
dict3 = dict1.copy()
dict1.update(dict2)

print(dict1)
print(dict2)
print(dict3)