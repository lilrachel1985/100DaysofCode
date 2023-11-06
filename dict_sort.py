numbers=[{'name': 'Homer', 'age': 39}, {'name': 'Bart', 'age': 15}, {'name': 'Rachel', 'age':38}]
def dict_sort(list):
    new_list=sorted(numbers,key=lambda X:X['age'])
    print(new_list)
dict_sort(list=numbers)