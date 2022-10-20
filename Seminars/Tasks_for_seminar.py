def hello(name: str):
    print('hello', name)



hello('ARTEM')

#аргумент по умолчанию
def hello(name= 'stranger'):
    print('hello', name)
    print(f'hello {name}!!!!!!!!!!!') # второй вариант вывода



hello('')


def add(m,n):
    return m+n


def mult(a=1,b=1):
    return a*b

m = mult(5,10)
print(m)

mult(add(5,10), add(10,20))