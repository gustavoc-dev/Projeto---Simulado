import os

gabarito = []
resp = []
pontos = 0

def questao1():
    global pontos
    A = "V – V – F – V."
    B = "F – F – F – V."
    C = "F – F – V – F."
    D = "V – V – F – F."

    ops = [A,B,C,D]
    rCorreta = C
    gabarito.append("C")

    print("1  A construção do middleware de sistemas distribuídos é caracterizada pelo seu alto grau de abstração, o que permite a existência de vários paradigmas com arquiteturas próprias e diferentes formatos de comunicação. Isso pode ser verificado na existência de diferentes implementações de sistemas distribuídos, como os baseados em objetos e arquivos distribuídos, os baseados na web, e os sistemas de multimídia distribuídos. Com isso em mente, avalie as sentenças relacionadas à construção de sistemas distribuídos classificando com V as sentenças verdadeiras e F as falsas:")
    print("\n(   )  Apesar de os sistemas distribuídos baseados em objetos possuírem uma arquitetura baseada em objetos distribuídos esta nada tem a ver com o conceito de orientação a objetos, pois, apesar de os objetos encapsularem dados, seus métodos não são disponibilizados por meio de interfaces.")
    print("\n(   )  Em sistemas de arquivos distribuídos o modelo de acesso remoto permite ao cliente baixar e acessar os arquivos localmente. Após as atualizações, o cliente faz o upload do arquivo atualizado para o servidor.")
    print("\n(   )  A arquitetura cliente/servidor típica dos sistemas baseados na web evoluiu de duas para três camadas, na qual encontramos um servidor web, um servidor de aplicação e um servidor de banco de dados.")
    print("\n(   )  A comunicação entre sistemas distribuídos baseados na web é bastante simples, pois ocorre via HTTP apenas.")
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
            pontos +=2
    elif r == "D":
        resp.append(r)
        r=D
    os.system("cls")
