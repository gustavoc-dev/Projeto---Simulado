import os

gabarito = []
resp = []
pontos = 0

def questao1():
    global pontos
    A = "A configuração baseada em Cluster é representada por um conjunto de dispositivos semelhantes rodando sobre uma rede local de alta velocidade, e nessa configuração cada host pode executar um SO diferente."
    B = "As configurações em Grid costumam ser montadas como a união de vários computadores como um só dispositivo, formando uma espécie de computador coletivo, e na qual cada sistema (hardware, software e infraestrutura de rede) pode ser administrado de maneira independente."
    C = "A configuração baseada em Grid é representada por um conjunto de dispositivos semelhantes rodando sobre uma rede local de alta velocidade, e nessa configuração cada host executa o mesmo SO."
    D = "A configuração baseada em Cluster costuma ser montada como a união de vários computadores como um só dispositivo, formando uma espécie de computador coletivo, e na qual cada sistema (hardware, software e infraestrutura de rede) pode ser administrado de maneira independente."

    ops = [A,B,C,D]
    rCorreta = B
    gabarito.append("B")

    print("1  A implementação das características de um sistema distribuído passa pela relação custo/desempenho. Com isso, é importante ter em mente o que se deseja destacar nas funcionalidades desse tipo de sistema, sendo que de uma maneira geral pode-se escolher entre os sistemas em Cluster e os sistemas em Grid. Vale ressaltar que apesar disso, não há um consenso definitivo para estabelecer essa classificação. Dessa forma, avalie as sentenças e indique a alternativa CORRETA sobre essa classificação:")
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
questao1()
def questao2():
    global pontos
    A = "V – F – F – V. "
    B = "F – V – V – F. "
    C = "V – F – V – F. "
    D = "V – V – F – F. "

    ops = [A,B,C,D]
    rCorreta = B
    gabarito.append("B")

    print("2  A implementação das características de um sistema distribuído passa pela relação custo/desempenho. Com isso, é importante ter em mente o que se deseja destacar nas funcionalidades desse tipo de sistema, sendo que, de uma maneira geral, pode-se escolher entre os sistemas em Cluster e os sistemas em Grid. Vale ressaltar que, apesar disso, não há um consenso definitivo para estabelecer essa classificação. Dessa forma, avalie as sentenças sobre a popularização dos sistemas baseados em Cluster, classificando V para as sentenças verdadeira e F para as falsas:")
    print("\n(   )  Boa relação no tocante custos/desempenho, com custos reduzidos, apesar do aumento de desempenho não ser significativo. Aqui o custo passa a ser mais relevante permitindo a construção de um sistema comparável a um supercomputador.")
    print("\n(   )  A relação escalabilidade/balanceamento de carga é considerável, permitindo acréscimo, e/ou eliminação, de hosts facilitando assim o tuning de sua capacidade sem afetar o sistema como um todo.")
    print("\n(   )  Boa relação no tocante custos/desempenho, com custos reduzidos e aumento de desempenho significativo. Aqui a custo/desempenho tem a mesma relevância.")
    print("\n(   )  A relação escalabilidade/balanceamento de carga é considerável, permitindo acréscimo, e/ou eliminação, de hosts facilitando assim o tuning de sua capacidade, porém com uma certa degradação do sistema como um todo.")
    print("\nAgora, assinale a alternativa CORRETA:")
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
        if r == rCorreta:
            pontos +=2
    os.system("cls")
questao2()
def questao3():
    global pontos
    A = "II e IV. "
    B = "II e III."
    C = "Somente a I. "
    D = "Somente a II. "

    ops = [A,B,C,D]
    rCorreta = D
    gabarito.append("D")

    print("3  A implementação das características de um sistema distribuído passa pela relação custo/desempenho. Com isso é importante ter em mente o que se deseja destacar nas funcionalidades desse tipo de sistema, sendo que de uma maneira geral pode-se escolher entre os sistemas em Cluster e os sistemas em Grid. Vale ressaltar que, apesar disso, não há um consenso definitivo para estabelecer essa classificação. Dessa forma, avalie as sentenças relacionadas as características dos sistemas em Grid:")
    print("\n(   )  Esse tipo de sistema objetiva, de maneira secundária,  o alto desempenho, alcançado com o compartilhamento das fatias de recursos do conjunto computacional. Ele tem como foco principal uma arquitetura heterogênea para a convivência de vários sistemas diferentes.")
    print("\n(   )  Esse tipo de sistema objetiva, acima de tudo, o alto desempenho, alcançado com o compartilhamento das fatias de recursos, do conjunto computacional, dos vários dispositivos conectados que o compõe.")
    print("\n(   )  Do ponto de vista dos sistemas que o compõem são também homogêneos (formados por máquinas iguais) como os seus irmãos clusteres, permitindo a utilização do mesmo SO em todos os hosts.")
    print("\n(   )  Do ponto de vista dos sistemas que o compõem são heterogêneos (porém, formados por uma quantidade maior de máquinas iguais) como os seus irmãos clusteres, permitindo a utilização do mesmo SO em todos os hosts.")
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
    elif r == "D":
        resp.append(r)
        r=D
        if r == rCorreta:
            pontos +=2
    os.system("cls")
