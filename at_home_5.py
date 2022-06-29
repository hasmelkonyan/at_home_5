def join(data, sep):
    pass


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


def my_split(source, sep, count=None):
    my_count = 0
    lst = []
    if count is not None:
        while sep in source and my_count < count:
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
    else:
        while sep in source:
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
        else:
            lst.append(source)
        return lst


print(my_split(s, " ", 5))
print(s.split(" ", 5))