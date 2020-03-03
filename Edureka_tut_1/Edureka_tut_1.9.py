#Functions
def fun():
    print('This is first fun')
fun()
def my_fun(fname):
    print(fname + ' Targareyan')

my_fun('Aegon')
my_fun('Rhaegar')
my_fun('Viserys')
print('\n')
def my_fun1(name='Daenerys'):
    print(name + ' Targareyan')

my_fun1('Aegon')
my_fun1()
my_fun1('Rhaegar')
my_fun1('Viserys')
print('\n')
def my_fun2(x=0):
    return 5*x

print(my_fun2(16))
print(my_fun2())
print(my_fun2(-1))