questao3()
def questao4():
    global pontos
    A = "III e IV. "
    B = "I e IV."
    C = "Somente a IV. " 
    D = "II e III. "

    ops = [A,B,C,D]
    rCorreta = B
    gabarito.append("B")

    print("4  A construção de um sistema distribuído pode ser alcançada por intermédio de, basicamente, dois tipos, os sistemas em Cluster e os sistemas em Grid. Ambos carregam um fator custo/desempenho que deve ser considerado no desenvolvimento de suas funcionalidades. Sendo que, apesar disso, não há um consenso estabelecido e definitivo em relação a essa tipificação. Tendo isso em mente, avalie as sentenças relacionadas às características dos sistemas em Grid:")
    print("\n(   ) Existe uma camada responsável pela coordenação dos recursos. Ela manipula o acesso a esses recursos, promove o escalonamento de tarefas, além de lidar com dados replicados, trata-se da camada coletiva.")
    print("\n(   )  Além das cinco camadas conceituais da arquitetura de um sistema distribuído em grid, existe uma sexta, implícita, que envolve toda as outras para criar um nível de abstração que facilite o acesso dos usuários às funcionalidades do sistema.")
    print("\n(   )  Existe uma camada responsável pela coordenação dos recursos. Ela manipula o acesso a esses recursos, promove o escalonamento de tarefas, além de lidar com dados replicados, trata-se da camada de recursos.")
    print("\n(   )  A camada mais distante das interações com o usuário é a Camada-base, ela tem a importante função de gerenciar a comunicação de camadas superiores, com os pontos de conexão de acesso aos recursos físicos de um dado sistema computacional.")
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
questao4()
def questao5():
    global pontos
    A = "Existem sistemas capazes de trabalhar com transações distribuídas, que tiveram origem no modelo cliente/servidor. Nesse modelo, geralmente existe a figura de um servidor que mantém, normalmente, um banco de dados, é responsável pelas aplicações e pela sua disponibilização às máquinas clientes, tais sistemas são denominados sistemas de integração de aplicações empresariais."
    B = "Existem sistemas capazes de trabalhar com transações distribuídas, que tiveram origem no modelo cliente/servidor. Nesse modelo, geralmente existe a figura de um servidor que mantém, normalmente, um banco de dados, é responsável pelas aplicações e pela sua disponibilização às máquinas clientes, tais sistemas são denominados sistemas de processamento de transações."
    C = "A partir de um dado momento o ambiente empresarial necessitou de uma maior integralidade entre as suas aplicações, e nesse momento tais aplicações passam a atuar de uma maneira mais independente dos bancos de dados. Aqui passa-se à segunda geração dos sistemas de processamento de transações." 
    D = "A partir de um dado momento o ambiente empresarial necessitou de uma maior integralidade entre as suas aplicações, e nesse momento tais aplicações passam a necessitar de componentes com a capacidade de comunicação diretamente entre si, o comportamento básico requisição/resposta evoluiu. Aqui passa-se à segunda geração dos sistemas de processamento de transações."

    ops = [A,B,C,D]
    rCorreta = B
    gabarito.append("B")

    print("5  Existe um conjunto de elementos que relaciona os sistemas de informação distribuídos ao contexto empresarial, tendo como causa o nascimento de uma infraestrutura que propiciou a integração entre sistemas. Nesse contexto, autores apresentam uma tipificação para os sistemas de informação distribuídos, sendo assim, assinale a alternativa CORRETA em relação a essa tipificação:")
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