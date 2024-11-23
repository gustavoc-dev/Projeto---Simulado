import os
gabarito = []
resp = []
pontos = 0

def questao1():
    global pontos
    A = "Do hardware que também evoluiu juntamente com os SO."
    B = "Do software, já que apesar da evolução do hardware as manipulações de programas são, ainda, pouco amigáveis."
    C = "Dos softwares aplicativos, uma vez que a sua evolução permitiu a construção de interfaces de interação mais amigáveis para os usuários. "
    D = "Principalmente dos softwares de sistemas, especialmente o SO, em combinação com a evolução do hardware e dos softwares aplicativos. "

    ops = [A,B,C,D]
    rCorreta = D
    gabarito.append("D")

    print("1  Uma das importantes funções dos SO é: fornecer e manter a interface do usuário, e ela deve ser a mais amigável e intuitiva possível e “simples, confiável e eficiente”. Logo, com a evolução dos SO essa função foi cada vez mais deixada ao controle:")
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
            pontos +=2.5
    os.system("cls")
questao1()
def questao2():
    global pontos
    A = "I – III – II."
    B = "II – III – I."
    C = "III – I – II."
    D = "I – II – III."

    ops = [A,B,C,D]
    rCorreta = C
    gabarito.append("C")

    print("2  As primeiras ideias que culminaram com o projeto do computador e a Ciência da Computação, foram apresentadas por mentes com um íntimo desejo de modificar suas realidades, tornando processos demorados e manuais realizados pelo ser humano em processos automatizados. Desde então, muitos outros projetos foram apresentados e implementados até se chegar ao modelo do computador atual. Isso contribuiu para a evolução do hardware, do software e, consequentemente, dos SO. Dessa forma, associe os itens fornecidos com as suas respectivas sentenças corretas:")
    print("\nI-   John Pesper Eckert Jr.")
    print("\nII- Howard Aiken.")
    print("\nIII- Alan Turing.")
    print("\n\n(   ) Criador da máquina Colossus, responsável por decifrar as mensagens geradas pela máquina alemã Enigma.")
    print("\n(   ) Criador do projeto mais conhecido da década de 1940, e considerado o primeiro computador digital e eletrônico.")
    print("\n(   ) Cientista da Universidade de Harvard e criador da máquina Mark I.")
    print("\n\nA partir das definições fornecidas, a sequência CORRETA para as assertivas é:")
    
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
    A = "II e III."
    B = "I e IV."
    C = "Somente a III."
    D = "Somente a II."

    ops = [A,B,C,D]
    rCorreta = A
    gabarito.append("A")

    print("3  As primeiras ideias que culminaram com o projeto do computador e a Ciência da Computação, foram apresentadas por mentes com um íntimo desejo de modificar suas realidades, tornando processos demorados e manuais realizados pelo Ser Humano em processos automatizados. Desde então, muitos outros projetos foram apresentados e implementados até se chegar ao modelo do computador atual. Isso contribuiu para a evolução do hardware, do software e, consequentemente, dos SO. Dessa forma, assinale a alternativa que indica as assertivas sobre a relação dos primeiros projetos de computadores e os SO:")
    print("\n\nI-  As primeiras máquinas, década de 1940, já não existiam sem um SO e já contavam com dispositivos como teclados e monitores.")
    print("\nII-  As primeiras máquinas, década de 1940, existiam sem um SO e também não contavam com dispositivos como teclados e monitores, sendo que o conceito de SO só surgiu a partir da década de 1950.")
    print("\nIII-  A década de 1940 também foi marcada pela falta do conceito de linguagens de programação, sendo que as máquinas dessa década eram controladas através da combinação de fios conectados em painéis.")
    print("\nIV- Já a década de 1950 foi marcada pela evolução nas máquinas com a substituição dos transistores pelas válvulas.")
    print("\n\nA partir das definições fornecidas, estão CORRETAS as assertivas:")
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
    A = "Na década de 1950 a introdução das válvulas possibilitou o aumento da eficiência no processamento dos computadores"
    B = "Aos transistores, década de 1950, juntou-se a memória magnética, com sua contribuição para o aumento da velocidade de acesso aos dados, para a capacidade de armazenamento de dados maior, e a possibilidade da criação de projetos de computadores menores."
    C = "Porém, a geração de 1950 pouco mudou as formas de se utilizar o computador, pois continuou baseada nos chamados cartões perfurados."
    D = "Apesar da geração de 1950 ainda permanecer com a utilização dos cartões perfurados, os processos de interação com os computadores, que levavam longos períodos, passaram a consumir menos tempo."

    ops = [A,B,C,D]
    rCorreta = B
    gabarito.append("B")

    print("4  As primeiras ideias que culminaram com o projeto do computador e a Ciência da Computação foram apresentadas por mentes com um íntimo desejo de modificar suas realidades, tornando processos demorados e manuais realizados pelo Ser Humano em processos automatizados. Desde então, muitos outros projetos foram apresentados e implementados até se chegar ao modelo do computador atual. Isso contribuiu para a evolução do hardware, do software e, consequentemente, dos SO. Dessa forma, assinale a alternativa CORRETA sobre a relação dos primeiros projetos de computadores e os SO:")
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
            pontos +=2.5
    elif r == "C":
        resp.append(r)
        r=C
    elif r == "D":
        resp.append(r)
        r=D
    os.system("cls")
questao4()

print("============GABARITO============")
for i in range(0,4):
    print(gabarito[i])
print("============SUA PROVA============")
for i in range(0,4):
    print(resp[i])
print("Sua pontuação foi de: {}".format(pontos))