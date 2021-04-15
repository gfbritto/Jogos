import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = round(random.randrange(1, 101))
total_de_tentativas = 0

print("Qual o nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Defina o nível:"))

if(nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas=10
else:
    total_de_tentativas = 5

for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chutestr = input("digite o seu número entre 1 e 100: ")
    print("Você digitou", chutestr)
    chute = int(chutestr)

    if(chute >100 or chute <=0):
        print("Você deve digitar um número entre 1 e 100!")
        continue

    acertou = chute == numero_secreto
    chute_Is_maior = chute > numero_secreto
    chute_Is_menor = chute < numero_secreto

    if (acertou):
        print("Você acertou")
        break

    else:
        if(chute_Is_maior):
            print("Você errou! O seu chute foi maior que o número secreto!")
        elif (chute_Is_menor):
            print("Você errou! O seu chute foi menor que o número secreto.")

print("Fim do jogo!")
