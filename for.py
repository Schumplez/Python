import random
pontuaçao=0
for x in range(1,6):
  num_1=random.randint(1,100)
  num_2=random.randint(1,100)
  correto= num_1 + num_2
  print(num_1, "+", num_2, "= ")
  resposta = int(input("Digite sua resposta:"))
  if resposta==correto:
    pontuaçao+=1
print("Sua pontuação foi de:", pontuaçao, "de 5 tentativas")