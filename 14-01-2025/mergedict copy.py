dictionary = {
    "name":"Mahendrakumar"
}
dictionary1 = {
    "class":"csai-f"
}
for key in dictionary1:
    dictionary[key] = dictionary1[key]

print(dictionary)