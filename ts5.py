ts1,ts2,ts3=input("").split()
if ts1>ts2:
  if ts1>ts3:
    print(ts1)
  else:
    print(ts3)
elif ts2>ts3:
  print(ts2)
else:
  print(ts3)
