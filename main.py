import random

def questao():
    op1 = "Programas de sistema, que gerenciam a operacao do computador em si."
    op2 = "Realizam o trabalho real desejado pelo usuario."
    op3 = "Consiste em um ou mais processadores, memoria principal, discos, impressoras, teclado, tela, interfaces de rede e outros dispositivos de entrada/saida. "
    op4 = "Pode ser entendido como um programa em execucao."

    ops = [op1,op2,op3,op4]
    rCorreta = op2
    # random.shuffle(ops)

    print("1  Mencionou-se, neste topico, que, ao software de um computador, sao atribuidas duas acoes distintas: primeiro, fazer o computador funcionar e segundo, permitir que o usuario faca o que desejar, fazendo com que identifiquemos dois tipos de software: o software de sistema e o software aplicativo. A partir disso, assinale a alternativa que estabelece uma definicao para o software de sistema:")
    print("A) "+ ops[0])
    print("B) "+ ops[1])
    print("C) "+ ops[2])
    print("D) "+ ops[3])
    r = input("Qual é a resposta correta?\n")
    if r == "A":
        r = op1
        if r == rCorreta:
            print("Você acertou!!!")
        else:
            print("Você errou")
    elif r == "B":
        r=op2
        if r == rCorreta:
            print("Você acertou!!!")
        else:
            print("Você errou")
    elif r == "C":
        r = op3
        if r == rCorreta:
            print("Você acertou!!!")
        else:
            print("Você errou")
    elif r == "D":
        r = op4
        if r == rCorreta:
            print("Você acertou!!!")
        else:
            print("Você errou")
questao()