questao1()
def questao2():
    global pontos
    A = "V – V – F – F."
    B = "F – V – V – F."
    C = "V – V – F – F."
    D = "V – F – F – V."

    ops = [A,B,C,D]
    rCorreta = D
    gabarito.append("D")

    print("2  A base dos sistemas distribuídos é o compartilhamento. A implementação de sistemas de arquivos distribuídos permite que usuários possam acessar e armazenar arquivos de dados a partir de qualquer dispositivo em uma rede exatamente como se o estivessem fazendo localmente, tendo-se ainda garantidos desempenho e controle de acesso. Sendo assim, avalie as sentenças relacionadas à construção de sistemas de arquivos distribuídos classificando com V as sentenças verdadeiras e F as falsas:")
    print("\n(   )  Sistemas de arquivos distribuídos seguem uma arquitetura cliente/servidor sendo o NFS a arquitetura mais utilizada.")
    print("\n(   )  Sistemas de arquivos distribuídos seguem uma arquitetura cliente/servidor sendo a RPC a arquitetura mais utilizada.")
    print("\n(   )  No tocante à consistência e replicação para sistemas de arquivos distribuídos, tanto a replicação do lado do servidor quanto os serviços de cache de dados no lado do cliente são estratégias comuns.")
    print("\n(   )  No tocante à consistência e replicação para sistemas de arquivos distribuídos, a replicação do lado do servidor não costuma ser uma estratégia comum, diferentemente dos serviços de cache de dados no lado do cliente.")
    print("\nAgora, assinale a alternativa CORRETA:\n")
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
    A = "As sentenças I e III estão corretas."
    B = "As sentenças II e IV estão corretas."
    C = "As sentenças I e II estão corretas."
    D = "As sentenças III e IV estão corretas."

    ops = [A,B,C,D]
    rCorreta = A
    gabarito.append("A")

    print("3  A construção do middleware de sistemas distribuídos é caracterizada pelo seu alto grau de abstração, o que permite a existência de vários paradigmas com arquiteturas próprias e diferentes formatos de comunicação. Isso pode ser verificado na existência de diferentes implementações de sistemas distribuídos, como os baseados em objetos e arquivos distribuídos, os baseados na web, e os sistemas de multimídia distribuídos. Com isso em mente, avalie as sentenças relacionadas à construção de sistemas distribuídos:")
    print("\nI-    Sistemas multimídia distribuídos devem ser capazes de manipular grandes volumes de dados, como vídeos em alta definição, por exemplo, sem perder o desempenho.")
    print("\nII-   Sistemas distribuídos baseados na web tem como principal característica o fato de competirem com outras aplicações por largura de banda.")
    print("\nIII-  A comunicação em sistemas distribuídos baseados em objetos se dá através da vinculação de um cliente a um processo invocando os métodos do objeto via proxy. É o que chamamos de invocação de método remoto ou RMI.")
    print("\nIV-  Uma das formas de RMI é a invocação estática, na qual o método que será invocado é selecionado em tempo de execução.")
    print("\nAgora, indique a alternativa CORRETA:\n")
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
questao3()
def questao4():
    global pontos
    A = "As sentenças I e III estão corretas."
    B = "As sentenças II e IV estão corretas."
    C = "As sentenças I e II estão corretas."
    D = "As sentenças III e IV estão corretas."

    ops = [A,B,C,D]
    rCorreta = D
    gabarito.append("D")

    print("4  A base dos sistemas distribuídos é o compartilhamento. A implementação de sistemas de arquivos distribuídos permite que usuários possam acessar e armazenar arquivos de dados a partir de qualquer dispositivo em uma rede exatamente como se o estivessem fazendo localmente, tendo-se ainda garantidos desempenho e controle de acesso. Sendo assim, avalie as sentenças relacionadas à construção de sistemas de arquivos distribuídos:")
    print('\nI-    Procedimentos compostos, caracterizados pelo agrupamento de várias RPC em uma única requisição consistem em uma técnica de replicação no lado do cliente.')
    print("\nII-   Procedimentos compostos, caracterizados pelo agrupamento de várias RPC em uma única requisição é uma forma de tornar sistemas de arquivos distribuídos tolerantes a falhas.")
    print("\nIII-  O acesso a arquivos remotos se dá através de dois modelos: modelo de acesso remoto e modelo de carga/atualização.")
    print("\nIV-  O compartilhamento de arquivos distribuídos se dá pela implementação de um serviço de arquivo remoto, capaz de permitir a transparência de acesso às máquinas clientes.")
    print("\nAgora, indique a alternativa CORRETA:\n")
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
    A = "V – V – F – F."
    B = "F – F – V – V."
    C = "F – V – F – V." 
    D = "V – F – F – F."

    ops = [A,B,C,D]
    rCorreta = A
    gabarito.append("A")

    print("5  Desde sua criação pelo CERN, a web passou de um sistema baseado em documentos estáticos para um grande sistema distribuído, acessado por milhões de usuários no mundo todo. Mais recentemente, com o compartilhamento dos serviços percebemos que a web passou a promover uma forma mais rica de interoperabilidade aos seus usuários. Sendo assim, avalie as sentenças relacionadas à construção de sistemas distribuídos baseados na web classificando com V as sentenças verdadeiras e F as falsas:")
    print("\n(   )  Para que um serviço web possa ser consumido, a comunicação entre os processos de uma máquina cliente e de uma máquina servidora ocorre via protocolo SOAP.")
    print("\n(   )  Sistemas distribuídos baseados na web possuem uma arquitetura cliente/servidor que se utiliza de um navegador para apresentar suas aplicações denominadas documentos web.")
    print("\n(   )  Serviços web fazem uso de scripts do lado do servidor que processam o documento antes de enviá-lo ao cliente.")
    print("\n(   )  Em sistemas distribuídos baseados na web, navegadores web e proxies web são os principais processos do lado do servidor.")
    print("\nAgora, indique a alternativa CORRETA:\n")
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
questao5()

print("============GABARITO============")
for i in range(0,5):
    print(gabarito[i])
print("============SUA PROVA============")
for i in range(0,5):
    print(resp[i])
print("Sua pontuação foi de: {}".format(pontos))