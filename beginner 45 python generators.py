def my_func():
    n = 1
    print('---------------', n)
    yield n
    n += 1
    print('---------------', n)
    yield n
    n += 1
    print('---------------', n)
    yield n
    
x = my_func()

print(next(x))
print(next(x))
print(next(x))


#new example

def my_funt():
    for i in range (5):
        print('--------------', i)
        yield i

x = my_funt()
print(next(x))
print(next(x))
print(next(x))


#another example

def list_iterator(list):
    for i in list:
        yield i

a = [1, 2, 3, 4, 5]        
mylist = list_iterator(a)

print(next(mylist))
print(next(mylist))
print(next(mylist))
print(next(mylist))
print(next(mylist))