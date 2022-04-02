import copy

def eggs(someParameter):
    someParameter.append('Hello')

spam = ['a', 'b', 'c', 'd']

cheese = copy.deepcopy(spam)


eggs(cheese)

print(spam)
print(cheese)
