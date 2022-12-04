def set_(coll, path, value):
    new = coll
    index = 0
    for i in path[:-1]:
        if i in new:
            new = new[i]
            new[path[-1]] = value
            index += 1
        elif i not in new:
            for i in path:
                new.update({path[index]: value})
                new[i] = new
                index += 1

coll = {"a": {"b": {"c": 3}}}
set_(coll, ["a", "b", "c"], 4)
print(coll["a"]["b"]["c"])
set_(coll, ['x', 'y', 'z'], 5)
print(coll['x']['y']['z'])