import os

gabarito = []
resp = []
pontos = 0

def questao1():
    global pontos
    A = "Programas de sistema, que gerenciam a operacao do computador em si."
    B = "Realizam o trabalho real desejado pelo usuario."
    C = "Consiste em um ou mais processadores, memoria principal, discos, impressoras, teclado, tela, interfaces de rede e outros dispositivos de entrada/saida. "
    D = "Pode ser entendido como um programa em execucao."

    ops = [A,B,C,D]
    rCorreta = A
    gabarito.append("A")

    print("1   Mencionou-se, neste tópico, que, ao software de um computador, são atribuídas duas ações distintas: primeiro, fazer o computador funcionar e segundo, permitir que o usuário faça o que desejar, fazendo com que identifiquemos dois tipos de software: o software de sistema e o software aplicativo. A partir disso, assinale a alternativa que estabelece uma definição para o software de sistema:")
    print("A) "+ ops[0])
    print("B) "+ ops[1])
    print("C) "+ ops[2])
    print("D) "+ ops[3])
    r = input("\nQual é a resposta correta?\n")
    
    if r == "A":
        resp.append(r)
        r=A
        if r == rCorreta:
            pontos +=2
    elif r == "B":
        resp.append(r)
        r=B
    elif r == "C":
        resp.append(r)
        r=C
    elif r == "D":
        resp.append(r)
        r=D
    os.system("cls")
questao1()
def questao2():
    global pontos
    A = "I e II. "
    B = "I e IV."
    C = "Soemente a III"
    D = "Somente a I"

    ops = [A,B,C,D]
    rCorreta = C
    gabarito.append("C")

    print("2   Você viu que o principal objetivo do SO é “[...] funcionar como uma interface entre o usuário e o computador, tornando sua utilização mais simples, rápida e segura” (MACHADO; MAIA, 2011; 2017, p. 1). Esse objetivo é cumprido porque o SO executa uma série de funções como, por exemplo, monitorar o desempenho do computador, corrigir eventuais erros na execução de softwares aplicativos, fornecer e manter a interface do usuário e inicializar o computador. Há ainda outras funções, consideradas mais complexas, e que merecem nossa atenção. Nas assertivas a seguir são apresentadas as definições de algumas destas funções:")
    print("\nI-   Gerenciamento de processos é caracterizado pela existência de dois ou mais processadores interligados executando programas distintos ou executando, simultaneamente, um mesmo programa. ")
    print("\nII-  Multiprocessamento está entre as funções essenciais do SO, pois está relacionada à capacidade de um processo de armazenar e recuperar grandes volumes de informações.")
    print("\nIII- Tolerância a falhas é a capacidade de manter o sistema em operação mesmo em casos de falha em algum componente.")
    print("\nIV- Gerenciamento de arquivos é a função exercida pelo SO para controlar os programas (softwares aplicativos, por exemplo) que estão sendo executados em algum momento pelo processador.")
    print("\nA partir das definições fornecidas, estão CORRETAS as assertivas:")
    
    print("A) "+ ops[0])
    print("B) "+ ops[1])
    print("C) "+ ops[2])
    print("D) "+ ops[3])
    r = input("\nQual é a resposta correta?\n")
    if r == "A":
        resp.append(r)
        r=A
    elif r == "B":
        resp.append(r)
        r=B
    elif r == "C":
        resp.append(r)
        r=C
        if r == rCorreta:
            pontos +=2
    elif r == "D":
        resp.append(r)
        r=D
    os.system("cls")
