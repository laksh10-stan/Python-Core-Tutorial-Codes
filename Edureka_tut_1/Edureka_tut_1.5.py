set1 = {'Python','Anaconda','Boa'}         #........not order.......no index
print(set1)
for x in set1:
    print(x)
print("Boa" in set1)
set1.add("Viper")
print(set1)
set1.update(['Cobra','Krait','Death Adder','Water Mocassin'])
print(set1)
print(len(set1))
set1.remove("Krait")            #........shows error if we try to delete item that's not present
print(set1)
set1.discard("Cobra")           #........doesn't show error if we try to delete item that's not present
print(set1)
set1.pop()                      #........we're not sure what will we popped because sets are not ordered
print(set1)
set1.clear()
print(set1)
set1.update(['Cobra','Krait','Death Adder','Water Mocassin'])
#del set1                        .................will show an error
print(set1)
set1 = set({'Cobra','Krait','Death Adder','Water Mocassin'})
print(set1)
# ..........set methods.....add(),clear(),copy(),difference(),difference_update(),discard(),intersection(),issubset(),pop()

