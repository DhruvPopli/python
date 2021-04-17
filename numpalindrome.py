list1 = [21,22,23,25,26,66]
a = len(list1)
reverse = 0
b = 0
while a>b:
  num = str(list1[b])
  reverse = 0
  i = list1[b]
  R = i%10
  reverse = reverse*10 + R
  i = i//10
  j = str(reverse)
  i = str(i)
  i = j + i
  b +=1
  if num == i:
    print(i," is a palindrome")
  
