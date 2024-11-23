import os
gabarito = []
resp = []
pontos = 0

def questao1():
    global pontos
    A = "Um processo ou uma thread deve executar, sem afetar de modo intencional, malicioso ou mesmo, acidentalmente, o comportamento do outro."
    B = "Um processo ou uma thread pode executar, sem afetar de modo intencional, malicioso ou mesmo acidentalmente, o comportamento do outro."
    C = "Um processo é impedido pelo SO de compartilhar dados com outros processos e com suas threads."
    D = "Uma thread criada por um processo A é impedida pelo SO de compartilhar dados com outras threads criadas por outros processos."

    ops = [A,B,C,D]
    rCorreta = A
    gabarito.append("A")

    print("1  Os processos são criados e destruídos. O momento e a forma pela qual eles são criados e destruídos depende do sistema operacional em consideração. Alguns sistemas trabalham com um número fixo de processos. Por exemplo, um processo para cada terminal do computador. Nesse caso, todos os processos são criados na inicialização do sistema. Eles somente são destruídos quando o próprio sistema é desligado.")
    print("\nOs autores lembram ainda que cada um dos processos em execução deve executar sem interferência entre eles. Dessa forma, assinale a alternativa CORRETA sobre processos e threads.")
    print("A) "+ ops[0])
    print("B) "+ ops[1])
    print("C) "+ ops[2])
    print("D) "+ ops[3])
    r = input("\nQual é a resposta correta?\n")
    
    if r == "A":
        resp.append(r)
        r=A
        if r == rCorreta:
            pontos +=3.4
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
    A = "As sentenças II e III estão corretas."
    B = "As sentenças III e IV estão corretas."
    C = "As sentenças II e IV estão corretas."
    D = "As sentenças I e II estão corretas. "

    ops = [A,B,C,D]
    rCorreta = B
    gabarito.append("B")

    print("2  Para a capacidade de utilizar um recurso (UCP, memória principal, armazenamento secundário por exemplo) como se houvesse mais do que um, dá-se o nome de virtualização (TANENBAUM; STEEN, 2007). Com isso, o site Vmware (O QUE, 2018) aponta que a virtualização pode permitir a implantação de cargas de trabalho mais rápidas, aumento do desempenho e a disponibilidade de recursos maiores com a automatização das atividades organizacionais, resultando em uma TI simples, barata de se operar. Com isso em mente, analise as sentenças e assinale a resposta CORRETA sobre os benefícios da virtualização:")
    print("\nI-   Combate às despesas operacionais, porém não às de capital.")
    print("\nII-  Suaviza, porém, sem eliminar, o tempo de inatividade dos recursos do sistema.")
    print("\nIII- Agiliza a capacidade de resposta da TI.")
    print("\nIV- Permite a provisão de aplicativos e recursos com mais rapidez.")
    print("\nAgora, assinale a alternativa que apresenta a sequência CORRETA:")
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
            pontos +=3.3
    elif r == "C":
        resp.append(r)
        r=C
    elif r == "D":
        resp.append(r)
        r=D
    os.system("cls")
questao2()
def questao3():
    global pontos
    A = "V – V – V – V. "
    B = "V – V – F – F. "
    C = "F – V – V – F. "
    D = "V – F – F – V."

    ops = [A,B,C,D]
    rCorreta = C
    gabarito.append("C")

    print("3  Em um ambiente de execução de processos computacionais é impossível desassociá-los de suas threads não só sob o aspecto dos SO, mas também da programação para computadores. Elas representam fluxos de execução e sempre estão associadas a um único processo, porém cada processo pode ser composto por várias threads. Dessa forma, avalie as afirmações sobre as processos e threads.")
    print("\n(   ) Processos permitem construir programas (porções) que parecem ser executados simultaneamente em dispositivos com um único processador.")
    print("\n(   ) Threads permitem construir programas (porções) que podem ser executados simultaneamente em dispositivos com mais de um processador.")
    print("\(   ) Threads permitem construir programas (porções) que parecem ser executados simultaneamente em dispositivos com um único processador.n")
    print("\n(   ) Processos permitem construir programas (porções) que podem ser executados simultaneamente em dispositivos com mais de um processador.")
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
    elif r == "C":
        resp.append(r)
        r=C
        if r == rCorreta:
            pontos +=3.3
    elif r == "D":
        resp.append(r)
        r=D
    os.system("cls")
questao3()


print("============GABARITO============")
for i in range(0,4):
    print(gabarito[i])
print("============SUA PROVA============")
for i in range(0,4):
    print(resp[i])
print("Sua pontuação foi de: {}".format(pontos))