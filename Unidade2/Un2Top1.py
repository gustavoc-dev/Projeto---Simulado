import os

gabarito = []
resp = []
pontos = 0

def questao1():
    global pontos
    A = "SO de rede e os sistemas distribuídos."
    B = "SO de rede e os clusters. "
    C = "Sistemas distribuídos e os clusters."
    D = "SO de rede e os sistemas fracamente acoplados. "

    ops = [A,B,C,D]
    rCorreta = A
    gabarito.append("A")

    print("1  A popularização e avanço dos computadores pessoais e estações de trabalho juntamente com as tecnologias de informação e comunicação, especialmente as associadas às redes de computadores, propiciou o surgimento de um novo modelo de computação, chamado modelo de rede de computadores. Esse novo modelo introduziu um novo tipo de sistema computacional, os hosts, e, consequentemente, a necessidade de SO fracamente acoplados. Dessa forma, indique a sentença que traz os dois tipos desses SO:")
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
    A = "Para a percepção do usuário final, um sistema distribuído é utilizado transparentemente, como se não existisse uma infraestrutura de rede de computadores dando suporte a ele, e que apesar de distribuído por essa rede, o usuário o percebe como um único sistema."
    B = "Tendo como ponto de partida uma visão de implementação, com suporte a ambientes heterogêneos e oferecendo uma visão única de sistema, esses sistemas muitas vezes são organizados como uma camada de software chamada middleware."
    C = "Para a percepção do usuário final, um sistema distribuído é utilizado transparentemente, como se não existisse uma infraestrutura de rede de computadores dando suporte a ele, e que apesar de distribuído por essa rede, o usuário o percebe como um único sistema. Essa característica de transparência é muitas vezes denominada middleware."
    D = "Em uma percepção de hardware um sistema distribuído congrega uma miríade de sistemas computacionais distintos, com memórias e processadores como seus recursos. Mesmo assim, há a impressão de que existe uma única máquina uma vez que se tem um único SO gerenciando tais recursos."

    ops = [A,B,C,D]
    rCorreta = C
    gabarito.append("C")

    print("2  Sistemas distribuídos compreendem uma série de elementos, conceitos e práticas de projeto para a sua construção, passando por infraestrutura física e lógica de redes de computadores, e outros dispositivos com conectividade, SO, arquiteturas de sistemas, entre outros. Pode-se então formalizar definições para esse tipo de sistema que compreendam todos esses elementos. Com isso em mente, assinale a sentença que não traz uma definição correta para o conceito de sistemas distribuídos.")
    
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
    A = "V – V – F – F. "
    B = "F – V – V – F. "
    C = "F – F – V – V."
    D = "V – V – F – F. "

    ops = [A,B,C,D]
    rCorreta = A
    gabarito.append("A")

    print("3  A escalabilidade é uma característica imprescindível dos sistemas distribuídos, uma vez que ela deve manter a eficiência do sistema mesmo com a inserção de novos recursos ou usuários. Logo, na construção de um sistema distribuído existem desafios significativos para que essa sua característica seja alcançada. Com isso em mente, avalie as sentenças relacionadas a esses desafios classificando V para as sentenças verdadeiras e F para as falsas.")
    print("\n\n(   ) Os controles relacionados ao custo dos recursos físicos, considerando a inclusão de novos recursos, devem ser aceitáveis.")
    print("(   ) No controle associado à perda de desempenho, considerando a escalabilidade, a perda deve ser menor que a função do tempo de acesso aos dados do sistema.")
    print("(   ) Os controles relacionados ao custo dos recursos físicos, considerando a inclusão de novos recursos, estão sempre disponíveis já que se deve garantir a característica da escalabilidade.")
    print("(   ) No controle associado à perda de desempenho, considerando a escalabilidade, a perda não deve ser menor que a função do tempo de acesso aos dados do sistema.")
    print("\n\nAssinale a alternativa CORRETA:\n\n")
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
    A = "As sentenças I e II representam proposições verdadeiras, mas a II não é uma justificativa correta da I."
    B = "As sentenças I e II representam proposições verdadeiras, e a II é uma justificativa correta da I."
    C = "As sentenças I e II não representam proposições verdadeiras."
    D = "A sentenças I é uma proposição verdadeira, porém a II é uma proposição falsa."

    ops = [A,B,C,D]
    rCorreta = B
    gabarito.append("B")

    print("4  Sistemas distribuídos compreendem uma série de características (heterogeneidade, escalabilidade, concorrência, segurança, entre outras) que devem ser alcançadas para viabilizar um projeto para um sistema dessa natureza. Como esses sistemas lidam, por vias de regra, com infraestruturas física e lógica de redes de computadores (e outros dispositivos com conectividade), SO, arquiteturas de sistemas, entre outros, as características de concorrência aos recursos e, consequentemente, sua segurança são condições necessárias a se alcançar. Com isso em mente, avalie a sentença de afirmação com a sua sentença de explicação relacionadas a essas duas características dos sistemas distribuídos.")
    print('\nI-  A concorrência nesse tipo de ambiente é perfeitamente natural, pois existe uma chance potencialmente alta de que inúmeros usuários concorram para a utilização de um dado recurso compartilhado no sistema. Logo, esses inúmeros usuários distintos, cada um em seu dispositivo, podem compartilhar arquivos (como fotos, áudios, vídeos, entre outros) sempre que necessário. Para tanto, eles devem, de alguma maneira, possuir uma identificação no sistema (rede de origem, login, senha, protocolo de segurança, entre outros).')
    ("\n\nPORQUE\n\n")
    print("II- Parte, ou grande parte, da característica de concorrência está associada ao quesito segurança, uma vez que o sistema deve garantir a ocultação dos conteúdos das mensagens, bem como deve garantir, de maneira confiável, as identidades do emissor da mensagem e do seu receptor.")
    print("\n\nAgora, assinale a alternativa que apresenta a resposta CORRETA:\n\n")
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
    A = "V – V – F – F. "
    B = "F – V – V – F."
    C = "F – F – V – F." 
    D = "V – V – F – F."

    ops = [A,B,C,D]
    rCorreta = C
    gabarito.append("C")

    print("5  A escalabilidade é uma característica imprescindível dos sistemas distribuídos, uma vez que ela deve manter a eficiência do sistema mesmo com a inserção de novos recursos ou usuários. Logo, na construção de um sistema distribuído existem desafios significativos para que essa sua característica seja alcançada. Com isso em mente, avalie as sentenças relacionadas a esses desafios classificando com V as sentenças verdadeiras e F as falsas.")
    print("\n\n(   ) No controle associado à perda de desempenho, considerando a escalabilidade, a perda pode ser menor, ou maior, que a função do tempo de acesso aos dados do sistema. Isso dependerá do grau de escalabilidade que se quer alcançar com o sistema.")
    print("(   ) O controle relacionado ao custo dos recursos físicos, considerando a inclusão de novos recursos, possui sua disponibilidade diretamente proporcional ao grau de escalabilidade que se deseja dar a um determinado módulo do sistema.")
    print("(   ) Deve-se evitar o esgotamento dos recursos de software, porém fazer uma previsão antecipada da escalabilidade de um sistema distribuído não é uma tarefa fácil. Logo, uma das abordagens para evitar este esgotamento pode ser através da adaptação às mudanças.")
    print("(   ) Deve-se evitar o esgotamento dos recursos de software, para isso é imprescindível uma previsão antecipada da escalabilidade, mesmo que para um sistema distribuído isso não seja uma tarefa fácil. De qualquer forma, a adaptação às mudanças não pode ser uma abordagem sugerida uma vez que não se trata de uma medida eficaz.")
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