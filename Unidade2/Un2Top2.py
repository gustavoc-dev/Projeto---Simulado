import os

gabarito = []
resp = []
pontos = 0

def questao1():
    global pontos
    A = "As sentenças I e II representam proposições verdadeiras, e a II é uma justificativa correta de I."
    B = "As sentenças I e II representam proposições verdadeiras, mas a II não é uma justificativa correta de I."
    C = "A sentença I representa uma proposição verdadeira, e a II uma proposição falsa."
    D = "A sentença I representa uma proposição falsa, e a II uma proposição verdadeira."

    ops = [A,B,C,D]
    rCorreta = A
    gabarito.append("A")

    print("1  Os sistemas distribuídos constituem um tipo especial de sistema pois rodam em ambientes heterogêneos (plataformas 32 e 64 bits, diferentes sistemas operacionais, diferentes tipos de dispositivos, dispositivos e servidores distribuídos globalmente, entre outros) e precisam que seus componentes (físicos e lógicos) abstraiam essa miríade de ambientes para que o usuário tenha a impressão de que todos os processos, serviços, operações e tarefas acessadas estão sendo executados apenas na rede a qual ele está conectado. Dessa forma, esses sistemas são construídos de maneira que o seu hardware e o seu software consigam abstrair especificidades dos dispositivos, das tecnologias e da infraestrutura de rede empregadas. Avalie as sentenças e a relação proposta entre elas tendo em mente o cenário apresentado anteriormente.")
    print('\nI-  Mesmo os modelos que lidam com as características físicas dos sistemas distribuídos precisam de uma medida de abstração para garantir uma comunicação entre os seus dispositivos em rede, e suas trocas de mensagens, independentes entre si.')
    ("\n\nPORQUE\n\n")
    print("II- As arquiteturas para sistemas distribuídos apresentam tais sistemas sob uma visão de atividades computacionais e sua relação de comunicação com os componentes computacionais suportados pelas infraestruturas das redes que os conectam.")
    print("\n\nAgora, assinale a alternativa que apresenta a resposta CORRETA:\n\n")
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
    A = "A contemporaneidade dos sistemas distribuídos é alcançada quando dispositivos diferentes dos computadores pessoais e notebooks, mas com o mesmo conceito, são incluídos como elementos integrantes desses sistemas, tratam-se dos dispositivos móveis."
    B = "Inicialmente a característica “distribuída” dos sistemas distribuídos surgiu como uma resposta natural ao nascimento das redes de computadores e ao seu amadurecimento. Os serviços utilizados estavam baseados principalmente na transferência de arquivos através da rede, inclusive da internet e no compartilhamento de recursos físicos existentes nesses ambientes."
    C = "A contemporaneidade dos sistemas distribuídos é alcançada quando dispositivos diferentes dos computadores pessoais e notebooks, mas com o mesmo conceito, são incluídos como elementos integrantes desses sistemas, tratam-se dos dispositivos móveis. Nesse contexto, novos serviços são tratados por esses sistemas, como os de multimídias, e o crescimento da heterogeneidade e dos dispositivos conectados, aumenta significativamente."
    D = "Inicialmente a característica “distribuída” dos sistemas distribuídos surgiu como uma resposta natural ao nascimento das redes de computadores e ao seu amadurecimento. Os serviços distribuídos utilizados estavam baseados principalmente na transferência de arquivos através da rede, inclusive da internet, e no compartilhamento de recursos físicos existentes nesses ambientes. Apesar disso, esses primeiros sistemas já rodavam em ambiente heterogêneos, mas seguindo padrões de qualidade de serviço muito baixos."

    ops = [A,B,C,D]
    rCorreta = D
    gabarito.append("D")

    print("2  As implementações de sistemas distribuídos atuais conseguem criar abstrações significativas para os seus atributos físicos, permitindo que a comunicação entre as conexões de seus dispositivos interligados em rede coordene ações através da troca de mensagens, mantendo-os independentes entre si. Até essa condição ser alcançada, esses sistemas passaram por algumas gerações marcadas pelo tipo de tecnologias existentes aplicadas em cada uma delas. Com isso em mente, avalie as sentenças e indique a INCORRETA no tocante as gerações dos sistemas distribuídos.")
    
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
    A = "A característica de expansibilidade dos sistemas distribuídos já era considerável (grande) mesmo na primeira geração desses sistemas."
    B = "A era da internet inaugura uma nova preocupação (característica) significativa relacionada aos sistemas distribuídos, a qualidade de serviço."
    C = "As características de expansibilidade e qualidade de serviço já nasceram maduras nos sistemas distribuídos, uma vez que do seu surgimento os ambientes computacionais já estavam maduros e as suas tecnologias."
    D = "A era da internet inaugura uma nova preocupação (característica) significativa relacionada aos sistemas distribuídos, a expansibilidade"

    ops = [A,B,C,D]
    rCorreta = B
    gabarito.append("B")

    print("3  As implementações de sistemas distribuídos atuais conseguem criar abstrações significativas para os seus atributos físicos, permitindo que a comunicação entre as conexões de seus dispositivos interligados em rede coordene ações através da troca de mensagens, mantendo-os independentes entre si. Até essa condição ser alcançada esses sistemas passaram por algumas gerações marcadas pelo tipo de tecnologias existentes aplicadas em cada uma delas. Com isso em mente, avalie as sentenças e indique qual a correta no tocante às gerações dos sistemas distribuídos:")
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
questao3()
def questao4():
    global pontos
    A = "V – V – V – V."
    B = "V – V – V – F."
    C = "V – F – F – V." 
    D = "F – F – V – V. "

    ops = [A,B,C,D]
    rCorreta = B
    gabarito.append("B")

    print("4  Sistemas distribuídos compreendem uma série de elementos, conceitos e práticas de projeto para a sua construção. Passando por infraestrutura física e lógica de redes de computadores, e outros dispositivos com conectividade, SO, arquiteturas de sistemas, entre outros. Pode-se então formalizar definições para esse tipo de sistema que compreendam todos esses elementos. Com isso em mente, avalie as sentenças sobre as características dos sistemas distribuídos:")
    print("\n\n(   ) Os sistemas distribuídos precisam de um SO específico que lide com códigos distribuídos.")
    print("(   ) As aplicações desenvolvidas são desenvolvidas com características que as permitam se comunicar com outras aplicações, em máquinas diferentes e remotas, para a realização das atividades de um sistema distribuído.")
    print("(   ) As arquiteturas físicas e aquelas de software de servidores seguem estruturas e princípios que permitam aos elementos dos sistemas distribuídos se comunicarem de maneira remota para a realização das suas atividades dando ao usuário uma impressão de rede local.")
    print("(   ) As arquiteturas físicas e aquelas de software de servidores seguem estruturas e princípios que permitam aos elementos dos sistemas distribuídos se comunicarem de maneira remota para a realização das suas atividades dando ao usuário uma visão de comunicação distribuída entre os vários dispositivos que compõem o sistema.")
    print("\n\nAgora, assinale a alternativa CORRETA:\n\n")
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
    A = "As sentenças II e III estão corretas."
    B = "As sentenças I e IV estão corretas."
    C = "As sentenças II e IV estão corretas." 
    D = "As sentenças I e III estão corretas."

    ops = [A,B,C,D]
    rCorreta = C
    gabarito.append("C")

    print("5  Elementos para uma arquitetura de sistemas distribuídos envolvem desde aspectos lógicos, como aspectos físicos que estão mutuamente relacionados entre si, e relacionados com a complexidade desse tipo de sistema. Dessa forma, avalie as sentenças relacionadas aos aspectos de arquitetura para os sistemas distribuídos:")
    print("\n\nI-   O suporte a uma conversa em uma determinada rede social através de um dispositivo móvel, por exemplo, diz respeito apenas ao aspecto de comunicação em um ambiente de sistemas distribuídos.")
    print("II-  O suporte a uma conversa em uma determinada rede social através de um dispositivo móvel, por exemplo, diz respeito tanto ao aspecto de responsabilidade quanto ao de comunicação em um ambiente de sistemas distribuídos.")
    print("III- O suporte a uma conversa em uma determinada rede social através de um dispositivo móvel, por exemplo, diz respeito apenas ao aspecto de responsabilidade em um ambiente de sistemas distribuídos.")
    print("IV- As entidades relacionadas aos aspectos de arquitetura dos sistemas distribuídos podem ser físicas (sensores e controladores, por exemplo) quanto lógicas como trechos de códigos de programas.")
    print("\n\nAgora, indique a alternativa CORRETA:\n\n")
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
questao5()

print("============GABARITO============")
for i in range(0,5):
    print(gabarito[i])
print("============SUA PROVA============")
for i in range(0,5):
    print(resp[i])
print("Sua pontuação foi de: {}".format(pontos))