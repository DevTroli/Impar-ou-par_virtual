# 'replica virtual' do jogo impar ou par

import random
#importei a biblioteca random para gerar os números aleatórios


def inicio():
    impar_ou_par = input("Bora jogar impar ou par?\nVou deixar você escolher primeiro (digite 'i' para impar ou 'p' para par)\n")
    #solicitei a quem estiver lendo que escolha entre par ou ímpar para nós iniciarmos
    num_usuario = int(input("Digite um número de 1 a 100: "))
    num_pc = random.randint(1, 100)
    #puxei uma random para gerar um número aleatório de 1 a 100
    print("Eu escolhi o número: ", num_pc)
    #imprimi na tela o número escolhido pelo computador usando a primeira pessoa para a minha maquina
    soma = num_usuario + num_pc
    #soma o número escolhido do usuário com o número escolhido pela maquina
    print("Resultado: ", soma)
    if soma % 2 == 0:
    #verifiquei se a soma é par pelo resto do resultado [usando o operador 'modulo(%)']
        print("Deu par!")
        if impar_ou_par == "p":
            print("Você ganhou, parabéns!")  #Olha só que legal, a pessoa ganhou da maquina
        else:
            print("Você perdeu, que pena!")  #mostra na tela que o usuário perdeu e pode tentar novamente
    else:
        print("Deu Impar")
        if impar_ou_par == "i": #veri
            print("Você ganhou, parabéns!")
        else:
            print("Você perdeu, que pena! Tente novamente")

inicio()
    #chama a função inicio() para iniciar o jogo
