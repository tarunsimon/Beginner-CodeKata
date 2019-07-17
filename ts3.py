char = input()
if(char=='A' or char=='a' or char=='E' or char =='e' or char=='I'
 or char=='i' or char=='O' or char=='o' or char=='U' or char=='u'):
  print("Vowel")
elif(char>='a'and char<='z')or(char>='A'and char<='Z'):
  print("Consonant")
else:
  print("invalid")