questao2()
def questao3():
    global pontos
    A = "Monitorar o desempenho."
    B = "Formatar dispositivos como pen drives."
    C = "Inicializar o computador."
    D = "Gerenciar a alocação de memória para esses programas."

    ops = [A,B,C,D]
    rCorreta = D
    gabarito.append("D")

    print("3   Um SO pode permitir que um computador execute vários programas na memória, ao mesmo tempo ou de maneira concorrente, com mostra a figura. Logo, o SO deve assegurar que todos executem sem interferência entre si. Isto é, sem que cada um dos programas afete de algum modo a corretude do comportamento individual um do outro (TANENBAUM; STEEN, 2007). A afirmação em destaque refere-se a qual função do SO:")
    print("A) "+ ops[0])
    print("B) "+ ops[1])
    print("C) "+ ops[2])
    print("D) "+ ops[3])
    r = input("\nQual é a resposta correta?\n")
    if r == "A":
        resp.append(r)
        r=A
    elif r == "B":
        resp.append(r)
        r=B
    elif r == "C":
        resp.append(r)
        r=C
    elif r == "D":
        resp.append(r)
        r=D
        if r == rCorreta:
            pontos +=2
    os.system("cls")
questao3()
def questao4():
    global pontos
    A = "Permitir que as aplicações recuperem/armazenem dados de/para a memória."
    B = "Gerenciar o tráfego de dados entre os periféricos de um computador."
    C = "Fornecer informações relevantes aos usuários quando da ocorrência de um erro no sistema."
    D = "Realizar buscas/armazenamentos de dados em base de dados de softwares aplicativos. "

    ops = [A,B,C,D]
    rCorreta = D
    gabarito.append("D")

    print("4  “[...] funcionar como uma interface entre o usuário e o computador, tornando sua utilização mais simples, rápida e segura” (MACHADO; MAIA, 2011; 2017, p. 1), trata-se do principal objetivo de um SO. Como parte desse objetivo, tem-se a detecção de vírus, localização, criação e exclusão de arquivos, criação e manutenção de pastas, existindo, ainda, outras funções. Considerando as assertivas a seguir, indique aquela que não representa a função de um SO:")
    print("A) "+ ops[0])
    print("B) "+ ops[1])
    print("C) "+ ops[2])
    print("D) "+ ops[3])
    r = input("\nQual é a resposta correta?\n")
    if r == "A":
        resp.append(r)
        r=A
    elif r == "B":
        resp.append(r)
        r=B
    elif r == "C":
        resp.append(r)
        r=C
    elif r == "D":
        resp.append(r)
        r=D
        if r == rCorreta:
            pontos +=2
    os.system("cls")
questao4()
def questao5():
    global pontos
    A = "I e III. "
    B = "II e IV."
    C = "Soemente a III"
    D = "Somente a I"

    ops = [A,B,C,D]
    rCorreta = B
    gabarito.append("B")

    print("5  Um SO pode permitir que um computador execute vários programas na memória, ao mesmo tempo ou de maneira concorrente, com mostra a figura. Logo, o SO deve assegurar que todos executem sem interferência entre si. Isto é, sem que cada um dos programas afete de algum modo a corretude do comportamento individual um do outro (TANENBAUM; STEEN, 2007). A afirmação em destaque refere-se as funções do SO:")
    print("\nI-  Criar e manter diretórios.")
    print("\nII-  Preservar a segurança e limitar o acesso.")
    print("\nIII-  Detectar vírus.")
    print("\nIV- Ler os programas para a memória.")
    print("\nA partir das definições fornecidas, estão CORRETAS as assertivas:")
    print("A) "+ ops[0])
    print("B) "+ ops[1])
    print("C) "+ ops[2])
    print("D) "+ ops[3])
    r = input("\nQual é a resposta correta?\n")
    if r == "A":
        resp.append(r)
        r=A
    elif r == "B":
        resp.append(r)
        r=B
        if r == rCorreta:
            pontos +=2
    elif r == "C":
        resp.append(r)
        r=C
    elif r == "D":
        resp.append(r)
        r=D
    os.system("cls")
questao5()

print("============GABARITO============")
for i in range(0,5):
    print(gabarito[i])
print("============SUA PROVA============")
for i in range(0,5):
    print(resp[i])
print("Sua pontuação foi de: {}".format(pontos))