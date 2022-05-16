lista=[]
while True:
  n=int(input("Digite um numero (0 sai):"))
  if n==0:
    break
  lista.append(n)
x=0
while x<len(lista):
  print(lista[x])
  x+=1    
