def remove_key(key):
    dict = {'a':1,'b':2,'c':3,'d':4}
    print("Initial dictionary")
    print(dict)

    if key in dict: 
        del dict[key]
    else:
        print("Key not found!")
        exit(0)
    print("Updated dictionary")
    print(dict)
remove_key(key='d')