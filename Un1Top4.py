import os
gabarito = []
resp = []
pontos = 0

def questao1():
    global pontos
    A = "Monotarefa; Multitarefa e Multiprocessado."
    B = "Monotarefa; Monousuário e Multitarefa."
    C = "Multitarefa; Multiprocessado e Monotarefa. "
    D = "Multiusuário; Multiprocessado e Multitarefa. "

    ops = [A,B,C,D]
    rCorreta = C
    gabarito.append("C")

    print("1  Neste tópico, você compreendeu que “os tipos de sistemas operacionais e sua evolução estão relacionados diretamente com a evolução do hardware e das aplicações por ele suportadas” (MACHADO; MAIA, 2017, p. 15). As assertivas a seguir trazem definições de diferentes tipos de SO vistos neste tópico:")
    print("\n\nI-   Passou a ser possível compartilhar os recursos de processamento, memória e periféricos entre vários usuários e aplicações.")
    print("\nII-  Tem como principal característica o fato de possuírem dois ou mais processadores comunicando-se e trabalhando perfeitamente em conjunto.")
    print("\nIII- É um tipo de sistema no qual o processador, a memória e os periféricos ficam dedicados à execução de um programa de cada vez.")
    print("\n\nAs definições apresentadas referem-se a quais tipos de SO respectivamente?")
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
questao1()
def questao2():
    global pontos
    A = "Com o aumento do número de processadores, aumenta-se a velocidade ou throughput, pois espera-se realizar mais trabalho em menos tempo. Isso porque é possível que vários programas sejam executados ao mesmo tempo, ou que um mesmo programa seja dividido em partes e executado ao mesmo tempo por vários processadores."
    B = "Em sistemas multiprocessados é possível aumentar o poder computacional apenas acrescentando novos processadores, o que os torna altamente escaláveis."
    C = "Basicamente existem dois tipos de sistemas multiprocessados: os sistemas fortemente acoplados e os sistemas fracamente acoplados."
    D = "Um sistema fracamente acoplado é caracterizado por existirem vários processadores com seus periféricos sendo gerenciados por um único SO. Esses vários processadores compartilham uma única memória."

    ops = [A,B,C,D]
    rCorreta = D
    gabarito.append("D")

    print("2  Um dos tipos de SO que você estudou são os sistemas com múltiplos processadores ou multiprocessados. A principal característica deste tipo de SO é a existência de dois ou mais processadores trabalhando conjuntamente. Por esta razão, estes sistemas são também chamados de sistemas paralelos. Os sistemas multiprocessados apresentam uma série de características que os tornam mais atraentes em relação aos sistemas com um único processador. Sobre os sistemas multiprocessados assinale a alternativa INCORRETA:")    
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
questao2()
def questao3():
    global pontos
    A = "No tocante à natureza da forma de controle exigido pelos serviços dos usuários, uma possível classificação para os SO reside em ele ser ou não multiusuário."
    B = "No tocante ao número de usuários acessando um serviço, ou um recurso, uma possível classificação para os SO reside em ele ser ou não multitarefa."
    C = "No tocante à natureza da forma de controle exigido pelos serviços dos usuários, uma possível classificação para os SO reside em ele ser ou não multitarefa."
    D = "No tocante à natureza da forma de controle exigido pelos serviços dos usuários, uma possível classificação para os SO reside em ele ser ou não monousuário."

    ops = [A,B,C,D]
    rCorreta = C
    gabarito.append("C")

    print("3  A construção de um SO envolve vários aspectos relevantes, por exemplo, a sua utilização pelos usuários, o tipo de serviço que deve ser provido por ele e a complexidade destes serviços, ou o tipo de ambiente no qual eles irão rodar, como, por exemplo, os atuais ambientes para dispositivos móveis. Logo, esses aspectos levam a um agrupamento dos SO baseado em uma classificação. Considerando essa classificação assinale a alternativa CORRETA:")
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
questao3()
def questao4():
    global pontos
    A = "O tipo de sistema no qual o conjunto processador, memória e dispositivos E/S está disponível aos vários programas de usuários um por vez, como em uma espécie de fila, caracteriza um sistema multitarefa. Neste ambiente o SO enfileira os acessos a estes recursos e, como existem vários programas enfileirados, isto caracteriza um ambiente multitarefa."
    B = "O tipo de sistema no qual o conjunto processador, memória e dispositivos E/S está disponível aos vários programas de usuários um por vez, como em uma espécie de fila, caracteriza um sistema multitarefa. Neste ambiente o SO enfileira os acessos a estes recursos e, como existem vários programas enfileirados, isto caracteriza um ambiente de multiprogramação."
    C = "O tipo de sistema no qual o conjunto processador, memória e dispositivos E/S está disponível aos vários programas de usuários um por vez, como em uma espécie de fila, caracteriza um sistema multitarefa. Neste ambiente o SO enfileira os acessos a estes recursos e, como existem vários programas enfileirados, isto caracteriza um ambiente monotarefa."
    D = "O tipo de sistema no qual o conjunto processador, memória e dispositivos E/S está disponível aos vários programas de usuários um por vez, como em uma espécie de fila, caracteriza um sistema multitarefa. Neste ambiente o SO enfileira os acessos a estes recursos e, como existem vários programas enfileirados, isto caracteriza um ambiente de multiprocessamento."

    ops = [A,B,C,D]
    rCorreta = C
    gabarito.append("C")

    print("4 Um dos grandes desafios para o projeto de um SO reside em garantir que os seus serviços tenham acesso seguro e confiável aos recursos gerenciados por esse SO, sendo que estes recursos estão relacionados ao acesso e compartilhamento do processador, memória e dispositivos de E/S, entre outros. Com isso, a forma como esses recursos são compartilhados e a forma como são acessados caracteriza algumas tipificações para os SO. Considerando essas tipificações assinale a alternativa CORRETA:")
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
questao4()
def questao5():
    global pontos
    A = "Ambientes multiprocessados tightly coupled systems constituem uma tipificação de sistemas na qual sua natureza de memórias individuais, para cada processador, configura sistemas independentes, porém coesos, comunicando-se para a execução dos seus serviços."
    B = "Ambientes multiprocessados loosely coupled systems constituem uma tipificação de sistemas na qual sua natureza de memórias individuais, para cada processador, configura sistemas dependentes, e sem coesão, mas que se comunicam para a execução dos seus serviços."
    C = "Ambientes multiprocessados tightly coupled systems constituem uma tipificação de sistemas na qual sua natureza de memória individual compartilhada, configura sistemas independentes, porém coesos, comunicando-se para a execução dos seus serviços."
    D = "Ambientes multiprocessados loosely coupled systems constituem uma tipificação de sistemas na qual sua natureza de memórias individuais, para cada processador, configura sistemas independentes, porém coesos, comunicando-se para a execução dos seus serviços."

    ops = [A,B,C,D]
    rCorreta = D
    gabarito.append("D")

    print("5  Um dos grandes desafios para o projeto de um SO reside em garantir que os seus serviços tenham acesso seguro e confiável aos recursos gerenciados por esse SO, sendo que esses recursos estão relacionados ao acesso e compartilhamento do processador, memória e dispositivos de E/S, entre outros. E esse acesso e compartilhamento ganham uma maior importância e complexidade quando o SO tem que lidar com ambientes de multiprocessamento. Considerando essa característica assinale a alternativa CORRETA:")
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
questao5()
print("============GABARITO============")
for i in range(0,4):
    print(gabarito[i])
print("============SUA PROVA============")
for i in range(0,4):
    print(resp[i])
print("Sua pontuação foi de: {}".format(pontos))