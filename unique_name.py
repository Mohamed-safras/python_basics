def unique(list=None):
    unique__list = []
    if list is None:
        list = ["safras", "safras"]
    for myname in list:
        if myname not in unique__list:
            unique__list.append(myname)
    return unique__list

def a():
    print("hellow")