num=0
while True:
  num=int(input("insira um numero entre 10 e 20:"))
  if num<10:
    print("Muito baixo, tente novamente")
  elif num>20:
    print("Muito alto, tente novamente")
  else:
    print("Obrigado")
    break