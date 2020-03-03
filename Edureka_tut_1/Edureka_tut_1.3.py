last = ["Gammora","Nebula","Thanos"]
print(last)
print(last[1])
last[1]="Star Lord"
print(last[1])
for x in last:
 print(x)
if "Star Lord" in last:
   print("Yes Star  Lord Exist")
else:
    print("Star Lord has been wiped out")
print(len(last))
last.append("Cyborg")
print(last)
last.insert(1,"Yondu")
print(last)
last.remove("Star Lord")
print(last)
last.pop()
print(last)
last.pop(1)
print(last)
last.append("Cyborg")
print(last)
del last[0]
print(last)
#del list
#print(list)
last.append("Cyborg")
print(last)
last.clear()
print(last)
newlist = list(("Bear Grylls","Brady Barr","Austin Stevens"))   #Constructor not a normal list
print(newlist)
#other list funcs append(),clear(),copy(),count(),extend(),index(),insert(),pop(),remove(),reverse(),sort(),  .... etc
