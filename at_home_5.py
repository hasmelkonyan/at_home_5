def my_join(data, sep):
    lst = data[0]
    if len(data) > 1:
        for i in range(1, len(data)):
            lst += sep + data[i]
    return lst



my_lst = ["I", "like", "apple", "I", "don't", "like", "strawberry"]
print(" ".join(my_lst))
print(my_join(my_lst, " "))


def my_replace(source, old, new, count=1):
    """str replace method implementation
    """

    while count > 0:
        source_lst = [i for i in source]
        index = source.find(old)
        if old in source:
            source_lst[index: index + len(old)] = new
            count -= 1
            source = "".join(source_lst)
    return source


s = "one one was a rase horse, two two was a one too"


def my_split(source, sep, count=-1):
    my_count = 0
    lst = []
    if count is not None:
        while sep in source and (my_count < count or count == -1):
            source_lst = [i for i in source]
            index = source.find(sep)
            item_lst = []
            if index > 0:
                for j in range(index):
                    item_lst.append(source_lst[j])
            item = "".join(item_lst)
            lst.append(item)
            del source_lst[0: index + len(sep)]
            source = "".join(source_lst)
            my_count += 1
        else:
            lst.append(source)
        return lst
    


print(my_split(s, " ", 5))
print(s.split(" ", 5))
