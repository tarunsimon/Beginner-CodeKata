var1=int(input())
var2=[]
var3=[]
for i in range(var1):
  var3=input()
  var2.append(var3)
d=[]
for i in zip(*var2):
  if(i.count(i[0])==len(i)):
    d.append(i[0])
  else:
    break
print(''.join(d))
