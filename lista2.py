lista=[15, 7, 27, 39]
procurado=int(input("Digite o valor a ser procurado:"))
achou= False
x=0
while x<=len(lista):
  if lista[x]==procurado:
      achou=True
      break
  x=1
if achou:
  print("%d achado na posição %d"%(procurado, x))
else:
  print("%d nao foi encontrado"%(procurado))