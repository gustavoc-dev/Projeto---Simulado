import os

gabarito = []
resp = []
pontos = 0

def questao1():
    global pontos
    A = "Execução; pronto; espera."
    B = "Execução; execução; pronto."
    C = "Espera; pronto; execução."
    D = "Pronto; execução; espera."

    ops = [A,B,C,D]
    rCorreta = A
    gabarito.append("A")

    print("1    É definido como processo um programa que se encontra em execução. Em um sistema computacional multiprogramável ou multitarefa, vários processos podem ser acionados, simultaneamente, pelo usuário. Assim, para que a concorrência ocorra de forma organizada, os processos assumem diferentes estados à medida que são executados, que são: execução, pronto e espera. A partir disso, avalie os seguintes cenários:")
    print("\n\nI-    Um documento é encaminhado para a fila de impressão.")
    print("\nII-    Um software aplicativo de e-mail é acionado pelo usuário.")
    print("\nIII-    Um sistema aguarda pela confirmação do usuário para finalização.")
    print("Os cenários apresentados nas assertivas se encontram em que estados, respectivamente?")
    print("A) "+ ops[0])
    print("B) "+ ops[1])
    print("C) "+ ops[2])
    print("D) "+ ops[3])
    r = input("\nQual é a resposta correta?\n")
    
    if r == "A":
        resp.append(r)
        r=A
        if r == rCorreta:
            pontos +=2.5
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
    A = "Espaço de armazenamento e contextos físico e de software."
    B = "Espaço de endereçamento e contextos de hardware e de sistema."
    C = "Espaço de endereçamento, contextos de hardware e de software."
    D = "Espaço de armazenamento e contextos de hardware e lógico."

    ops = [A,B,C,D]
    rCorreta = C
    gabarito.append("C")

    print("2  Pode-se considerar que um processo pode ser visualizado em três dimensões distintas, mas que se complementam para a sua composição. Cada uma delas define o que se chama de contexto, isto é, mantêm à sua volta partes de elementos que se ligam para compor um todo, o processo. Com isso em mente, avalie as sentenças e indique aquela que contém essas dimensões:")    
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
            pontos +=2.5
    elif r == "D":
        resp.append(r)
        r=D
    os.system("cls")
questao2()
def questao3():
    global pontos
    A = "Dados dos registradores do processador, prioridade e estado do processo, informações da memória principal usada pelo processo e indicação de arquivos abertos."
    B = "Dados dos registradores na memória principal, prioridade do processo, informações da memória principal usada pelo processo e indicação de arquivos abertos."
    C = "Dados dos registradores da memória, estado do processo do processo, informações da memória principal usada pelo processo e indicação de arquivos abertos."
    D = "Dados dos registradores do processador, prioridade e estado do processo, informações da memória secundária usada pelo processo e indicação de arquivos abertos."

    ops = [A,B,C,D]
    rCorreta = A
    gabarito.append("A")

    print("3  Pode-se considerar que um processo pode ser visualizado em três dimensões distintas, mas que se complementam para a sua composição. Cada uma delas define o que se chama de contexto, isto é, mantêm à sua volta partes de elementos que se ligam para compor um todo, o processo, sendo que essas dimensões registram certas informações de um processo. Sabendo disso, avalie as sentenças e indique aquelas que representam as informações mencionadas:")
    print("A) "+ ops[0])
    print("B) "+ ops[1])
    print("C) "+ ops[2])
    print("D) "+ ops[3])
    r = input("\nQual é a resposta correta?\n")
    if r == "A":
        resp.append(r)
        r=A
        if r == rCorreta:
            pontos +=2.5
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
questao3()
def questao4():
    global pontos
    A = "Tempo de processador representa o tempo no qual um processo executa no processador."
    B = "Throughput representa a quantidade de processos executados considerando um espaço de tempo especificado."
    C = "Utilização do processador significa que se espera que o processador se mantenha a maior parte do tempo desocupado."
    D = "Tempo de espera significa o total de tempo em estado de pronto para execução que um processo aguarda na fila."

    ops = [A,B,C,D]
    rCorreta = C
    gabarito.append("C")

    print("4  Um SO não executa aleatoriamente os seus processos, mas aqueles processos que se encontram em estado de “pronto” são elegíveis para execução baseados em critérios regidos pela sua política de escalonamento no seu gerenciamento de processos. Desta forma, tendo em mente estes critérios, assinale a resposta INCORRETA sobre os mesmos:")
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
            pontos +=2.5
    elif r == "D":
        resp.append(r)
        r=D
    os.system("cls")
questao4()

print("============GABARITO============")
for i in range(0,5):
    print(gabarito[i])
print("============SUA PROVA============")
for i in range(0,5):
    print(resp[i])
print("Sua pontuação foi de: {}".format(pontos))