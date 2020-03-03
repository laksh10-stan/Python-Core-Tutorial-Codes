#file operations
'''
open /closing a file
read/write in file
rename file
'''
import os

'''
open() function
file_Object=open(file_name[access_mode])
access_mode--->read,write,append
'''
'''
opening modes
r ---> read only
rb --> read only in binary format
r+ --> read and write
rb+ -> read and write in binary format
w ---> write only, overwrites if the file exist, creates new file if doesnt exist
wb --> write only in binary format, overwrites if the file exist, creates new file if doesnt exist
a ---> appending, adding something at the end
ab --> appending in binary format, adding something at the end in binary format
a+ --> appending and reading
ab+ -> appending and reading in binary format
w+ --> writing and reading
wb+ ->  writing and reading in binary format
'''
'''
1.  fileObject.Write(string)      ........write method
    it does not add \n at the end
    python files can have binary data and not just text
2.  fileObject.read([count])         #count specifies the no. of characters it can read, it is optional, if u dont use it it'll read n no. of characters
    reads a string from an open file
    python strings can have binary data apart from just text
3.  os.rename(current_file_name,new_file_name)            #os---> Operating System
4.  os.remove(file_name)
'''
newfile=open('Laksh.txt','w+')
for i in range(1,10):
    newfile.write("\n I'm back")
newfile.close()
newfile=open('Laksh.txt','r')
for i in range(1,10):
    print(newfile.read())
newfile.close()
newfile=open('Laksh.txt','r')
for i in range(1,10):
    print(newfile.read(5))  #reads 5 char at a time
newfile.close()
#os.rename('Laksh.txt','Hukka.txt')
os.remove('Laksh.txt')
#newfile=23           ...........python will automatically close the file if we reassign
print(newfile.mode)          #..........prints the mode r ,w+ etc..
print(newfile.name)
#      .......file.softspace().....returns a boolean, weather a space character needs to be printed before another value when using print statement
#print (newfile.softspace())
#........file.seek().........changes the current file position
#.............file.tell()........method tells you the current position within the file
newfile=open('Hukka.txt','r')
newfile.seek(10)
print(newfile.read())  #starts reading after 10 characters
print(newfile.tell())
