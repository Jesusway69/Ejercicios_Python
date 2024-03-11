import os
os.system('clear')

n1 = int(input('escriba número1: '))
n2 = int(input('escriba número2: '))


if n1>n2 and n1%n2==0:
  print(n1 ,' es múltiplo de ', n2)
elif n1<n2 and n2%n1==0:
    print(n2 ,' es múltiplo de ', n1)
elif n1==n2:
    print(n1, 'y' , n2 , 'son el mismo número y por lo tanto son múltiplos')
else:
    print(n1 ,' y ', n2, 'no son múltiplos')
