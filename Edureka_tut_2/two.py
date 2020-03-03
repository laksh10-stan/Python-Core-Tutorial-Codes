# file two.py
import one                # when we import a file the code inside it gets executed first
print('top level in two.py')
one.func()
if __name__== "__main__":
    print('two.py is being run directly')
else:
    print('two.py is being run by another module')
    