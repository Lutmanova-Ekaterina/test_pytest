def get_val(collection, key, default='python'):
    if key in collection:
        return collection[key]

    elif key not in collection:
        return default

get_val({"hello": "world"}, "hello") #world
get_val({"hello": "world"}, "hello", "python") #world
get_val({}, "hello", "python") #python
print(get_val({"hello": "world"}, "hello"))
print(get_val({"hello": "world"}, "hello", "python"))
print(get_val({}, "hello", "python"))